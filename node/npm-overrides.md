---
date: 2023-11-06
---

# Override nested dependencies with npm

Today I learned that as of npm cli v8.3.0 (2021-12-09), you can use the [overrides field](https://docs.npmjs.com/cli/v9/configuring-npm/package-json#overrides) in `package.json` to "override" nested dependency versions.

This is handy for several scenarios, but for me I used for a third-party react component that has a `peerDependency` on v16 of react even though it works just fine with v18 but it isn't under active development at the moment so I had to override the version it accepts:

``` json
  "overrides": {
    "react-input-range": {
      "react-dom": "^18.2.0",
      "react": "^18.2.0"
    }
  },
```

Yarn has similar functionality that it calls [resolutions](https://classic.yarnpkg.com/lang/en/docs/selective-version-resolutions/).
