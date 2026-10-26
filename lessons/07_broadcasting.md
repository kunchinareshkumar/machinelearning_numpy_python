# 07. Broadcasting

**Level:** Intermediate

## Definition

Broadcasting is NumPy's rule set for performing operations on arrays of different shapes by virtually stretching the smaller array.

## Explanation

Shapes are compared from the trailing dimension backwards. Two dimensions are compatible if they are equal or one of them is 1. A size-1 dimension is stretched to match the other, without copying data. This removes the need for loops, for example subtracting a column mean from every row.

## Code

```python
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row = np.array([10, 20, 30])
col = np.array([[100], [200], [300]])

print("matrix + row:\n", m + row)       # (3,3) + (3,)
print("matrix + col:\n", m + col)       # (3,3) + (3,1)
print("outer sum:\n", np.arange(3)[:, None] + np.arange(3))   # (3,1)+(3,) -> (3,3)

# Center each column (subtract column means)
print("centered:\n", m - m.mean(axis=0))

try:
    np.ones((3, 2)) + np.ones((3,))
except ValueError as e:
    print("Incompatible shapes ->", e)
```

## Output

```text
matrix + row:
 [[11 22 33]
 [14 25 36]
 [17 28 39]]
matrix + col:
 [[101 102 103]
 [204 205 206]
 [307 308 309]]
outer sum:
 [[0 1 2]
 [1 2 3]
 [2 3 4]]
centered:
 [[-3. -3. -3.]
 [ 0.  0.  0.]
 [ 3.  3.  3.]]
Incompatible shapes -> operands could not be broadcast together with shapes (3,2) (3,)
```

## Exercises

1. Multiply each row of a 3x3 matrix by [1, 2, 3].
2. Build a 9x9 multiplication table without loops.
