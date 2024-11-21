---
date: 2024-11-12
---

# SRI integrity hash algorithms

#til that you can actually specify different hash algorithms for [Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) (SRI) hashes.

If you aren't familiar with SRI, [this post](https://frontendmasters.com/blog/script-integrity/) does a good job explaining why it's useful and how it would have mitigated the recent [pollyfill.io incident](https://www.securityweek.com/polyfill-supply-chain-attack-hits-over-100k-websites/).

I needed to add the hashes to some scripts from a third party CDN that didn't provide them and I came across this handy [generator](https://www.srihash.org/) which let's you choose which algorithm to use and defaults to SHA-384 and [report-uri](https://report-uri.com/home/sri_hash) has a generator that just includes _all 3 different hashes_ in the `integrity` value.

So which one to use?

Apparently you can specify different hashes but there isn't much value in doing so at the moment since all modern browsers support all of the available algorithms so you should just pick **`SHA512`**.  
In the future however, newer algorithms might be implemented which you could add while maintaining backwards compatibility.

