TOPICS = []


def add(slug, title, level, definition, explanation, code, exercises):
    TOPICS.append(dict(n=len(TOPICS) + 1, slug=slug, title=title, level=level,
                       definition=definition, explanation=explanation,
                       code=code, exercises=exercises))


add("introduction", "Introduction to NumPy", "Beginner",
    "NumPy (Numerical Python) is the foundational Python library for fast numerical computing. Its core object is the `ndarray`, a fixed-type, N-dimensional array stored in contiguous memory.",
    "Python lists can hold mixed types and are flexible, but they are slow for math because every element is a separate Python object. A NumPy array stores one data type in one block of memory, so operations run in compiled C code. Almost the whole scientific Python stack (pandas, SciPy, scikit-learn, Matplotlib) is built on NumPy arrays.\n\nInstall with `pip install numpy` and import by convention as `np`.",
    r'''import numpy as np

print("NumPy version:", np.__version__)

py_list = [1, 2, 3, 4, 5]
arr = np.array([1, 2, 3, 4, 5])

print(type(py_list), type(arr))
print("list * 2 :", py_list * 2)      # repeats the list
print("array * 2:", arr * 2)          # element-wise math''',
    ["Create a list and an array of 1..10 and square every element of both (the list needs a loop).",
     "Print the type of `np.array([1, 2.5])`'s elements."])

add("creating-arrays", "Creating Arrays", "Beginner",
    "Array creation functions build `ndarray` objects from Python sequences or from rules (ranges, constants, identity matrices, random numbers).",
    "Use `np.array` to convert existing data. Use `zeros`, `ones`, `full`, `empty` for constant fills, `arange` (step-based) and `linspace` (count-based) for sequences, and `eye`/`identity` for identity matrices. `*_like` variants copy the shape of another array.",
    r'''a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])
print("1D:", a)
print("2D:\n", b)

print("zeros:\n", np.zeros((2, 3)))
print("ones:\n", np.ones((2, 2), dtype=int))
print("full:\n", np.full((2, 2), 7))
print("arange:", np.arange(0, 10, 2))
print("linspace:", np.linspace(0, 1, 5))
print("eye:\n", np.eye(3))
print("zeros_like:\n", np.zeros_like(b))''',
    ["Create a 5x5 array filled with 9.", "Create 11 evenly spaced numbers from 0 to 100.",
     "Build a 4x4 identity matrix."])

add("attributes-dtypes", "Array Attributes and Data Types", "Beginner",
    "Attributes (`shape`, `ndim`, `size`, `dtype`, `itemsize`, `nbytes`) describe an array. A `dtype` is the data type of its elements.",
    "`shape` is a tuple of dimension lengths, `ndim` the number of axes, `size` the total element count. Choosing a smaller dtype (for example `int8` or `float32`) saves memory. Convert with `astype`, which returns a new array.",
    r'''m = np.array([[1, 2, 3], [4, 5, 6]])
print("shape   :", m.shape)
print("ndim    :", m.ndim)
print("size    :", m.size)
print("dtype   :", m.dtype)
print("itemsize:", m.itemsize, "bytes")
print("nbytes  :", m.nbytes, "bytes")

f = m.astype(np.float32)
print("float32 :", f.dtype, f.nbytes, "bytes")

small = np.array([127], dtype=np.int8)      # int8 range is -128..127
print("int8 wraps around on overflow:", small + np.int8(1))''',
    ["Create an array of 1000 int64 values and compare `nbytes` after converting to int16.",
     "What dtype does `np.array([1, 2.0, True])` get?"])

add("indexing-slicing", "Indexing and Slicing", "Beginner",
    "Indexing selects single elements; slicing (`start:stop:step`) selects ranges along each axis. Slices of NumPy arrays are views, not copies.",
    "For 2D arrays use `a[row, col]`. A colon means 'all along this axis'. Negative indices count from the end. Because slices are views, modifying a slice changes the original array (see the Copies vs Views lesson).",
    r'''a = np.arange(1, 13).reshape(3, 4)
print(a)
print("a[0, 0]   :", a[0, 0])
print("a[-1, -1] :", a[-1, -1])
print("row 1     :", a[1])
print("col 2     :", a[:, 2])
print("sub-block :\n", a[0:2, 1:3])
print("every other col:", a[:, ::2])
print("reversed rows:\n", a[::-1])''',
    ["Extract the second and third column of a 3x4 array.", "Select the outer border elements of a 5x5 array."])

