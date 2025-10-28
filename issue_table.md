# Static Code Analysis — Issue Documentation

| No | Issue Type | Tool | Line(s) | Description | Severity | Fix Approach | Status |
|----|-------------|------|----------|--------------|-----------|----------------|---------|
| 1 | Mutable default arg | Pylint | 8 | logs=[] shared across calls | Medium | Changed default to None and initialized inside function | ✅ Fixed |
| 2 | Bare except | Bandit / Flake8 | 19 | No exception type specified | High | Added KeyError, TypeError handling | ✅ Fixed |
| 3 | Insecure eval() | Bandit | 59 | Use of eval() | High | Removed eval() completely | ✅ Fixed |
| 4 | open() without encoding | Pylint | 26, 32 | File opened without encoding | Medium | Added `encoding="utf-8"` and used `with` statement | ✅ Fixed |
| 5 | Unused import | Flake8 | 2 | logging not used | Low | Removed `import logging` | ✅ Fixed |
| 6 | Naming style | Pylint | Multiple | Function names not in snake_case | Medium | Renamed to snake_case | ✅ Fixed |
| 7 | Missing docstrings | Pylint | Multiple | Missing documentation | Low | Added docstrings to all functions | ✅ Fixed |
| 8 | String formatting | Pylint | 12 | Used `%` formatting | Low | Changed to f-strings | ✅ Fixed |

**Total Issues Fixed:** 8  
**Pylint Score After Fix:** ~9.8/10  
