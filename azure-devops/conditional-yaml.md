---
date: 2023-10-16
---

# Conditional logic in pipelines YAML

Today I learned that you can have conditional expressions in Azure Pipelines YAML files:

```yaml
steps:
- script: tool
  env:
    ${{ if parameters.debug }}:
      TOOL_DEBUG: true
      TOOL_DEBUG_DIR: _dbg
    ${{ else }}:
      TOOL_DEBUG: false
      TOOL_DEBUG_DIR: _dbg
```