add("reshaping-joining", "Reshaping, Transposing, Joining and Splitting", "Beginner",
    "These functions change an array's shape or combine and divide arrays without changing the underlying values.",
    "`reshape` needs the same total size (use `-1` to infer one dimension). `flatten` returns a copy, `ravel` a view when possible. `.T` transposes. `concatenate`, `vstack`, `hstack`, `stack` join arrays; `split`, `vsplit`, `hsplit` divide them. `np.newaxis` adds an axis.",
    r'''a = np.arange(12)
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
print("add axis:", x[:, np.newaxis].shape)''',
    ["Turn a length-24 array into shape (2, 3, 4).", "Split a 6x6 array into three 6x2 arrays."])

add("operations-ufuncs", "Arithmetic Operations and Universal Functions", "Beginner",
    "A universal function (ufunc) is a vectorized function that operates element-wise on arrays, implemented in C.",
    "Operators `+ - * / // % **` work element-wise. Math ufuncs include `sqrt`, `exp`, `log`, `sin`, `abs`, `round`, `floor`, `ceil`. Comparison operators return boolean arrays. `out=` writes results into an existing array to avoid allocating memory.",
    r'''a = np.array([1, 2, 3, 4])
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
print("dot   :", np.dot(a, b))''',
    ["Convert a temperature array from Celsius to Fahrenheit using one expression.", "Compute the Euclidean distance between two 2D points stored as arrays."])

add("broadcasting", "Broadcasting", "Intermediate",
    "Broadcasting is NumPy's rule set for performing operations on arrays of different shapes by virtually stretching the smaller array.",
    "Shapes are compared from the trailing dimension backwards. Two dimensions are compatible if they are equal or one of them is 1. A size-1 dimension is stretched to match the other, without copying data. This removes the need for loops, for example subtracting a column mean from every row.",
    r'''m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row = np.array([10, 20, 30])
col = np.array([[100], [200], [300]])

print("matrix + row:\n", m + row)       # (3,3) + (3,)
print("matrix + col:\n", m + col)       # (3,3) + (3,1)
print("outer sum:\n", np.arange(3)[:, None] + np.arange(3))   # (3,1)+(3,) -> (3,3)

# Center each column (subtract column means)
print("centered:\n", m - m.mean(axis=0))

try:
    np.ones((3, 2)) + np.ones((3,))
except ValueError as e:
    print("Incompatible shapes ->", e)''',
    ["Multiply each row of a 3x3 matrix by [1, 2, 3].", "Build a 9x9 multiplication table without loops."])

add("aggregations-statistics", "Aggregations and Statistics", "Intermediate",
    "Aggregation functions reduce an array to a smaller one (sum, mean, std, min, max). The `axis` argument selects which dimension is collapsed.",
    "`axis=0` collapses rows (gives one value per column); `axis=1` collapses columns (one value per row). `keepdims=True` keeps the reduced axis as size 1 which helps broadcasting. Also see `cumsum`, `cumprod`, `argmin`, `argmax`, `percentile`, `median`, `var`, `corrcoef`.",
    r'''data = np.array([[85, 90, 78], [92, 88, 95], [70, 65, 80], [88, 92, 85]])
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
print("corr:\n", np.corrcoef(data[:, 0], data[:, 1]).round(3))''',
    ["Find the student (row) with the highest total score.", "Normalize each column to zero mean and unit standard deviation."])

add("boolean-fancy-indexing", "Boolean Masking, Fancy Indexing and np.where", "Intermediate",
    "Boolean masking selects elements that satisfy a condition. Fancy indexing selects elements using arrays of integer indices. Both return copies.",
    "A comparison creates a boolean array of the same shape; using it as an index keeps the `True` positions. Combine conditions with `&`, `|`, `~` (with parentheses). `np.where(cond, x, y)` chooses between two values element-wise; `np.where(cond)` returns indices.",
    r'''a = np.array([5, 12, 7, 20, 3, 18])
mask = a > 6
print("mask    :", mask)
print("filtered:", a[mask])
print("and/or  :", a[(a > 4) & (a < 15)])
print("not     :", a[~mask])

print("fancy   :", a[[0, 3, 5]])
print("where   :", np.where(a > 10, "big", "small"))
print("indices :", np.where(a > 10)[0])

b = a.copy()
b[b > 10] = 10        # clip using a mask
print("clipped :", b)
print("any/all :", (a > 10).any(), (a > 0).all())
print("count>6 :", np.count_nonzero(mask))''',
    ["Replace all negative numbers in an array with 0.", "Select all even numbers greater than 10."])

