# 01. Introduction to NumPy

**Level:** Beginner

## Definition

NumPy (Numerical Python) is the foundational Python library for fast numerical computing. Its core object is the `ndarray`, a fixed-type, N-dimensional array stored in contiguous memory.

## Explanation

Python lists can hold mixed types and are flexible, but they are slow for math because every element is a separate Python object. A NumPy array stores one data type in one block of memory, so operations run in compiled C code. Almost the whole scientific Python stack (pandas, SciPy, scikit-learn, Matplotlib) is built on NumPy arrays.

Install with `pip install numpy` and import by convention as `np`.

## Code

```python
import numpy as np

print("NumPy version:", np.__version__)

py_list = [1, 2, 3, 4, 5]
arr = np.array([1, 2, 3, 4, 5])

print(type(py_list), type(arr))
print("list * 2 :", py_list * 2)      # repeats the list
print("array * 2:", arr * 2)          # element-wise math
```

## Output

```text
NumPy version: 2.5.3
<class 'list'> <class 'numpy.ndarray'>
list * 2 : [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
array * 2: [ 2  4  6  8 10]
```

## Exercises

1. Create a list and an array of 1..10 and square every element of both (the list needs a loop).
2. Print the type of `np.array([1, 2.5])`'s elements.
