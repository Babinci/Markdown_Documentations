# Available Regions

Supabase offers a global network of regions where you can spin up projects, allowing you to host your data closer to your users for improved performance.

## AWS Regions

Supabase projects can be deployed in the following AWS regions:

| Region Name | Region Code | Location |
|-------------|-------------|----------|
| West US | `us-west-1` | North California |
| East US | `us-east-1` | North Virginia |
| East US | `us-east-2` | Ohio |
| Canada | `ca-central-1` | Central Canada |
| West EU | `eu-west-1` | Ireland |
| West Europe | `eu-west-2` | London |
| Central EU | `eu-central-1` | Frankfurt |
| Central Europe | `eu-central-2` | Zurich |
| North EU | `eu-north-1` | Stockholm |
| South Asia | `ap-south-1` | Mumbai |
| Southeast Asia | `ap-southeast-1` | Singapore |
| Northeast Asia | `ap-northeast-1` | Tokyo |
| Northeast Asia | `ap-northeast-2` | Seoul |
| Oceania | `ap-southeast-2` | Sydney |
| South America | `sa-east-1` | São Paulo |

## Fly Regions

Our [Fly Postgres](https://supabase.com/docs/guides/platform/fly-postgres) offering (in private alpha) is supported in every region where Fly operates.

## Choosing a Region

When selecting a region for your Supabase project, consider the following factors:

### 1. Proximity to Users

Choose a region that is geographically close to the majority of your users to minimize latency.

### 2. Compliance Requirements

Some applications have legal or regulatory requirements to store data in specific regions or countries.

### 3. Available Features

Certain features may be available only in specific regions. Check the documentation for any feature-specific region limitations.

### 4. Pricing

While Supabase pricing is consistent across regions, underlying infrastructure costs from AWS may vary slightly by region.

## Changing Regions

Currently, you cannot change the region of an existing project. If you need to move your project to a different region, you'll need to:

1. Create a new project in the desired region
2. Migrate your data to the new project
3. Update your application to connect to the new project

For more information about migrating between projects, see the [Migrating within Supabase](https://supabase.com/docs/guides/platform/migrating-and-upgrading-projects) guide.

## Region Availability and SLAs

Supabase leverages AWS infrastructure which offers industry-leading availability and reliability. However, availability may vary by region. For mission-critical applications, consider implementing multi-region strategies for increased resilience.

For the most up-to-date status of Supabase services and regions, check the [Supabase Status page](https://status.supabase.com/).
