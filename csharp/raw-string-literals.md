---
date: 2024-11-18
---

# Raw string literals in C# 11

Today I learned about [raw string literals](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/raw-string) introduced in C# 11.

The big improvement to me is that you don't need to escape double quotes.

So no more of this noise if you need a json string:

```csharp
    string json = @"
{
  ""number"": 42,
  ""text"": ""Hello, world"",
  ""nested"": { ""flag"": true }
}";
```

You can now write:

```csharp
        string json = """
        {
          "number": 42,
          "text": "Hello, world",
          "nested": { "flag": true }
        }
        """;
```

The other nice feature is that an extraneous indentation will stripped out based on the location of the closing `"""`. 🔥

[This post](https://www.stevefenton.co.uk/blog/2022/02/raw-string-literals-in-c/) goes into it deeper.
