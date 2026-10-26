# 09. Boolean Masking, Fancy Indexing and np.where

**Level:** Intermediate

## Definition

Boolean masking selects elements that satisfy a condition. Fancy indexing selects elements using arrays of integer indices. Both return copies.

## Explanation

A comparison creates a boolean array of the same shape; using it as an index keeps the `True` positions. Combine conditions with `&`, `|`, `~` (with parentheses). `np.where(cond, x, y)` chooses between two values element-wise; `np.where(cond)` returns indices.

## Code

```python
a = np.array([5, 12, 7, 20, 3, 18])
mask = a > 6
print("mask    :", mask)
print("filtered:", a[mask])
print("and/or  :", a[(a > 4) & (a < 15)])
print("not     :", a[~mask])

print("fancy   :", a[[0, 3, 5]])
print("where   :", np.where(a > 10, "big", "small"))
print("indices :", np.where(a > 10)[0])

b = a.copy()
b[b > 10] = 10        # clip using a mask
print("clipped :", b)
print("any/all :", (a > 10).any(), (a > 0).all())
print("count>6 :", np.count_nonzero(mask))
```

## Output

```text
mask    : [False  True  True  True False  True]
filtered: [12  7 20 18]
and/or  : [ 5 12  7]
not     : [5 3]
fancy   : [ 5 20 18]
where   : ['small' 'big' 'small' 'big' 'small' 'big']
indices : [1 3 5]
clipped : [ 5 10  7 10  3 10]
any/all : True True
count>6 : 4
```

## Exercises

1. Replace all negative numbers in an array with 0.
2. Select all even numbers greater than 10.
