---
date: 2023-10-19
---

# Calling an extension method on a null instance

Today I learned that you can call an extension method on a null instance of the type.
I had always assumed without thinking about it too hard, that the reason `string.IsNullOrEmpty` isn't defined as an extension method in the framework is because you would get `NullReferenceException`.

But if we were to define an extension method like `public static bool IsNullOrEmpty(this string s)`, and call it like `if(s.IsNullOrEmpty())`
this is just syntactic sugar for `if(StringExtensions.IsNullOrEmpty(s))` and therefore it's safe to call on a null instance.

Apparently the argument against this is that it could be confusing or counterintuitive when looking at the code if you think it's an instance method.
I personally fall on the side of adding convenient extension methods like this - if nothing else to add a `NotNullOrEmpty` method.

To me I've always found it very easy to miss the `!` operator in a conditional and so avoiding those makes the condition much easier to read.

I much perfer:  
`if(userName.NotNullOrEmpty)`  
over  
`if(!string.IsNullOrEmpty(userName))`