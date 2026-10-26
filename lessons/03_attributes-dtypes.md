# 03. Array Attributes and Data Types

**Level:** Beginner

## Definition

Attributes (`shape`, `ndim`, `size`, `dtype`, `itemsize`, `nbytes`) describe an array. A `dtype` is the data type of its elements.

## Explanation

`shape` is a tuple of dimension lengths, `ndim` the number of axes, `size` the total element count. Choosing a smaller dtype (for example `int8` or `float32`) saves memory. Convert with `astype`, which returns a new array.

## Code

```python
m = np.array([[1, 2, 3], [4, 5, 6]])
print("shape   :", m.shape)
print("ndim    :", m.ndim)
print("size    :", m.size)
print("dtype   :", m.dtype)
print("itemsize:", m.itemsize, "bytes")
print("nbytes  :", m.nbytes, "bytes")

f = m.astype(np.float32)
print("float32 :", f.dtype, f.nbytes, "bytes")

small = np.array([127], dtype=np.int8)      # int8 range is -128..127
print("int8 wraps around on overflow:", small + np.int8(1))
```

## Output

```text
shape   : (2, 3)
ndim    : 2
size    : 6
dtype   : int64
itemsize: 8 bytes
nbytes  : 48 bytes
float32 : float32 24 bytes
int8 wraps around on overflow: [-128]
```

## Exercises

1. Create an array of 1000 int64 values and compare `nbytes` after converting to int16.
2. What dtype does `np.array([1, 2.0, True])` get?
