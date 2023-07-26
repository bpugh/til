---
date: 2023-07-25
---

# A hidden button in an HTML form can be submitted

Even if a button is hidden with `display: none`, if it has a type of `submit` then it will still be activated if it's the first button in a form and a user hits enter in a form field.

So it's a good reason to always explicitly specify the type of a button since `submit` is the default but most of the time you want `type="button"`.

FYI there's an [eslint rule](https://github.com/jsx-eslint/eslint-plugin-react/blob/master/docs/rules/button-has-type.md) for this for react.
