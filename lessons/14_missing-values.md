# 14. Missing Values: NaN and Inf

**Level:** Intermediate

## Definition

`np.nan` represents 'not a number' (missing or undefined float data) and `np.inf` infinity. NaN is contagious: any arithmetic with it yields NaN.

## Explanation

NaN never equals itself, so test with `np.isnan`. Standard aggregations return NaN if any value is NaN; use the `nan*` versions (`nansum`, `nanmean`, `nanmax`, ...). Use `np.nan_to_num` to replace NaN/inf and `np.isfinite` to check.

## Code

```python
a = np.array([1.0, 2.0, np.nan, 4.0, np.inf])
print("nan == nan:", np.nan == np.nan)
print("isnan    :", np.isnan(a))
print("isfinite :", np.isfinite(a))

b = np.array([1.0, 2.0, np.nan, 4.0])
print("sum  :", b.sum())
print("nansum:", np.nansum(b))
print("nanmean:", np.nanmean(b))

b[np.isnan(b)] = np.nanmean(b)       # simple imputation
print("imputed:", b.round(2))
print("nan_to_num:", np.nan_to_num(a, nan=0.0, posinf=999.0))
```

## Output

```text
nan == nan: False
isnan    : [False False  True False False]
isfinite : [ True  True False  True False]
sum  : nan
nansum: 7.0
nanmean: 2.3333333333333335
imputed: [1.   2.   2.33 4.  ]
nan_to_num: [  1.   2.   0.   4. 999.]
```

## Exercises

1. Fill NaN values in each column with that column's mean.
2. Count the NaN values in a 2D array.
