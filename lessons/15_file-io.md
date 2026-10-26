# 15. Saving and Loading Data

**Level:** Intermediate

## Definition

NumPy reads and writes arrays in text formats (`savetxt`/`loadtxt`) and efficient binary formats (`save`/`load` for `.npy`, `savez` for `.npz`).

## Explanation

Binary `.npy` files preserve dtype and shape exactly and load fast. `savez_compressed` stores several arrays in one compressed archive. Text/CSV files are human readable but lose precision and metadata. For richer tabular data with headers, pandas is usually better.

## Code

```python
import os
os.makedirs("data", exist_ok=True)
arr = np.arange(12).reshape(3, 4)

np.save("data/sample.npy", arr)
print("npy  :", np.load("data/sample.npy").shape)

np.savez_compressed("data/bundle.npz", a=arr, b=arr * 2)
bundle = np.load("data/bundle.npz")
print("npz keys:", list(bundle.keys()), bundle["b"][0])

np.savetxt("data/sample.csv", arr, delimiter=",", fmt="%d")
print("csv  :\n", np.loadtxt("data/sample.csv", delimiter=",", dtype=int))
print("files:", sorted(os.listdir("data")))
```

## Output

```text
npy  : (3, 4)
npz keys: ['a', 'b'] [0 2 4 6]
csv  :
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
files: ['bundle.npz', 'sample.csv', 'sample.npy']
```

## Exercises

1. Save two arrays in one `.npz` and load only one.
2. Load a CSV that has a header row using `skiprows=1`.
