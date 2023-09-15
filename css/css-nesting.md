---
date: 2023-09-14
---

# CSS Nesting

Today I learned that as of last month all modern browsers support [css nesting](https://developer.chrome.com/articles/css-nesting/)!

So instead of having to define styles like this:
``` css
.header {
  background-color: blue;
}

.header p {
  font-size: 16px;
}
.header p span:hover{
  color: green
} 
```

you can instead do:
```css
.header {
  background-color: blue;

  p {
    font-size: 16px;

    span {
      &:hover {
        color: green
      }
    }
  }
}
```

This was the last feature of Sass that I used regularly that was missing from native CSS ([CSS variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties) being the first big one that caused me to drop pulling sass into projects). 