add("sorting-searching", "Sorting, Searching, and Set Operations", "Intermediate",
    "Functions that order elements (`sort`, `argsort`), find values (`argmax`, `searchsorted`) and compute unique values or set relations (`unique`, `intersect1d`, `union1d`, `isin`).",
    "`np.sort` returns a sorted copy while `a.sort()` sorts in place. `argsort` returns the indices that would sort the array, ideal for ordering one array by another. `unique(return_counts=True)` counts occurrences. `searchsorted` does binary search on sorted data.",
    r'''a = np.array([40, 10, 30, 20, 10, 40])
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
print("sort 2D by col0:\n", m[m[:, 0].argsort()])''',
    ["Return the top 3 largest values of an array.", "Find the elements present in one array but not in another (`setdiff1d`)."])

add("linear-algebra", "Linear Algebra", "Intermediate",
    "`numpy.linalg` provides matrix products, inverses, determinants, eigen decomposition, SVD and linear system solvers.",
    "Use `@` or `np.matmul` for matrix multiplication (not `*`, which is element-wise). `np.linalg.solve(A, b)` is preferred over computing the inverse explicitly. Eigenvalues/vectors come from `eig`, and singular value decomposition from `svd`.",
    r'''A = np.array([[2.0, 1.0], [1.0, 3.0]])
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
print("singular values:", S.round(3))''',
    ["Solve a 3-variable linear system with `solve`.", "Verify that `A @ inv(A)` is close to the identity using `np.allclose`."])

add("random", "Random Number Generation", "Intermediate",
    "NumPy's random module generates pseudo-random numbers from many distributions. The modern API uses a `Generator` created by `np.random.default_rng(seed)`.",
    "Using a fixed seed makes results reproducible. The generator offers `random`, `integers`, `normal`, `uniform`, `choice`, `shuffle`, `permutation`, `binomial`, `poisson`, and more. Prefer `default_rng` over the legacy `np.random.seed` / `np.random.rand` functions.",
    r'''rng = np.random.default_rng(42)

print("uniform [0,1):", rng.random(3).round(3))
print("integers     :", rng.integers(1, 7, size=5))
print("normal       :", rng.normal(loc=50, scale=10, size=3).round(2))
print("choice       :", rng.choice(["red", "green", "blue"], size=4))
print("permutation  :", rng.permutation(5))

deck = np.arange(10)
rng.shuffle(deck)
print("shuffled     :", deck)

rolls = rng.integers(1, 7, size=10_000)
print("mean of 10k dice rolls:", rolls.mean().round(3))
sample = rng.normal(0, 1, 100_000)
print("sample mean/std:", sample.mean().round(3), sample.std().round(3))''',
    ["Simulate 1000 coin flips and count heads.", "Draw 5 random samples without replacement from 1..20."])

add("copy-vs-view", "Copies vs Views", "Intermediate",
    "A view shares memory with the original array; a copy owns independent memory. Knowing which operation gives which prevents silent bugs.",
    "Basic slicing, `reshape` (when possible), `ravel`, and `.T` return views. Boolean/fancy indexing, `flatten`, and `.copy()` return copies. Use `np.shares_memory` or the `.base` attribute to check. Call `.copy()` when you need independence.",
    r'''a = np.arange(6)
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
print("view.base is a      :", v.base is a)''',
    ["Predict whether `a.reshape(2,3)` modifies `a` when you edit it, then test.", "Why does `b = a` not create a copy?"])

add("missing-values", "Missing Values: NaN and Inf", "Intermediate",
    "`np.nan` represents 'not a number' (missing or undefined float data) and `np.inf` infinity. NaN is contagious: any arithmetic with it yields NaN.",
    "NaN never equals itself, so test with `np.isnan`. Standard aggregations return NaN if any value is NaN; use the `nan*` versions (`nansum`, `nanmean`, `nanmax`, ...). Use `np.nan_to_num` to replace NaN/inf and `np.isfinite` to check.",
    r'''a = np.array([1.0, 2.0, np.nan, 4.0, np.inf])
print("nan == nan:", np.nan == np.nan)
print("isnan    :", np.isnan(a))
print("isfinite :", np.isfinite(a))

b = np.array([1.0, 2.0, np.nan, 4.0])
print("sum  :", b.sum())
print("nansum:", np.nansum(b))
print("nanmean:", np.nanmean(b))

b[np.isnan(b)] = np.nanmean(b)       # simple imputation
print("imputed:", b.round(2))
print("nan_to_num:", np.nan_to_num(a, nan=0.0, posinf=999.0))''',
    ["Fill NaN values in each column with that column's mean.", "Count the NaN values in a 2D array."])

