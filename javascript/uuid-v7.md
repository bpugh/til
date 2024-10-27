---
date: 2024-08-21
---

# UUID v7

Today I learned that there are 8 versions of UUID!

I was vaguely aware that there were some older versions that aren't recommended but just this past May the RFC was approved that added versions 6, 7, and 8.

Basically, v4 is a good default if you just need a good unguessable random ID. For javascript, this is now built into browsers via [`crypto.randomUUID()`](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/randomUUID) — or in dotnet with `Guid.NewGuid()`.

But [v7](https://uuid7.com/) is an exciting new option because it's time-based so the UUIDs are sortable based on when it was created and you can even [extract the timestamp](https://park.is/blog_posts/20240803_extracting_timestamp_from_uuid_v7/) if you want.
This also apparently makes it [better as a database key](https://itnext.io/why-uuid7-is-better-than-uuid4-as-clustered-index-edb02bf70056).

The [uuid](https://github.com/uuidjs/uuid) npm package just added support for v7 if you need it in javascript.
For C#, v7 support is [coming in dotnet 9](https://steven-giesel.com/blogPost/ea42a518-4d8b-4e08-8f73-e542bdd3b983).

This is a nice [overview of the different versions](https://www.ntietz.com/blog/til-uses-for-the-different-uuid-versions/) if you want to read more.

