# Set Up SSO with Okta

> **Note:** This feature is only available on the Team and Enterprise Plans. Contact [Sales](https://forms.supabase.com/enterprise) before doing these steps.

Looking for docs on how to add Single Sign-On support in your Supabase project? Head on over to [Single Sign-On with SAML 2.0 for Projects](https://supabase.com/docs/guides/auth/enterprise-sso/auth-sso-saml).

Supabase supports single sign-on (SSO) using Okta.

## Step 1: Choose to Create an App Integration

Navigate to the Applications dashboard of the Okta admin console. Click _Create App Integration_.

![Okta dashboard: Create App Integration button](https://supabase.com/docs/img/sso-okta-step-01.png)

## Step 2: Choose SAML 2.0 in the App Integration Dialog

Supabase supports the SAML 2.0 SSO protocol. Choose it from the _Create a new app integration_ dialog.

![Okta dashboard: Create new app integration dialog](https://supabase.com/docs/img/sso-okta-step-02.png)

## Step 3: Fill Out General Settings

The information you enter here is for visibility into your Okta applications menu. You can choose any values you like. `Supabase` as a name works well for most use cases.

![Okta dashboard: Create SAML Integration wizard](https://supabase.com/docs/img/sso-okta-step-03.png)

## Step 4: Fill Out SAML Settings

These settings let Supabase use SAML 2.0 properly with your Okta application. Make sure you enter this information exactly as shown on in this table and screenshot.

| Setting | Value |
| --- | --- |
| Single sign-on URL | `https://alt.supabase.io/auth/v1/sso/saml/acs` |
| Use this for Recipient URL and Destination URL | ✔️ |
| Audience URI (SP Entity ID) | `https://alt.supabase.io/auth/v1/sso/saml/metadata` |
| Default `RelayState` | `https://supabase.com/dashboard` |
| Name ID format | `EmailAddress` |
| Application username | Email |
| Update application username on | Create and update |

![Okta dashboard: Create SAML Integration wizard, Configure SAML step](https://supabase.com/docs/img/sso-okta-step-04.png)

## Step 5: Fill Out Attribute Statements

Attribute Statements allow Supabase to get information about your Okta users on each login.

**A `email` to `user.email` statement is required.** Other mappings shown below are optional and configurable depending on your Okta setup. If in doubt, replicate the same config as shown.

Share any changes, if any, from this screen with your Supabase support contact.

![Okta dashboard: Attribute Statements configuration screen](https://supabase.com/docs/img/sso-okta-step-05.png)

## Step 6: Obtain IdP Metadata URL

Supabase needs to finalize enabling single sign-on with your Okta application.

To do this scroll down to the _SAML Signing Certificates_ section on the _Sign On_ tab of the _Supabase_ application. Pick the the _SHA-2_ row with an _Active_ status. Click on the _Actions_ dropdown button and then on the _View IdP Metadata_.

This will open up the SAML 2.0 Metadata XML file in a new tab in your browser. Copy this URL and send it to your support contact and await further instructions. If you're not clear who to send this link to or need further assistance, contact [Supabase Support](https://supabase.help/).

The link usually has this structure: `https://<okta-org>.okta.com/apps/<app-id>/sso/saml/metadata`

![Okta dashboard: SAML Signing Certificates, Actions button highlighted](https://supabase.com/docs/img/sso-okta-step-06.png)

## Step 7: Wait for Confirmation

Once you've configured the Okta app as shown above, make sure you send the metadata URL and information regarding the attribute statements (if any changes are applicable) to your support contact at Supabase.

Wait for confirmation that this information has successfully been added to Supabase. It usually takes us 1 business day to configure this information for you.

## Step 8: Test Single Sign-On

Once you've received confirmation from your support contact at Supabase that SSO setup has been completed for your enterprise, you can ask some of your users to sign in via their Okta account.

You ask them to enter their email address on the [Sign in with SSO](https://supabase.com/dashboard/sign-in-sso) page.

If sign in is not working correctly, reach out to your support contact at Supabase for further guidance.