add("file-io", "Saving and Loading Data", "Intermediate",
    "NumPy reads and writes arrays in text formats (`savetxt`/`loadtxt`) and efficient binary formats (`save`/`load` for `.npy`, `savez` for `.npz`).",
    "Binary `.npy` files preserve dtype and shape exactly and load fast. `savez_compressed` stores several arrays in one compressed archive. Text/CSV files are human readable but lose precision and metadata. For richer tabular data with headers, pandas is usually better.",
    r'''import os
os.makedirs("data", exist_ok=True)
arr = np.arange(12).reshape(3, 4)

np.save("data/sample.npy", arr)
print("npy  :", np.load("data/sample.npy").shape)

np.savez_compressed("data/bundle.npz", a=arr, b=arr * 2)
bundle = np.load("data/bundle.npz")
print("npz keys:", list(bundle.keys()), bundle["b"][0])

np.savetxt("data/sample.csv", arr, delimiter=",", fmt="%d")
print("csv  :\n", np.loadtxt("data/sample.csv", delimiter=",", dtype=int))
print("files:", sorted(os.listdir("data")))''',
    ["Save two arrays in one `.npz` and load only one.", "Load a CSV that has a header row using `skiprows=1`."])

add("performance", "Vectorization and Performance", "Advanced",
    "Vectorization replaces explicit Python loops with array expressions so the work happens in optimized C loops, often 10x to 100x faster.",
    "Avoid iterating over elements in Python. Use ufuncs, broadcasting, boolean masks and `np.where`. Memory layout matters too: C-contiguous arrays are fastest when traversed along the last axis. Use `%timeit` in notebooks or `time.perf_counter` in scripts to measure.",
    r'''import time

n = 1_000_000
x = np.arange(n)

t0 = time.perf_counter()
loop_total = 0
for v in x.tolist():
    loop_total += v * v
t_loop = time.perf_counter() - t0

t0 = time.perf_counter()
vec_total = (x * x).sum()
t_vec = time.perf_counter() - t0

print("same result:", loop_total == vec_total)
print(f"python loop: {t_loop*1000:.1f} ms")
print(f"numpy      : {t_vec*1000:.1f} ms")
print(f"speed-up   : about {t_loop / t_vec:.0f}x")

print("C-contiguous:", np.zeros((3, 3)).flags["C_CONTIGUOUS"])''',
    ["Time a loop vs vectorized computation of the sum of squares for 10 million numbers.", "Rewrite `[x if x > 0 else 0 for x in a]` with NumPy."])

add("advanced-features", "Advanced Features: vectorize, einsum, Structured and Masked Arrays", "Advanced",
    "A collection of power tools: `np.vectorize` (convenience wrapper), `np.einsum` (Einstein summation), structured arrays (records with named fields) and masked arrays (arrays with invalid entries hidden).",
    "`np.vectorize` is syntactic sugar, not a speed-up. `np.einsum('ij,jk->ik', A, B)` expresses sums of products compactly (matrix multiply here). Structured arrays give column-like named fields with different dtypes. `np.ma` masks entries so they are ignored in calculations. `np.apply_along_axis` applies a function to 1D slices.",
    r'''def clamp_odd(x):
    return x * 2 if x % 2 else x

vf = np.vectorize(clamp_odd)
print("vectorize:", vf(np.arange(6)))

A = np.arange(6).reshape(2, 3)
B = np.arange(6).reshape(3, 2)
print("einsum matmul:\n", np.einsum("ij,jk->ik", A, B))
print("einsum trace :", np.einsum("ii", np.eye(3)))

people = np.array([("Ann", 25, 55.5), ("Bob", 31, 70.2)],
                  dtype=[("name", "U10"), ("age", "i4"), ("weight", "f4")])
print("structured ages:", people["age"], "mean weight:", people["weight"].mean())

data = np.ma.masked_array([1, 2, -999, 4], mask=[0, 0, 1, 0])
print("masked mean:", data.mean())

print("apply_along_axis:", np.apply_along_axis(np.ptp, 1, np.array([[1, 5, 3], [9, 2, 4]])))''',
    ["Use `einsum` to compute the batch dot product of two (5, 3) arrays.", "Create a structured array of products with name, price and stock fields."])

