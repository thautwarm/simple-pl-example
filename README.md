## easylang

Running the code with no dependency but the Python standard library.

See `run.py` for more details.


```python
exp = parse("""
print(add(1, 2))
k = fun (x, y, z) =>
    {
        if gt(x,  y)
        then add(z, 1)
        else add(z, -1)
    }

print(k(1, 2, 3))
print(k(2, 1, 3))
""", "<unknown file>")

import operator
ctx = {'add': operator.add, 'print': print, 'gt': operator.gt}
exp(ctx)
# 3
# 2
# 4
``` 

## About the Parser

If you want to modify the parser and generate it again:
```
fff --trace easylang.gg
```

You need [frontend-for-free](https://github.com/thautwarm/frontend-for-free/) installed.