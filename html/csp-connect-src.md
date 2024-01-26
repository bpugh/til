---
date: 2024-01-26
---

# CSP `connect-src` directive

Today I learned that there is a Content-Security-Policy (CSP) directive `connect-src` that you can use to restrict all outgoing requests from your website to only the domains that you specify.

This a powerful mitigation against any kind of script injection attacks since no data can then be exfiltrated from your page.

It applies to `XMLHttpRequest` (AJAX), `WebSocket`, `fetch()`, `<a ping>` or `EventSource`.

CSP is an HTTP response header for enhancing the security of a site and there are of course several other directives you might want to enable.

[This is a handy reference](https://content-security-policy.com/)

If you want to see a real-world comprehensive example, take a look at the [CSP header for haveibeenpwned.com](https://report-uri.com/home/analyse/https%3A%2F%2Fhaveibeenpwned.com%2F).