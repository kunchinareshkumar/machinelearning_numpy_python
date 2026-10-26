# 10. Sorting, Searching, and Set Operations

**Level:** Intermediate

## Definition

Functions that order elements (`sort`, `argsort`), find values (`argmax`, `searchsorted`) and compute unique values or set relations (`unique`, `intersect1d`, `union1d`, `isin`).

## Explanation

`np.sort` returns a sorted copy while `a.sort()` sorts in place. `argsort` returns the indices that would sort the array, ideal for ordering one array by another. `unique(return_counts=True)` counts occurrences. `searchsorted` does binary search on sorted data.

## Code

```python
a = np.array([40, 10, 30, 20, 10, 40])
print("sort     :", np.sort(a))
print("descend  :", np.sort(a)[::-1])
print("argsort  :", np.argsort(a))

names = np.array(["Ann", "Bob", "Cy", "Di", "Ed", "Flo"])
print("names by score:", names[np.argsort(a)])

vals, counts = np.unique(a, return_counts=True)
print("unique   :", vals, counts)
print("intersect:", np.intersect1d([1, 2, 3, 4], [3, 4, 5]))
print("union    :", np.union1d([1, 2], [2, 3]))
print("isin     :", np.isin(a, [10, 40]))
print("searchsorted:", np.searchsorted([10, 20, 30, 40], 25))

m = np.array([[3, 1], [2, 9], [1, 5]])
print("sort 2D by col0:\n", m[m[:, 0].argsort()])
```

## Output

```text
sort     : [10 10 20 30 40 40]
descend  : [40 40 30 20 10 10]
argsort  : [1 4 3 2 0 5]
names by score: ['Bob' 'Ed' 'Di' 'Cy' 'Ann' 'Flo']
unique   : [10 20 30 40] [2 1 1 2]
intersect: [3 4]
union    : [1 2 3]
isin     : [ True  True False False  True  True]
searchsorted: 2
sort 2D by col0:
 [[1 5]
 [2 9]
 [3 1]]
```

## Exercises

1. Return the top 3 largest values of an array.
2. Find the elements present in one array but not in another (`setdiff1d`).
