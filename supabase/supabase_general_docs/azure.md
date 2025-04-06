# Set Up SSO with Azure AD

This feature is only available on the Team and Enterprise Plans. Contact [Sales](https://forms.supabase.com/enterprise) before doing these steps.

> Looking for docs on how to add Single Sign-On support in your Supabase project? Head on over to [Single Sign-On with SAML 2.0 for Projects](https://supabase.com/docs/guides/auth/enterprise-sso/auth-sso-saml).

Supabase supports single sign-on (SSO) using Microsoft Azure AD.

## Step 1: Add and register an Enterprise application

Open up the [Azure Active Directory](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/Overview) dashboard for your Azure account.

Click the _Add_ button then _Enterprise application_.

## Step 2: Choose to create your own application

You'll be using the custom enterprise application setup for Supabase.

## Step 3: Fill in application details

In the modal titled _Create your own application_, enter a display name for Supabase. This is the name your Azure AD users see when signing in to Supabase from Azure. `Supabase` works in most cases.

Make sure to choose the third option: _Integrate any other application you don't find in the gallery (Non-gallery)_.

## Step 4: Set up single sign-on

Before you get to assigning users and groups, which would allow accounts in Azure AD to access Supabase, you need to configure the SAML details that allows Supabase to accept sign in requests from Azure AD.

## Step 5: Select SAML single sign-on method

Supabase only supports the SAML 2.0 protocol for Single Sign-On, which is an industry standard.

## Step 6: Upload SAML-based sign-on metadata file

First you need to download Supabase's SAML metadata file. Click the button below to initiate a download of the file.

[Download Supabase SAML Metadata File](https://alt.supabase.io/auth/v1/sso/saml/metadata?download=true)

Alternatively, visit this page to initiate a download: `https://alt.supabase.io/auth/v1/sso/saml/metadata?download=true`

Click on the _Upload metadata file_ option in the toolbar and select the file you just downloaded.

All of the correct information should automatically populate the _Basic SAML Configuration_ screen.

**Make sure you input these additional settings:**

| Setting | Value |
| --- | --- |
| Sign on URL | `https://supabase.com/dashboard/sign-in-sso` |
| Relay State | `https://supabase.com/dashboard` |

Finally, click the _Save_ button to save the configuration.

## Step 7: Obtain metadata URL and send to Supabase

Supabase needs to finalize enabling single sign-on with your Azure AD application. To do this, copy and send the link under **App Federation Metadata URL** in section 3 **SAML Certificates** to your support contact and await further instructions. If you're not clear who to send this link to or need further assistance, reach out to [Supabase Support](https://supabase.help/).

**Do not test the login until you have heard back from the support contact.**

## Step 8: Wait for confirmation

Wait for confirmation or further instructions from your support contact at Supabase before proceeding to the next step. It usually takes us 1 business day to configure SSO for you.

## Step 9: Test single sign-on

_Testing sign-on before your Azure AD has been registered with Supabase will not work. Make sure you've received confirmation from your support contact at Supabase as laid out in the [confirmation](#step-8-wait-for-confirmation) step._

Once you've received confirmation from your support contact at Supabase that SSO setup has been completed for your enterprise, you can ask some of your users to sign in via their Azure AD account.

You ask them to enter their email address on the [Sign in with SSO](https://supabase.com/dashboard/sign-in-sso) page.

If sign in is not working correctly, reach out to your support contact at Supabase for further guidance.
