# 02. Creating Arrays

**Level:** Beginner

## Definition

Array creation functions build `ndarray` objects from Python sequences or from rules (ranges, constants, identity matrices, random numbers).

## Explanation

Use `np.array` to convert existing data. Use `zeros`, `ones`, `full`, `empty` for constant fills, `arange` (step-based) and `linspace` (count-based) for sequences, and `eye`/`identity` for identity matrices. `*_like` variants copy the shape of another array.

## Code

```python
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])
print("1D:", a)
print("2D:\n", b)

print("zeros:\n", np.zeros((2, 3)))
print("ones:\n", np.ones((2, 2), dtype=int))
print("full:\n", np.full((2, 2), 7))
print("arange:", np.arange(0, 10, 2))
print("linspace:", np.linspace(0, 1, 5))
print("eye:\n", np.eye(3))
print("zeros_like:\n", np.zeros_like(b))
```

## Output

```text
1D: [1 2 3]
2D:
 [[1 2 3]
 [4 5 6]]
zeros:
 [[0. 0. 0.]
 [0. 0. 0.]]
ones:
 [[1 1]
 [1 1]]
full:
 [[7 7]
 [7 7]]
arange: [0 2 4 6 8]
linspace: [0.   0.25 0.5  0.75 1.  ]
eye:
 [[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
zeros_like:
 [[0 0 0]
 [0 0 0]]
```

## Exercises

1. Create a 5x5 array filled with 9.
2. Create 11 evenly spaced numbers from 0 to 100.
3. Build a 4x4 identity matrix.
