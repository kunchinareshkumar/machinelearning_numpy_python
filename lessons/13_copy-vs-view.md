# 13. Copies vs Views

**Level:** Intermediate

## Definition

A view shares memory with the original array; a copy owns independent memory. Knowing which operation gives which prevents silent bugs.

## Explanation

Basic slicing, `reshape` (when possible), `ravel`, and `.T` return views. Boolean/fancy indexing, `flatten`, and `.copy()` return copies. Use `np.shares_memory` or the `.base` attribute to check. Call `.copy()` when you need independence.

## Code

```python
a = np.arange(6)
v = a[1:4]          # view
v[0] = 99
print("original changed by view:", a)

c = a[1:4].copy()   # copy
c[0] = -1
print("original after copy edit :", a)

fancy = a[[0, 1]]   # fancy index -> copy
fancy[0] = 1234
print("fancy edit leaves a alone:", a)

print("shares memory (view):", np.shares_memory(a, v))
print("shares memory (copy):", np.shares_memory(a, c))
print("view.base is a      :", v.base is a)
```

## Output

```text
original changed by view: [ 0 99  2  3  4  5]
original after copy edit : [ 0 99  2  3  4  5]
fancy edit leaves a alone: [ 0 99  2  3  4  5]
shares memory (view): True
shares memory (copy): False
view.base is a      : True
```

## Exercises

1. Predict whether `a.reshape(2,3)` modifies `a` when you edit it, then test.
2. Why does `b = a` not create a copy?
