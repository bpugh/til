---
date: 2023-11-10
---

# Disabled buttons are bad for accessibility

Today I learned that disabled buttons are potentially bad for accessibility.

I realized long ago that disabled buttons can be bad for UX but I just saw Chris Ferdinandi's post [Don't Disable Buttons](https://gomakethings.com/dont-disable-buttons/), and learned that disabled buttons aren't focusable which means they don't work well with screen readers or navigating with the keyboard.

I usually recommend against disabling form submit buttons when there are validation errors because the user has no feedback as to _why_ it's disabled, but Chris gives the example of disabling while the form is being submitted (which I've probably done in the past) and he goes into detail about the issues with this approach and a good alternative.
