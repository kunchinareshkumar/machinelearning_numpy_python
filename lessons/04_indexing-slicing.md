# 04. Indexing and Slicing

**Level:** Beginner

## Definition

Indexing selects single elements; slicing (`start:stop:step`) selects ranges along each axis. Slices of NumPy arrays are views, not copies.

## Explanation

For 2D arrays use `a[row, col]`. A colon means 'all along this axis'. Negative indices count from the end. Because slices are views, modifying a slice changes the original array (see the Copies vs Views lesson).

## Code

```python
a = np.arange(1, 13).reshape(3, 4)
print(a)
print("a[0, 0]   :", a[0, 0])
print("a[-1, -1] :", a[-1, -1])
print("row 1     :", a[1])
print("col 2     :", a[:, 2])
print("sub-block :\n", a[0:2, 1:3])
print("every other col:", a[:, ::2])
print("reversed rows:\n", a[::-1])
```

## Output

```text
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
a[0, 0]   : 1
a[-1, -1] : 12
row 1     : [5 6 7 8]
col 2     : [ 3  7 11]
sub-block :
 [[2 3]
 [6 7]]
every other col: [[ 1  3]
 [ 5  7]
 [ 9 11]]
reversed rows:
 [[ 9 10 11 12]
 [ 5  6  7  8]
 [ 1  2  3  4]]
```

## Exercises

1. Extract the second and third column of a 3x4 array.
2. Select the outer border elements of a 5x5 array.
