---
date: 2023-11-03
---

# Use ChatGPT to help you write architectural decision records

I've been discovering recently that ChatGPT is actually pretty good at helping write [Architectural Decision Records (ADRs)](https://adr.github.io/).

Like most writing tasks, I'm finding ChatGPT is good at giving me a nice starting point instead of staring a blank template.

Even with as simple a prompt as "write an architectural decision record on why we chose to go with react instead of angular", it'll give a decent list of pros and cons on the topic in a common ADR template.
I can also refine it further by saying "write it using the following template instead..."

I really like ADRs for capturing **_why_** we made a particular decision and the important points we considered and which things might have been deal breakers - which ChatGPT obviously can't do for you but it's a quick way to list out some points and occasionally it'll even mention something I hadn't considered.

I also like asking it to argue the reverse like: "write an architectural decision record on why we chose to go with _angular instead of react_"

Interestingly, it will show the result in the UI as the rendered markdown but when you click the "copy" button it will copy the source markdown which is nice.