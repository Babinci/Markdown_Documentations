# Build a Product Management Android App with Jetpack Compose

This tutorial demonstrates how to build a basic product management app. The app demonstrates management operations, photo upload, account creation and authentication using:

- [Supabase Database](https://supabase.com/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](https://supabase.com/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
- [Supabase Auth](https://supabase.com/docs/guides/auth) - users log in through magic links sent to their email (without having to set up a password).
- [Supabase Storage](https://supabase.com/docs/guides/storage) - users can upload a profile photo.

![manage-product-cover](https://supabase.com/docs/img/guides/kotlin/manage-product-cover.png)

If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/hieuwu/product-sample-supabase-kt).

## Project setup

Before we start building we're going to set up our Database and API. This is as simple as starting a new Project in Supabase and then creating a "schema" inside the database.

### Create a project

1. [Create a new project](https://app.supabase.com/) in the Supabase Dashboard.
2. Enter your project details.
3. Wait for the new database to launch.

### Set up the database schema

Now we are going to set up the database schema. You can just copy/paste the SQL from below and run it yourself.

```sql
-- Create a table for public profiles
create table  public.products (
    id uuid not null default gen_random_uuid (),
    name text not null,
    price real not null,
    image text null,
    constraint products_pkey primary key (id)
  ) tablespace pg_default;

-- Set up Storage!
insert into storage.buckets (id, name)
  values ('Product Image', 'Product Image');

-- Set up access controls for storage.
-- See https://supabase.com/docs/guides/storage/security/access-control#policy-examples for more details.
CREATE POLICY "Enable read access for all users" ON "storage"."objects"
AS PERMISSIVE FOR SELECT
TO public
USING (true)

CREATE POLICY "Enable insert for all users" ON "storage"."objects"
AS PERMISSIVE FOR INSERT
TO authenticated, anon
WITH CHECK (true)

CREATE POLICY "Enable update for all users" ON "storage"."objects"
AS PERMISSIVE FOR UPDATE
TO public
USING (true)
WITH CHECK (true)
```

### Get the API keys

Now that you've created some database tables, you are ready to insert data using the auto-generated API.
We just need to get the Project URL and `anon` key from the API settings.

1. Go to the [API Settings](https://app.supabase.com/project/_/settings/api) page in the Dashboard.
2. Find your Project `URL`, `anon`, and `service_role` keys on this page.

### Set up Google authentication

From the [Google Console](https://console.developers.google.com/apis/library), create a new project and add OAuth2 credentials.

![Create Google OAuth credentials](https://supabase.com/docs/img/guides/kotlin/google-cloud-oauth-credentials-create.png)

In your [Supabase Auth settings](https://app.supabase.com/project/_/auth/providers) enable Google as a provider and set the required credentials as outlined in the [auth docs](https://supabase.com/docs/guides/auth/social-login/auth-google).

## Building the app

### Create new Android project

Open Android Studio > New Project > Base Activity (Jetpack Compose).

![Android Studio new project](https://supabase.com/docs/img/guides/kotlin/android-studio-new-project.png)

### Set up API key and secret securely

#### Create local environment secret

Create or edit the `local.properties` file at the root (same level as `build.gradle`) of your project.

> **Note**: Do not commit this file to your source control, for example, by adding it to your `.gitignore` file!

```
SUPABASE_ANON_KEY=YOUR_SUPABASE_ANON_KEY
SUPABASE_URL=YOUR_SUPABASE_URL
```

#### Read and set value to `BuildConfig`

In your `build.gradle` (app) file, create a `Properties` object and read the values from your `local.properties` file by calling the `buildConfigField` method:

```groovy
defaultConfig {
   applicationId "com.example.manageproducts"
   minSdkVersion 22
   targetSdkVersion 33
   versionCode 5
   versionName "1.0"
   testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
   // Set value part
   Properties properties = new Properties()
   properties.load(project.rootProject.file("local.properties").newDataInputStream())
   buildConfigField("String", "SUPABASE_ANON_KEY", "\"${properties.getProperty("SUPABASE_ANON_KEY")}\"")
   buildConfigField("String", "SECRET", "\"${properties.getProperty("SECRET")}\"")
   buildConfigField("String", "SUPABASE_URL", "\"${properties.getProperty("SUPABASE_URL")}\"")
}
```

#### Use value from `BuildConfig`

Read the value from `BuildConfig`:

```kotlin
val url = BuildConfig.SUPABASE_URL
val apiKey = BuildConfig.SUPABASE_ANON_KEY
```

### Set up Supabase dependencies

![Gradle dependencies](https://supabase.com/docs/img/guides/kotlin/gradle-dependencies.png)

In the `build.gradle` (app) file, add these dependencies then press "Sync now." Replace the dependency version placeholders `$supabase_version` and `$ktor_version` with their respective latest versions.

```groovy
implementation "io.github.jan-tennert.supabase:postgrest-kt:$supabase_version"
implementation "io.github.jan-tennert.supabase:storage-kt:$supabase_version"
implementation "io.github.jan-tennert.supabase:auth-kt:$supabase_version"
implementation "io.ktor:ktor-client-android:$ktor_version"
implementation "io.ktor:ktor-client-core:$ktor_version"
implementation "io.ktor:ktor-utils:$ktor_version"
```

Also in the `build.gradle` (app) file, add the plugin for serialization. The version of this plugin should be the same as your Kotlin version.

```groovy
plugins {
    ...
    id 'org.jetbrains.kotlin.plugin.serialization' version '$kotlin_version'
    ...
}
```

### Set up Hilt for dependency injection

In the `build.gradle` (app) file, add the following:

```groovy
implementation "com.google.dagger:hilt-android:$hilt_version"
annotationProcessor "com.google.dagger:hilt-compiler:$hilt_version"
implementation("androidx.hilt:hilt-navigation-compose:1.0.0")
```

Create a new `ManageProductApplication.kt` class extending Application with `@HiltAndroidApp` annotation:

```kotlin
// ManageProductApplication.kt
@HiltAndroidApp
class ManageProductApplication: Application()
```

Open the `AndroidManifest.xml` file, update name property of Application tag:

```xml
<application
    ...
    android:name=".ManageProductApplication"
    ...
</application>
```

Create the `MainActivity`:

```kotlin
@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    //This will come later
}
```

### Provide Supabase instances with Hilt

To make the app easier to test, create a `SupabaseModule.kt` file as follows:

```kotlin
@InstallIn(SingletonComponent::class)
@Module
object SupabaseModule {
    @Provides
    @Singleton
    fun provideSupabaseClient(): SupabaseClient {
        return createSupabaseClient(
            supabaseUrl = BuildConfig.SUPABASE_URL,
            supabaseKey = BuildConfig.SUPABASE_ANON_KEY
        ) {
            install(Postgrest)
            install(Auth) {
                flowType = FlowType.PKCE
                scheme = "app"
                host = "supabase.com"
            }
            install(Storage)
        }
    }

    @Provides
    @Singleton
    fun provideSupabaseDatabase(client: SupabaseClient): Postgrest {
        return client.postgrest
    }

    @Provides
    @Singleton
    fun provideSupabaseAuth(client: SupabaseClient): Auth {
        return client.auth
    }

    @Provides
    @Singleton
    fun provideSupabaseStorage(client: SupabaseClient): Storage {
        return client.storage
    }
}
```

### Create a data transfer object

Create a `ProductDto.kt` class and use annotations to parse data from Supabase:

```kotlin
@Serializable
data class ProductDto(
    @SerialName("name")
    val name: String,
    @SerialName("price")
    val price: Double,
    @SerialName("image")
    val image: String?,
    @SerialName("id")
    val id: String,
)
```

Create a Domain object in `Product.kt` expose the data in your view:

```kotlin
data class Product(
    val id: String,
    val name: String,
    val price: Double,
    val image: String?
)
```

### Implement repositories

Create a `ProductRepository` interface and its implementation named `ProductRepositoryImpl`. This holds the logic to interact with data sources from Supabase. Do the same with the `AuthenticationRepository`.

Create the Product Repository:

```kotlin
interface ProductRepository {
    suspend fun createProduct(product: Product): Boolean
    suspend fun getProducts(): List<ProductDto>?
    suspend fun getProduct(id: String): ProductDto
    suspend fun deleteProduct(id: String)
    suspend fun updateProduct(
        id: String, name: String, price: Double, imageName: String, imageFile: ByteArray
    )
}
```

```kotlin
class ProductRepositoryImpl @Inject constructor(
    private val postgrest: Postgrest,
    private val storage: Storage,
) : ProductRepository {
    override suspend fun createProduct(product: Product): Boolean {
        return try {
            withContext(Dispatchers.IO) {
                val productDto = ProductDto(
                    name = product.name,
                    price = product.price,
                )
                postgrest.from("products").insert(productDto)
                true
            }
            true
        } catch (e: java.lang.Exception) {
            throw e
        }
    }

    override suspend fun getProducts(): List<ProductDto>? {
        return withContext(Dispatchers.IO) {
            val result = postgrest.from("products")
                .select().decodeList<ProductDto>()
            result
        }
    }

    override suspend fun getProduct(id: String): ProductDto {
        return withContext(Dispatchers.IO) {
            postgrest.from("products").select {
                filter {
                    eq("id", id)
                }
            }.decodeSingle<ProductDto>()
        }
    }

    override suspend fun deleteProduct(id: String) {
        return withContext(Dispatchers.IO) {
            postgrest.from("products").delete {
                filter {
                    eq("id", id)
                }
            }
        }
    }

    override suspend fun updateProduct(
        id: String,
        name: String,
        price: Double,
        imageName: String,
        imageFile: ByteArray
    ) {
        withContext(Dispatchers.IO) {
            if (imageFile.isNotEmpty()) {
                val imageUrl =
                    storage.from("Product%20Image").upload(
                        path = "$imageName.png",
                        data = imageFile,
                        upsert = true
                    )
                postgrest.from("products").update({
                    set("name", name)
                    set("price", price)
                    set("image", buildImageUrl(imageFileName = imageUrl))
                }) {
                    filter {
                        eq("id", id)
                    }
                }
            } else {
                postgrest.from("products").update({
                    set("name", name)
                    set("price", price)
                }) {
                    filter {
                        eq("id", id)
                    }
                }
            }
        }
    }

    // Because I named the bucket as "Product Image" so when it turns to an url, it is "%20"
    // For better approach, you should create your bucket name without space symbol
    private fun buildImageUrl(imageFileName: String) =
        "${BuildConfig.SUPABASE_URL}/storage/v1/object/public/${imageFileName}".replace(" ", "%20")
}
```

Create the Authentication Repository:

```kotlin
interface AuthenticationRepository {
    suspend fun signIn(email: String, password: String): Boolean
    suspend fun signUp(email: String, password: String): Boolean
    suspend fun signInWithGoogle(): Boolean
}
```

```kotlin
class AuthenticationRepositoryImpl @Inject constructor(
    private val auth: Auth) : AuthenticationRepository {
    override suspend fun signIn(email: String, password: String): Boolean {
        return try {
            auth.signInWith(Email) {
                this.email = email
                this.password = password
            }
            true
        } catch (e: Exception) {
            false
        }
    }

    override suspend fun signUp(email: String, password: String): Boolean {
        return try {
            auth.signUpWith(Email) {
                this.email = email
                this.password = password
            }
            true
        } catch (e: Exception) {
            false
        }
    }

    override suspend fun signInWithGoogle(): Boolean {
        return try {
            auth.signInWith(Google)
            true
        } catch (e: Exception) {
            false
        }
    }
}
```

### Implement screens

To navigate screens, use the AndroidX navigation library. For routes, implement a `Destination` interface.

This tutorial implements several screens:
- ProductListScreen - displays all products with swipe-to-delete functionality
- ProductDetailsScreen - shows details of a single product and allows editing
- AddProductScreen - allows adding new products
- Authentication screens - for sign in and sign up

### Implement the MainActivity

The MainActivity serves as the entry point of the application and sets up navigation between different screens using Jetpack Navigation. 

### Handle deep links for OAuth

To support OAuth authentication (Google sign-in), the app implements a DeepLinkHandlerActivity that handles callbacks from authentication providers.

## Conclusion

This tutorial demonstrates how to build a complete Android product management application with Jetpack Compose and Supabase. The app showcases:

1. Secure authentication with email and Google OAuth
2. Storing and retrieving data with Supabase Database
3. File uploads with Supabase Storage
4. Modern Android development patterns with MVVM architecture
5. Dependency injection with Hilt
6. Reactive UI with Jetpack Compose

For the complete working example with all implementation details, check out the [full source code on GitHub](https://github.com/hieuwu/product-sample-supabase-kt).
