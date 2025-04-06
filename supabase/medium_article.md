# A Supa-Introduction to Supabase

## Get ready for [SupaLaunchWeek 8](https://supabase.com/launch-week)

In my long professional SQL dabbler career, I've used numerous databases, methodologies, and software, yet none were to my liking.

A couple years ago I came across a **bold** statement, The Firebase of SQL Land, and I thought, Hmm, **why** would someone brag about anything Firebase-related?

Firebase ain't that great

Oh, was I wrong or were they wrong? But one thing is certain, [Supabase](https://supabase.com/) was cool; it had a decent CMS, JS library and provided direct access to the [Postgres DB](https://www.postgresql.org/) underneath.

Since I will mention Supabase countless times in this article, I decided to also use the following words to prevent utter boredom: *supa, base, radbase, the base, wowza*

# Supa-what?

After a rather uninviting introduction, let me explain in mundane terms **what *supa* is**:

> A solution for your database troubles, a Postgres wrapper hosted and scaled automagically (in [AWS](https://aws.amazon.com/blogs/opensource/supabase-makes-extensions-easier-for-developers-with-trusted-language-extensions-for-postgresql/)) and accessible through a clean web UI.

Everything that you could do with your custom Postgres Docker images deployed on unnecessarily complex infrastructure is at your fingertips without the hassle.

I'm not to bash on necessary custom maintained globally distributed orchestrated magical database systems (CMGDOMDS for short) but to encourage new projects in need of quick iteration to start less complex than last time.

[Architecture of Supabase services](https://www.workingsoftware.dev/tech-stack-and-architecture-of-supabase/)

## Flexibility

I have used the [Supabase client](https://supabase.com/docs/reference/javascript/introduction) in projects, mainly SPAs, although I'm not much of a fan since I find it hard to decouple in the unlikely case a migration from *the Base* is mandated.

Ah, an important aspect, *Base* is clearly not like [Firebase](https://fusionauth.io/blog/2022/05/25/how-to-migrate-from-firebase) as it has one major advantage. Migrations to other platforms are easy to manage since, in the end, it's all just Postgres, not some mumbo jumbo proprietary software owned by a non-evil corp.

You can quickly obtain an export of your database using the classic [pg\_dump and pg\_restore](https://www.postgresql.org/docs/8.0/backup.html) wherever you please, but really why migrate away from *Supa*?

## Authentication

The hot topic: is "password" a viable password or why .env being accidentaly pushed to a public repo means the entire git history needs to be deleted.

Even Michael uses a better password

Base makes it easy to get going via their OAuth integrations and [row-level security policies](https://supabase.com/docs/guides/auth/row-level-security), which are practically rules that dictate whether an authenticated user should have access to data. (This is available only when using the JS library or if you're passing the auth yourself.)

Don't forget to add an RLS policy after enabling it

With a click here, you've managed to not only lock bad actors out of your precious user data but also block everyone else since you must now manually create rules.

> I still forget to add read permissions when toggling RLS 2 years in so it's not something to be shy about, or is it?

## AI

All mighty AI, the hottest hot since NFTs were a thing, does Supabase allow it too? Well, let's set some expectations. This is neither an AI API nor a place to train your models, but it does excel in one thing.

Storage, :D, it's a database after all, [pgvector](https://supabase.com/docs/guides/database/extensions/pgvector) a native Postgres extension/plugin comes to the rescue. Without getting knee deep in AI theory, a model may require [embeddings](https://platform.openai.com/docs/guides/embeddings) to form a sort of memory around a particular topic, and pgvector allows that.

## Object storage

Since we are talking about storage, our favorite base offers an [object storage service](https://supabase.com/docs/guides/storage) built on top of S3 but with actual decent DX and sweet features like [image resizing and resumable uploads](https://supabase.com/blog/supabase-storage).

# My Supa-way

My method of using databases is uncanny, to say the least, I'm not big on client libraries built for specific databases, and I find being able to keep code intact when migrating to a different data source important.

I also had a fair share of difficulty maintaining types in sync with the DB until I found [Prisma](https://www.prisma.io/), which ensures consistency between any classic DB and ORM.

Therefore, I had to integrate *Wowza* in a slightly different manner than most, by using the [connection URI to link schema.prisma](https://supabase.com/partners/integrations/prisma) to the Postgres database directly.

Grab it while it's hot

This means I'm **giving away** RLS, object storage, and other benefits of the JS library, but I'm also gaining one priceless benefit: theoretical future insurance in case of migration mandation, basically gabble gabble.

I use all the Prisma syntax I want to query, mutate and even migrate new changes to the database while I can at any point preview the data using Supabase UI as if it were an admin CMS.

[Week 6](https://supabase.com/blog/supabase-beta-november-2022) was wild

On my most recent side-project I've switched back to the client library and discovered a neat feature, type generation to get much needed type support to various table queries.

It's important to note there are [2 ways to use the Supabase client](https://supabase.com/docs/guides/api/api-keys), server-side and client-side, although it's the same syntax I consider separate since I tend to use them for distinct needs.

The client side client lib (tongue twister) will expose credentials to the browser (network tab for ex.) allowing a bad actor access to data provided he knows what to seek. (this can **easily be prevented** via RLS)

You can use the same key for the server side although I take a different approach, if you want to bypass RLS you can use a service role key, a sort of admin mode which makes the client ignore RLS policies altogether.

> For obvious security reasons this should be done only on the server and with caution since gaining access to this token can lead to **doom**.

# Build in a **weekend**, **scale to millions**

The idea for this article took shape at midnight while I was having trouble sleeping, I can't stop thinking at the most inopportune times; what if I celebrate [**SupaLaunchWeek 8**](https://supabase.com/launch-week) by publishing an article covering my endeavors?

I've built many apps on *Radbase* and integrated it in many ways, in Next.JS, create-react-app, create-vite-app, heck even in a [Figma plugin](https://www.figma.com/community/plugin/1172891596048319817/Summon.AI) and I appreciate the awesome work the team put in.

Now I'm amidst developing [WITAS (wait, is that a sticker?)](https://witas.vercel.app/) and hope to submit it to the [Supabase Hackathon](https://supabase.com/blog/supabase-lw8-hackathon) by the end of the week, an AI-powered sticker generator and optimizer, all built on top of my favorite database.

A birds view of the systems architecture can be better visualized through the diagram below.

Witas Systems Diagram

The project is open-source on [GitHub](https://github.com/alex-streza/witas) and deployed on [Vercel](https://witas.vercel.app/), I'm considering adding something for analytics but no GA4.

While I'm using core Supa features like Database & Storage, I'm looking into adding more advanced workflows with the Edge Functions and a potential embeddings integration via pgvector before the challenge is over.

If you want to join the [hackathon](https://supabase.com/blog/supabase-lw8-hackathon) there's still plenty of time to build amazing stuff, win awesome prizes and maybe even bootstrap something for that domain name you bought so long ago.

Do you have any questions or suggestions? Feel free to **reach out**! 🚀. If you want to stay updated on my future writings follow me on [Medium](https://medium.com/@alex.streza) or [Twitter](https://twitter.com/alex_streza).

> ***P.S.:*** *No AI was used in writing this article, although I can't say the same about* [*WITAS*](https://witas.vercel.app/)
