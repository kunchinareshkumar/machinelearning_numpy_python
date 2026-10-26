# 20. NumPy Cheat Sheet and Next Steps

**Level:** Reference

## Definition

A quick reference of the most-used NumPy functions grouped by task, plus ideas for what to learn next.

## Explanation

**Create:** `array, zeros, ones, full, arange, linspace, eye, random.default_rng`

**Inspect:** `shape, ndim, size, dtype, astype`

**Reshape:** `reshape, ravel, flatten, T, concatenate, vstack, hstack, stack, split, newaxis`

**Math:** `+ - * / ** @, sqrt, exp, log, abs, clip, round`

**Reduce:** `sum, mean, std, var, min, max, argmin, argmax, median, percentile, cumsum`  (always think `axis`)

**Select:** `a[i,j], slices, a[mask], a[[idx]], where, nonzero, take`

**Sort/Set:** `sort, argsort, unique, isin, intersect1d, union1d, setdiff1d, searchsorted`

**Linear algebra:** `dot, matmul, linalg.inv, solve, det, eig, svd, norm`

**I/O:** `save, load, savez, savetxt, loadtxt, genfromtxt`

**Next steps:** pandas (labeled tables), Matplotlib (plotting), SciPy (scientific algorithms), scikit-learn (machine learning), Numba (JIT speed), and practice on real datasets.

## Code

```python
cheat = {
    "create": ["array", "zeros", "ones", "arange", "linspace"],
    "reduce": ["sum", "mean", "std", "min", "max"],
    "select": ["where", "isin", "argsort", "unique"],
}
missing = [f for fs in cheat.values() for f in fs if not hasattr(np, f)]
print("All cheat-sheet functions exist in NumPy:", not missing)
print("Total public names in numpy:", len([n for n in dir(np) if not n.startswith("_")]))
help_example = np.sum.__doc__.splitlines()[0]
print("Tip - use help(np.func) or np.info(np.func). Example:", help_example)
```

## Output

```text
All cheat-sheet functions exist in NumPy: True
Total public names in numpy: 496
Tip - use help(np.func) or np.info(np.func). Example:
```

## Exercises

1. Pick any 10 functions above and write a one-line example for each.
2. Build your own mini project: analyze a CSV with NumPy only.
