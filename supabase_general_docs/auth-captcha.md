# Enable CAPTCHA Protection

Supabase provides you with the option of adding CAPTCHA to your sign-in, sign-up, and password reset forms. This keeps your website safe from bots and malicious scripts. Supabase authentication has support for [hCaptcha](https://www.hcaptcha.com/) and [Cloudflare Turnstile](https://www.cloudflare.com/products/turnstile/).

## Sign up for CAPTCHA

### hCaptcha

Go to the [hCaptcha](https://www.hcaptcha.com/) website and sign up for an account. On the Welcome page, copy the **Sitekey** and **Secret key**.

If you have already signed up and didn't copy this information from the Welcome page, you can get the **Secret key** from the Settings page.

![Secret key settings](https://supabase.com/docs/img/guides/auth-captcha/site_secret_settings.png)

The **Sitekey** can be found in the **Settings** of the active site you created.

![Sites dashboard](https://supabase.com/docs/img/guides/auth-captcha/sites_dashboard.png)

In the Settings page, look for the **Sitekey** section and copy the key.

![Sitekey settings](https://supabase.com/docs/img/guides/auth-captcha/sitekey_settings.png)

## Enable CAPTCHA protection for your Supabase project

Navigate to the **[Auth](https://supabase.com/dashboard/project/_/settings/auth)** section of your Project Settings in the Supabase Dashboard and find the **Enable CAPTCHA protection** toggle under Settings > Authentication > Bot and Abuse Protection > Enable CAPTCHA protection.

Select your CAPTCHA provider from the dropdown, enter your CAPTCHA **Secret key**, and click **Save**.

## Add the CAPTCHA frontend component

The frontend requires some changes to provide the CAPTCHA on-screen for the user. This example uses React and the corresponding CAPTCHA React component, but both CAPTCHA providers can be used with any JavaScript framework.

### hCaptcha Implementation

Install `@hcaptcha/react-hcaptcha` in your project as a dependency.

```bash
npm install @hcaptcha/react-hcaptcha
```

Now import the `HCaptcha` component from the `@hcaptcha/react-hcaptcha` library.

```javascript
import HCaptcha from '@hcaptcha/react-hcaptcha'
```

Let's create an empty state to store our `captchaToken`

```javascript
const [captchaToken, setCaptchaToken] = useState()
```

Now let's add the `HCaptcha` component to the JSX section of our code

```jsx
<HCaptcha />
```

We will pass it the sitekey we copied from the hCaptcha website as a property along with an `onVerify` property which takes a callback function. This callback function will have a token as one of its properties. Let's set the token in the state using `setCaptchaToken`

```jsx
<HCaptcha
  sitekey="your-sitekey"
  onVerify={(token) => {
    setCaptchaToken(token)
  }}
/>
```

Now let's use the CAPTCHA token we receive in our Supabase signUp function.

```javascript
await supabase.auth.signUp({
  email,
  password,
  options: { captchaToken },
})
```

We will also need to reset the CAPTCHA challenge after we have made a call to the function above.

Create a ref to use on our `HCaptcha` component.

```javascript
const captcha = useRef()
```

Let's add a ref attribute on the `HCaptcha` component and assign the `captcha` constant to it.

```jsx
<HCaptcha
  ref={captcha}
  sitekey="your-sitekey"
  onVerify={(token) => {
    setCaptchaToken(token)
  }}
/>
```

Reset the `captcha` after the signUp function is called using the following code:

```javascript
captcha.current.resetCaptcha()
```

In order to test that this works locally we will need to use something like [ngrok](https://ngrok.com/) or add an entry to your hosts file. You can read more about this in the [hCaptcha docs](https://docs.hcaptcha.com/#local-development).

Run the application and you should now be provided with a CAPTCHA challenge.