add("project-student-grades", "Mini Project 1: Student Grade Analysis", "Project",
    "A practical exercise combining random data, aggregation, boolean masks, sorting and broadcasting.",
    "We simulate marks for 8 students in 4 subjects and answer typical analytics questions without a single loop.",
    r'''rng = np.random.default_rng(7)
students = np.array([f"S{i}" for i in range(1, 9)])
subjects = ["Math", "Physics", "Chem", "English"]
marks = rng.integers(40, 100, size=(8, 4))

print("marks:\n", marks)
totals = marks.sum(axis=1)
avg = marks.mean(axis=1)
rank = np.argsort(-totals)

print("\nTop 3:", list(zip(students[rank][:3].tolist(), totals[rank][:3].tolist())))
print("Subject averages:", dict(zip(subjects, marks.mean(axis=0).round(1).tolist())))
print("Hardest subject :", subjects[marks.mean(axis=0).argmin()])
print("Students failing any subject (<50):", students[(marks < 50).any(axis=1)])

z = (marks - marks.mean(axis=0)) / marks.std(axis=0)   # broadcasting
print("Best z-score student per subject:", students[z.argmax(axis=0)])

grades = np.select([avg >= 85, avg >= 70, avg >= 55], ["A", "B", "C"], default="D")
print("Grades:", dict(zip(students.tolist(), grades.tolist())))''',
    ["Add a 5th subject and recompute everything.", "Find the correlation between Math and Physics marks."])

add("project-image-processing", "Mini Project 2: Image Processing with Arrays", "Project",
    "Images are just arrays: height x width (grayscale) or height x width x 3 (RGB). Slicing and arithmetic become image editing.",
    "We build a synthetic 8x8 grayscale image and apply brightness change, thresholding, flipping, rotation and a 3x3 mean-blur using only NumPy.",
    r'''img = np.zeros((8, 8), dtype=np.uint8)
img[2:6, 2:6] = 200          # bright square
img[0, :] = 100              # top line

print("original:\n", img)
brighter = np.clip(img.astype(int) + 50, 0, 255).astype(np.uint8)
binary = (img > 150).astype(np.uint8)
print("binary:\n", binary)
print("flip LR equals img[:, ::-1]:", np.array_equal(np.fliplr(img), img[:, ::-1]))
print("rot90 shape:", np.rot90(img).shape)

# 3x3 mean blur via padding + slicing
p = np.pad(img.astype(float), 1, mode="edge")
blur = sum(p[i:i + 8, j:j + 8] for i in range(3) for j in range(3)) / 9
print("blurred center row:", blur[4].round(1))

rgb = np.stack([img, img // 2, img // 4], axis=-1)
print("RGB shape:", rgb.shape, "| grayscale back:", (rgb @ [0.299, 0.587, 0.114]).shape)''',
    ["Implement a vertical edge detector by subtracting neighboring columns.", "Load a real image with Pillow, convert to an array and invert it (255 - img)."])

add("cheat-sheet", "NumPy Cheat Sheet and Next Steps", "Reference",
    "A quick reference of the most-used NumPy functions grouped by task, plus ideas for what to learn next.",
    "**Create:** `array, zeros, ones, full, arange, linspace, eye, random.default_rng`\n\n**Inspect:** `shape, ndim, size, dtype, astype`\n\n**Reshape:** `reshape, ravel, flatten, T, concatenate, vstack, hstack, stack, split, newaxis`\n\n**Math:** `+ - * / ** @, sqrt, exp, log, abs, clip, round`\n\n**Reduce:** `sum, mean, std, var, min, max, argmin, argmax, median, percentile, cumsum`  (always think `axis`)\n\n**Select:** `a[i,j], slices, a[mask], a[[idx]], where, nonzero, take`\n\n**Sort/Set:** `sort, argsort, unique, isin, intersect1d, union1d, setdiff1d, searchsorted`\n\n**Linear algebra:** `dot, matmul, linalg.inv, solve, det, eig, svd, norm`\n\n**I/O:** `save, load, savez, savetxt, loadtxt, genfromtxt`\n\n**Next steps:** pandas (labeled tables), Matplotlib (plotting), SciPy (scientific algorithms), scikit-learn (machine learning), Numba (JIT speed), and practice on real datasets.",
    r'''cheat = {
    "create": ["array", "zeros", "ones", "arange", "linspace"],
    "reduce": ["sum", "mean", "std", "min", "max"],
    "select": ["where", "isin", "argsort", "unique"],
}
missing = [f for fs in cheat.values() for f in fs if not hasattr(np, f)]
print("All cheat-sheet functions exist in NumPy:", not missing)
print("Total public names in numpy:", len([n for n in dir(np) if not n.startswith("_")]))
help_example = np.sum.__doc__.splitlines()[0]
print("Tip - use help(np.func) or np.info(np.func). Example:", help_example)''',
    ["Pick any 10 functions above and write a one-line example for each.", "Build your own mini project: analyze a CSV with NumPy only."])
