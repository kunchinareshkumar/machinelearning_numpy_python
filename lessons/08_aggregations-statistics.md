# 08. Aggregations and Statistics

**Level:** Intermediate

## Definition

Aggregation functions reduce an array to a smaller one (sum, mean, std, min, max). The `axis` argument selects which dimension is collapsed.

## Explanation

`axis=0` collapses rows (gives one value per column); `axis=1` collapses columns (one value per row). `keepdims=True` keeps the reduced axis as size 1 which helps broadcasting. Also see `cumsum`, `cumprod`, `argmin`, `argmax`, `percentile`, `median`, `var`, `corrcoef`.

## Code

```python
data = np.array([[85, 90, 78], [92, 88, 95], [70, 65, 80], [88, 92, 85]])
print("sum all    :", data.sum())
print("mean/col   :", data.mean(axis=0))
print("mean/row   :", data.mean(axis=1))
print("max/col    :", data.max(axis=0))
print("argmax/col :", data.argmax(axis=0))
print("std        :", data.std().round(3))
print("median     :", np.median(data))
print("75th pctl  :", np.percentile(data, 75))
print("cumsum row0:", data[0].cumsum())
print("keepdims   :", data.mean(axis=1, keepdims=True).shape)
print("corr:\n", np.corrcoef(data[:, 0], data[:, 1]).round(3))
```

## Output

```text
sum all    : 1008
mean/col   : [83.75 83.75 84.5 ]
mean/row   : [84.33333333 91.66666667 71.66666667 88.33333333]
max/col    : [92 92 95]
argmax/col : [1 3 1]
std        : 8.794
median     : 86.5
75th pctl  : 90.5
cumsum row0: [ 85 175 253]
keepdims   : (4, 1)
corr:
 [[1.    0.924]
 [0.924 1.   ]]
```

## Exercises

1. Find the student (row) with the highest total score.
2. Normalize each column to zero mean and unit standard deviation.
