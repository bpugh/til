---
date: 2023-09-15
---

# Disabling browser autofill in a form

Today I learned that `autocomplete="off"` tends to be completely ignored by browsers these days because they seem to have the attitude that websites don't use it correctly.

Apparently the best way to prevent a browser from trying to autofill a field is to tell the browser it's not the field it thinks it is with something like `autocomplete="something-else"`.
If it's anything the browser doesn't recognize it won't try to fill it.
It looks like `autocomplete="new-password"` is one people tend to use especially for any `type="password"` fields that aren't actually meant to be a user's login password.
See this [StackOverflow question](https://stackoverflow.com/questions/15738259/disabling-chrome-autofill) for more discussion.

Likewise if you want to give the browser hints about what it should​​​​​​​ try to suggest you can use one of the [recognized values](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete#values) like `address-line1`.
