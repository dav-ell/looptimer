<img alt="looptimer" src="https://github.com/dav-ell/looptimer/blob/master/logo.png" width=364 height=82>

Quickly time your loops with a single line of code. Take code like this

```
for i in arr:
  # do something
```

and time it like this

```
for i in timing(arr):
  # do something
```

## Example

```
arr = range(10)
for i in timing(arr):
  time.sleep(1)
```

```
Iteration 0 took 1.0011s
Iteration 1 took 1.0011s
Iteration 2 took 1.0011s
Iteration 3 took 1.0008s
Iteration 4 took 1.0008s
Total runtime: 5.0068s
Average runtime per loop: 1.0010s
Shortest loop: 1.0008s
Longest loop: 1.0011s
```

Print every N iterations using the `every_n` parameter.

```
arr = range(5)
for i in timing(arr, every_n=2):
    time.sleep(1)
```

Print every N iterations using the `every_n` parameter.

```
arr = range(5)
for i in timing(arr, every_fraction=0.5):
    time.sleep(1)
```

## Credits

Logo courtesy of [Launchaco](https://www.launchaco.com/logo): [GitHub](https://github.com/launchaco/logo_builder)
