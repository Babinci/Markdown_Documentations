# Your Monthly Invoice

## Billing Cycle

When you sign up for a paid plan you get charged once a month at the beginning of the billing cycle. A billing cycle starts with the creation of a Supabase organization. If you create an organization on the sixth of January your billing cycle resets on the sixth of each month. If the anchored day is not present in the current month, then the last day of the month is used.

## Your Invoice Explained

When your billing cycle resets an invoice gets issued. That invoice contains line items from both the current and the previous billing cycle. Fixed fees for the current billing cycle, usage based fees for the previous billing cycle.

### Fixed Fees

Fixed fees are independent of usage and paid in-advance. Whether you have one or several projects, hundreds or millions of active users, the fee is always the same, and doesn't vary. Examples are the subscription fee, the fee for HIPAA and for priority support.

### Usage Based Fees

Fees vary depending on usage and are paid in arrears. The more usage you have, the higher the fee. Examples are fees for monthly active users and storage size.

### Discounted Line Items

Paid plans come with a usage quota for certain line items. You only pay for usage that goes beyond the quota. The quota for Storage for example is 100 GB. If you use 105 GB, you pay for 5 GB. If you use 95 GB, you pay nothing. This quota is declared as a discount on your invoice.

#### Compute Credits

Paid plans come with $10 in Compute Credits per month. This suffices for a single project using a Nano or Micro compute instance. Every additional project adds compute fees to your monthly invoice though.

### Example Invoice

The following invoice was issued on January 6, 2025 with the previous billing cycle from December 6, 2024 - January 5, 2025, and the current billing cycle from January 6 - February 5, 2025.

![Example Invoice](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fimg%2Fguides%2Fplatform%2Fexample-invoice.png&w=3840&q=75&dpl=dpl_9WgBm3X43HXGqPuPh4vSvQgRaZyZ)

1. The final amount due
2. Fixed subscription fee for the current billing cycle
3. Usage based fee for Compute for the previous billing cycle. There were two projects (`wsmmedyqtlrvbcesxdew`, `wwxdpovgtfcmcnxwsaad`) running 744 hours (24 hours * 31 days). These projects incurred $10 in Compute fees each. With $10 in Compute Credits deducted, the final Compute fees are $10.
4. Usage based fee for Custom Domain for the previous billing cycle. There is no free usage quota for Custom Domain. You get charged for the 744 hours (24 hours * 31 days) a Custom Domain was active. The final Custom Domain fees are $10.19.
5. Usage based fee for Egress for the previous billing cycle. There is a free usage quota of 250 GB for Egress. You get charged for usage beyond 250 GB only, meaning for 2,119.47 GB. The final Egress fees are $190.75.
6. Usage based fee for Monthly Active Users for the previous billing cycle. There is a free usage quota of 100,000 users. With 141 users there is no charge for this line item.

### Why Is My Invoice More Than $25?

The amount due of your invoice being higher than the $25 subscription fee for the Pro Plan can have several reasons.

- **Running several projects:** You had more than one project running in the previous billing cycle. Supabase provides a dedicated server and database for every project. That means that every project you launch incurs compute costs. While the $10 Compute Credits cover a single project using a Nano or Micro compute instance, every additional project adds at least $10 compute costs to your invoice.
- **Usage beyond quota:** You exceeded the included usage quota for one or more line items in the previous billing cycle while having the Spend Cap disabled.
- **Usage that is not covered by the Spend Cap:** You had usage in the previous billing cycle that is not covered by the [Spend Cap](https://supabase.com/docs/guides/platform/cost-control#spend-cap). For example using an IPv4 address or a custom domain.

## How to Settle Your Invoices

Monthly invoices are auto-collected by charging the payment method marked as "active" for an organization.

### Payment Failure

If your payment fails, Supabase retries the charge several times. We send you a Payment Failure email with the reason for the failure. Follow the steps outlined in this email. You can manually trigger a charge at any time via:

- The link in the Payment Failure email
- The "Pay Now" button on the [organization's invoices page](https://supabase.com/dashboard/org/_/invoices)

## Where to Find Your Invoices

Your invoice is sent to you via email. You can also find your invoices on the [organization's invoices page](https://supabase.com/dashboard/org/_/invoices).
