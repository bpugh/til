---
date: 2024-01-24
---

# Disable entire form

Today I learned that you can disable an entire form by wrapping all the inputs in a `<fieldset disabled>`.

You might think that you can disable a form with `<form disabled`>` but unfortunately, the form element doesn't have a disabled attribute.

Fieldsets are typically used to group related form elements (and in some cases can improve accessibility) so you can have multiple in a form and disable portions of the form separately.

This is much more convenient than having to toggle the `disabled` attributes on every form element.

I also learned that there is a difference between styling a button with `button:disabled` and `button[disabled]`, the former being the one you want to use in this case since the latter only matches a button with a disabled attribute.

[Disabling an entire <form>](https://linkedlist.ch/disabling_an_entire_form_in_html_37/)
