# 05. Reshaping, Transposing, Joining and Splitting

**Level:** Beginner

## Definition

These functions change an array's shape or combine and divide arrays without changing the underlying values.

## Explanation

`reshape` needs the same total size (use `-1` to infer one dimension). `flatten` returns a copy, `ravel` a view when possible. `.T` transposes. `concatenate`, `vstack`, `hstack`, `stack` join arrays; `split`, `vsplit`, `hsplit` divide them. `np.newaxis` adds an axis.

## Code

```python
a = np.arange(12)
m = a.reshape(3, 4)
print("reshape(3,4):\n", m)
print("reshape(2,-1):", a.reshape(2, -1).shape)
print("transpose:\n", m.T)
print("flatten:", m.flatten())

x, y = np.array([1, 2, 3]), np.array([4, 5, 6])
print("vstack:\n", np.vstack([x, y]))
print("hstack:", np.hstack([x, y]))
print("stack axis=1:\n", np.stack([x, y], axis=1))
print("concatenate:", np.concatenate([x, y]))

print("split:", np.split(np.arange(9), 3))
print("add axis:", x[:, np.newaxis].shape)
```

## Output

```text
reshape(3,4):
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
reshape(2,-1): (2, 6)
transpose:
 [[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]
flatten: [ 0  1  2  3  4  5  6  7  8  9 10 11]
vstack:
 [[1 2 3]
 [4 5 6]]
hstack: [1 2 3 4 5 6]
stack axis=1:
 [[1 4]
 [2 5]
 [3 6]]
concatenate: [1 2 3 4 5 6]
split: [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]
add axis: (3, 1)
```

## Exercises

1. Turn a length-24 array into shape (2, 3, 4).
2. Split a 6x6 array into three 6x2 arrays.
