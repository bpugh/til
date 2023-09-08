---
date: 2023-09-07
---

# CSS accent-color property

Today I learned that browsers now support an [accent-color](https://developer.mozilla.org/en-US/docs/Web/CSS/accent-color) property on some form inputs for customizing their color.
This is especially nice for checkboxes and radio buttons because now I no longer need any workarounds I've used in the past to make a decent-looking checkbox.
It will also ensure that it's accessible by automatically adjusting the color of the check to an appropriate contrast:

```html
<input type="checkbox" class="yellow" checked />
<input type="checkbox" class="purple" checked />

<style>
input {
  display: block;
  width: 30px;
  height: 30px;
}

input.purple {
  accent-color: rebeccapurple;
}

input.yellow {
  accent-color: yellow;
}
</style>
```

![checkboxes-screenshot](accent-color.png)
