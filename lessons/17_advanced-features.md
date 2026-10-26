# 17. Advanced Features: vectorize, einsum, Structured and Masked Arrays

**Level:** Advanced

## Definition

A collection of power tools: `np.vectorize` (convenience wrapper), `np.einsum` (Einstein summation), structured arrays (records with named fields) and masked arrays (arrays with invalid entries hidden).

## Explanation

`np.vectorize` is syntactic sugar, not a speed-up. `np.einsum('ij,jk->ik', A, B)` expresses sums of products compactly (matrix multiply here). Structured arrays give column-like named fields with different dtypes. `np.ma` masks entries so they are ignored in calculations. `np.apply_along_axis` applies a function to 1D slices.

## Code

```python
def clamp_odd(x):
    return x * 2 if x % 2 else x

vf = np.vectorize(clamp_odd)
print("vectorize:", vf(np.arange(6)))

A = np.arange(6).reshape(2, 3)
B = np.arange(6).reshape(3, 2)
print("einsum matmul:\n", np.einsum("ij,jk->ik", A, B))
print("einsum trace :", np.einsum("ii", np.eye(3)))

people = np.array([("Ann", 25, 55.5), ("Bob", 31, 70.2)],
                  dtype=[("name", "U10"), ("age", "i4"), ("weight", "f4")])
print("structured ages:", people["age"], "mean weight:", people["weight"].mean())

data = np.ma.masked_array([1, 2, -999, 4], mask=[0, 0, 1, 0])
print("masked mean:", data.mean())

print("apply_along_axis:", np.apply_along_axis(np.ptp, 1, np.array([[1, 5, 3], [9, 2, 4]])))
```

## Output

```text
vectorize: [ 0  2  2  6  4 10]
einsum matmul:
 [[10 13]
 [28 40]]
einsum trace : 3.0
structured ages: [25 31] mean weight: 62.85
masked mean: 2.3333333333333335
apply_along_axis: [4 7]
```

## Exercises

1. Use `einsum` to compute the batch dot product of two (5, 3) arrays.
2. Create a structured array of products with name, price and stock fields.
