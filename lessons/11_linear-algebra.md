# 11. Linear Algebra

**Level:** Intermediate

## Definition

`numpy.linalg` provides matrix products, inverses, determinants, eigen decomposition, SVD and linear system solvers.

## Explanation

Use `@` or `np.matmul` for matrix multiplication (not `*`, which is element-wise). `np.linalg.solve(A, b)` is preferred over computing the inverse explicitly. Eigenvalues/vectors come from `eig`, and singular value decomposition from `svd`.

## Code

```python
A = np.array([[2.0, 1.0], [1.0, 3.0]])
B = np.array([[1.0, 0.0], [4.0, 2.0]])

print("A @ B:\n", A @ B)
print("A * B (elementwise):\n", A * B)
print("transpose:\n", A.T)
print("det :", np.linalg.det(A).round(3))
print("inv:\n", np.linalg.inv(A).round(3))
print("trace:", np.trace(A))
print("rank :", np.linalg.matrix_rank(A))

# Solve: 2x + y = 5 ; x + 3y = 10
b = np.array([5.0, 10.0])
print("solution:", np.linalg.solve(A, b))

vals, vecs = np.linalg.eig(A)
print("eigenvalues:", vals.round(3))
print("norm:", np.linalg.norm(np.array([3, 4])))
U, S, Vt = np.linalg.svd(A)
print("singular values:", S.round(3))
```

## Output

```text
A @ B:
 [[ 6.  2.]
 [13.  6.]]
A * B (elementwise):
 [[2. 0.]
 [4. 6.]]
transpose:
 [[2. 1.]
 [1. 3.]]
det : 5.0
inv:
 [[ 0.6 -0.2]
 [-0.2  0.4]]
trace: 5.0
rank : 2
solution: [1. 3.]
eigenvalues: [1.382+0.j 3.618+0.j]
norm: 5.0
singular values: [3.618 1.382]
```

## Exercises

1. Solve a 3-variable linear system with `solve`.
2. Verify that `A @ inv(A)` is close to the identity using `np.allclose`.
