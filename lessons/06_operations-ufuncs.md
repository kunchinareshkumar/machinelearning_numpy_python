# 06. Arithmetic Operations and Universal Functions

**Level:** Beginner

## Definition

A universal function (ufunc) is a vectorized function that operates element-wise on arrays, implemented in C.

## Explanation

Operators `+ - * / // % **` work element-wise. Math ufuncs include `sqrt`, `exp`, `log`, `sin`, `abs`, `round`, `floor`, `ceil`. Comparison operators return boolean arrays. `out=` writes results into an existing array to avoid allocating memory.

## Code

```python
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
print("a + b :", a + b)
print("a * b :", a * b)
print("b / a :", b / a)
print("a ** 2:", a ** 2)
print("sqrt  :", np.sqrt(a))
print("exp   :", np.exp(a).round(2))
print("log   :", np.log(a).round(3))
print("a > 2 :", a > 2)
print("round :", np.round(np.array([1.234, 5.678]), 1))
print("dot   :", np.dot(a, b))
```

## Output

```text
a + b : [11 22 33 44]
a * b : [ 10  40  90 160]
b / a : [10. 10. 10. 10.]
a ** 2: [ 1  4  9 16]
sqrt  : [1.         1.41421356 1.73205081 2.        ]
exp   : [ 2.72  7.39 20.09 54.6 ]
log   : [0.    0.693 1.099 1.386]
a > 2 : [False False  True  True]
round : [1.2 5.7]
dot   : 300
```

## Exercises

1. Convert a temperature array from Celsius to Fahrenheit using one expression.
2. Compute the Euclidean distance between two 2D points stored as arrays.
