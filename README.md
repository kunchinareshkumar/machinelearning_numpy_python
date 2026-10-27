# 🔢 NumPy — Zero to Advanced Python Numerical Computing

### 📘 Complete NumPy Learning Guide | Python • Data Science • AI/ML • QA Engineering

<p align="center">
  <a href="https://github.com/kunchinareshkumar/machinelearning_numpy_python">
    <img src="https://img.shields.io/badge/Explore-Repository-181717?style=for-the-badge&logo=github" alt="Explore Repository"/>
  </a>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/NumPy-Numerical_Computing-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
  <img src="https://img.shields.io/badge/Learning_Path-Zero_to_Advanced-7C3AED?style=for-the-badge" alt="Zero to Advanced"/>
  <img src="https://img.shields.io/badge/Focus-AI%2FML_QA-16A34A?style=for-the-badge" alt="AI ML QA"/>
</p>

---

## 🌟 Welcome to the NumPy Learning Repository!

This repository is a structured learning resource for mastering **NumPy (Numerical Python)**, from basic array operations to advanced numerical computing concepts used in data science, machine learning, and AI/ML quality assurance.

It is designed for Python beginners, QA Engineers, SDETs, aspiring AI/ML Test Engineers, Data QA Engineers, and anyone who wants to strengthen their numerical computing skills.

The focus is on learning concepts in sequence, practicing Python code, understanding outputs, and applying NumPy to real-world testing and data analysis scenarios.

## 🎯 What You Will Learn

- 🔹 NumPy fundamentals and array creation
- 🔹 Array indexing, slicing, reshaping, and manipulation
- 🔹 Vectorization and broadcasting
- 🔹 Mathematical, statistical, and aggregation functions
- 🔹 Boolean masking and conditional filtering
- 🔹 Sorting, searching, and unique values
- 🔹 Random number generation and reproducibility
- 🔹 Linear algebra and matrix operations
- 🔹 Handling missing values and numerical edge cases
- 🔹 NumPy integration with Pandas and Matplotlib
- 🔹 Numerical validation for AI/ML and data quality testing
- 🔹 Practical projects and interview preparation

---

## 📚 Table of Contents

| # | Topic | Learning Focus |
|---:|---|---|
| 01 | [Introduction to NumPy](#-01-introduction-to-numpy) | Fundamentals |
| 02 | [Installation and Setup](#-02-installation-and-setup) | Environment setup |
| 03 | [NumPy Array Fundamentals](#-03-numpy-array-fundamentals) | `ndarray`, dimensions, shape |
| 04 | [Array Creation](#-04-array-creation-methods) | Creating arrays |
| 05 | [Indexing and Slicing](#-05-indexing-and-slicing) | Accessing elements |
| 06 | [Array Reshaping](#-06-array-reshaping-and-manipulation) | Reshape, transpose, flatten |
| 07 | [Data Types](#-07-data-types-and-type-conversion) | `dtype`, casting |
| 08 | [Mathematical Operations](#-08-mathematical-operations) | Arithmetic and universal functions |
| 09 | [Aggregation and Statistics](#-09-aggregation-and-statistical-functions) | Mean, median, standard deviation |
| 10 | [Broadcasting](#-10-broadcasting-and-vectorization) | Efficient calculations |
| 11 | [Boolean Masking](#-11-boolean-masking-and-filtering) | Conditions and filtering |
| 12 | [Sorting and Searching](#-12-sorting-and-searching) | Ordering and unique values |
| 13 | [Random Numbers](#-13-random-number-generation) | Sampling and reproducibility |
| 14 | [Linear Algebra](#-14-linear-algebra) | Vectors and matrices |
| 15 | [Missing Values and Edge Cases](#-15-missing-values-and-numerical-edge-cases) | NaN, infinity, validation |
| 16 | [Advanced NumPy](#-16-advanced-numpy-concepts) | Views, copies, performance |
| 17 | [Pandas and Matplotlib Integration](#-17-pandas-and-matplotlib-integration) | Data analysis |
| 18 | [AI/ML Testing Applications](#-18-numpy-for-aiml-testing) | Numerical validation |
| 19 | [Practice Projects](#-19-practical-projects) | Hands-on learning |
| 20 | [Interview Questions](#-20-interview-preparation) | Interview readiness |
| 21 | [Run the Repository](#-21-how-to-run-the-repository) | Local setup |
| 22 | [Learning Roadmap](#-22-learning-roadmap) | Suggested study sequence |
| 23 | [References](#-23-official-references) | Documentation |

---

## 🔰 01. Introduction to NumPy

NumPy is a Python library that provides efficient multidimensional arrays and numerical operations.

It is widely used in scientific computing, data analysis, statistics, and machine learning because it supports vectorized calculations and a broad range of mathematical functions.

### Why NumPy?

| Feature | Benefit |
|---|---|
| Multidimensional arrays | Represent vectors, matrices, and higher-dimensional data |
| Vectorization | Perform operations without manually looping over each element |
| Broadcasting | Combine compatible array shapes efficiently |
| Mathematical functions | Perform numerical calculations |
| Statistical functions | Summarize and analyze data |
| Linear algebra | Perform matrix multiplication and related operations |
| Random sampling | Generate reproducible test and simulation data |
| Memory-efficient data types | Store numerical data using appropriate types |

## 🛠️ 02. Installation and Setup

Install NumPy in your Python environment:

```bash
python3 -m pip install numpy
```

Import NumPy:

```python
import numpy as np

print(np.__version__)
```

Create your first array:

```python
numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
print(type(numbers))
print(numbers.shape)
print(numbers.ndim)
```

Expected output:

```text
[10 20 30 40 50]
<class 'numpy.ndarray'>
(5,)
1
```

## 🧱 03. NumPy Array Fundamentals

The primary NumPy data structure is `ndarray`, which represents an array with one or more dimensions.

| Array Type | Example | Shape |
|---|---|---|
| Scalar | `np.array(10)` | `()` |
| 1D array | `np.array([1, 2, 3])` | `(3,)` |
| 2D array | `np.array([[1, 2], [3, 4]])` | `(2, 2)` |
| 3D array | `np.zeros((2, 3, 4))` | `(2, 3, 4)` |

Important attributes:

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.ndim)   # Number of dimensions
print(arr.shape)  # Dimensions along each axis
print(arr.size)   # Total number of elements
print(arr.dtype)  # Element data type
print(arr.itemsize)  # Bytes per element
print(arr.nbytes)    # Total array data bytes
```

## 🏗️ 04. Array Creation Methods

Learn the main methods for creating arrays.

| Method | Example |
|---|---|
| `np.array()` | `np.array([1, 2, 3])` |
| `np.zeros()` | `np.zeros((2, 3))` |
| `np.ones()` | `np.ones((2, 3))` |
| `np.full()` | `np.full((2, 2), 7)` |
| `np.arange()` | `np.arange(0, 10, 2)` |
| `np.linspace()` | `np.linspace(0, 1, 5)` |
| `np.eye()` | `np.eye(3)` |
| `np.empty()` | `np.empty((2, 3))` |
| `np.identity()` | `np.identity(3)` |

Example:

```python
import numpy as np

print(np.zeros(3))
print(np.ones(3))
print(np.arange(1, 6))
print(np.linspace(0, 10, 5))
```

**Note:** `np.empty()` does not initialize its elements to zero. Its initial contents should not be assumed to be meaningful.

## 🔍 05. Indexing and Slicing

Access specific elements or select parts of an array.

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])     # First element
print(arr[-1])    # Last element
print(arr[1:4])   # Slice from index 1 to 3
print(arr[::2])   # Every second element
```

For two-dimensional arrays:

```python
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(matrix[0, 1])  # 20
print(matrix[1, :])  # Second row
print(matrix[:, 0])  # First column
print(matrix[0:2, 1:3])
```

Practice:

- Positive and negative indexing
- Basic slicing
- Row and column selection
- Integer-array indexing
- Boolean indexing
- Differences between views and copies

## 🔄 06. Array Reshaping and Manipulation

Learn to modify array shapes and combine or split arrays.

| Operation | Example |
|---|---|
| Reshape | `arr.reshape(2, 3)` |
| Flatten to a copy | `arr.flatten()` |
| Return a flattened view when possible | `arr.ravel()` |
| Transpose | `arr.T` |
| Add a dimension | `np.expand_dims(arr, axis=0)` |
| Remove single-sized dimensions | `np.squeeze(arr)` |
| Concatenate | `np.concatenate((a, b))` |
| Stack vertically | `np.vstack((a, b))` |
| Stack horizontally | `np.hstack((a, b))` |
| Split an array | `np.split(arr, 2)` |

Example:

```python
arr = np.arange(1, 7)

matrix = arr.reshape(2, 3)

print(matrix)
print(matrix.T)
```

Always ensure that the new shape is compatible with the number of elements.

## 🔢 07. Data Types and Type Conversion

NumPy supports numerical and other data types, including integers, floating-point numbers, booleans, and complex numbers.

```python
arr = np.array([1, 2, 3])

print(arr.dtype)

float_arr = arr.astype(np.float64)

print(float_arr)
print(float_arr.dtype)
```

Key concepts:

- Integer types: `int8`, `int32`, `int64`
- Floating-point types: `float32`, `float64`
- Boolean type: `bool`
- Complex type: `complex128`
- Type inference
- Explicit type conversion
- Integer overflow considerations
- Precision and rounding
- Memory usage

Choose data types carefully when validating numerical results or processing large datasets.

## ➕ 08. Mathematical Operations

NumPy performs element-wise arithmetic on compatible arrays.

```python
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
```

Important functions:

| Category | Functions |
|---|---|
| Arithmetic | `np.add()`, `np.subtract()`, `np.multiply()`, `np.divide()` |
| Powers | `np.power()`, `np.sqrt()` |
| Absolute values | `np.abs()` |
| Rounding | `np.round()`, `np.floor()`, `np.ceil()` |
| Exponential and logarithmic | `np.exp()`, `np.log()` |
| Trigonometry | `np.sin()`, `np.cos()`, `np.tan()` |
| Comparisons | `np.equal()`, `np.greater()`, `np.less()` |
| Element-wise selection | `np.where()` |

Example:

```python
scores = np.array([45, 75, 90, 30])

result = np.where(scores >= 50, "Pass", "Fail")

print(result)
```

## 📊 09. Aggregation and Statistical Functions

Summarize numerical data using statistical and aggregation operations.

| Function | Purpose |
|---|---|
| `np.sum()` | Total |
| `np.mean()` | Arithmetic mean |
| `np.median()` | Median |
| `np.min()` / `np.max()` | Minimum and maximum |
| `np.std()` | Standard deviation |
| `np.var()` | Variance |
| `np.percentile()` | Percentile |
| `np.quantile()` | Quantile |
| `np.argmin()` / `np.argmax()` | Index of minimum or maximum |
| `np.cumsum()` | Cumulative sum |
| `np.cumprod()` | Cumulative product |
| `np.corrcoef()` | Correlation coefficients |
| `np.unique()` | Unique values |

Example:

```python
scores = np.array([60, 70, 80, 90, 100])

print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Minimum:", np.min(scores))
print("Maximum:", np.max(scores))
print("Standard deviation:", np.std(scores))
```

Remember that `np.std()` uses `ddof=0` by default, which calculates population standard deviation. Use `ddof=1` when the sample standard deviation is appropriate.

## ⚡ 10. Broadcasting and Vectorization

**Broadcasting** allows NumPy to perform operations on arrays with compatible shapes without requiring them to have identical dimensions.

```python
arr = np.array([10, 20, 30])

print(arr + 5)
```

Broadcasting with a matrix:

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

values = np.array([10, 20, 30])

print(matrix + values)
```

Learn:

- Broadcasting rules
- Scalar-to-array operations
- Row-wise and column-wise operations
- `axis=0` and `axis=1`
- Vectorized calculations
- Performance comparison with Python loops
- Shape compatibility and broadcasting errors

## 🎯 11. Boolean Masking and Filtering

Filter data using conditions instead of manually iterating through every element.

```python
scores = np.array([35, 55, 75, 90, 40])

print(scores[scores >= 50])
print(scores[scores < 50])
```

Combine conditions:

```python
scores = np.array([35, 55, 75, 90, 40])

result = scores[(scores >= 50) & (scores <= 80)]

print(result)
```

Additional concepts:

- Boolean masks
- Multiple conditions
- `np.where()`
- `np.select()`
- `np.any()`
- `np.all()`
- `np.count_nonzero()`
- Conditional replacement

Use parentheses around individual conditions when combining them with `&` or `|`.

## 🔎 12. Sorting and Searching

Useful functions for data preparation and validation:

| Function | Purpose |
|---|---|
| `np.sort()` | Sort values |
| `np.argsort()` | Return sorting indices |
| `np.argmax()` | Index of maximum value |
| `np.argmin()` | Index of minimum value |
| `np.where()` | Find indices matching a condition |
| `np.unique()` | Identify unique values |
| `np.isin()` | Check membership |
| `np.searchsorted()` | Find insertion positions in sorted arrays |
| `np.count_nonzero()` | Count nonzero or true values |

Example:

```python
arr = np.array([30, 10, 40, 10, 20])

print(np.sort(arr))
print(np.unique(arr))
print(np.where(arr > 20))
```

## 🎲 13. Random Number Generation

Random data is useful for simulations, sampling, test-data generation, and machine learning experiments.

Recommended modern API:

```python
rng = np.random.default_rng(seed=42)

print(rng.integers(1, 101, size=5))
print(rng.random(5))
print(rng.normal(loc=0, scale=1, size=5))
```

Learn:

- `default_rng()`
- Random integers
- Uniform distributions
- Normal distributions
- Random sampling
- Shuffling and permutations
- Reproducible experiments
- Synthetic test data
- Sampling and simulation

A fixed seed helps reproduce results when the same generator and operations are used. It does not guarantee identical outputs across every possible NumPy version or execution setup.

## 🧮 14. Linear Algebra

Linear algebra is foundational for machine learning, numerical optimization, and many model computations.

| Operation | Function |
|---|---|
| Matrix multiplication | `@` or `np.matmul()` |
| Dot product | `np.dot()` |
| Transpose | `.T` |
| Determinant | `np.linalg.det()` |
| Matrix inverse | `np.linalg.inv()` |
| Solve a linear system | `np.linalg.solve()` |
| Eigenvalues and eigenvectors | `np.linalg.eig()` |
| Matrix rank | `np.linalg.matrix_rank()` |
| Vector or matrix norm | `np.linalg.norm()` |
| Singular value decomposition | `np.linalg.svd()` |

Example:

```python
A = np.array([
    [2, 1],
    [1, 3]
])

b = np.array([5, 6])

solution = np.linalg.solve(A, b)

print(solution)
print(A @ solution)
```

For numerical work, prefer `np.linalg.solve(A, b)` over explicitly calculating an inverse to solve a linear system.

## ⚠️ 15. Missing Values and Numerical Edge Cases

Handle exceptional values before relying on calculations.

```python
arr = np.array([10.0, 20.0, np.nan, 40.0])

print(np.isnan(arr))
print(np.nanmean(arr))
print(np.nanmax(arr))
print(np.isfinite(arr))
```

Important topics:

- `np.nan`
- `np.isnan()`
- `np.isinf()`
- `np.isfinite()`
- `np.nanmean()`
- `np.nanmedian()`
- Division by zero
- Overflow and underflow
- Floating-point precision
- Empty arrays
- Invalid shapes
- Integer overflow
- Numerical tolerance using `np.isclose()` and `np.allclose()`

Example of numerical comparison:

```python
actual = np.array([0.1 + 0.2])
expected = np.array([0.3])

print(np.allclose(actual, expected))
```

Use tolerances for floating-point comparisons instead of assuming every decimal calculation will be exactly equal.

## 🚀 16. Advanced NumPy Concepts

Once the fundamentals are clear, explore:

- Views versus copies
- Memory layout and strides
- Advanced indexing
- Broadcasting with higher-dimensional arrays
- Universal functions (ufuncs)
- Reduction operations and axes
- Structured arrays
- Masked arrays
- `np.einsum()`
- `np.vectorize()` and its limitations
- Memory-efficient array processing
- Numerical precision
- Performance profiling
- Array serialization and loading
- `np.save()`, `np.load()`, `np.savez()`
- Text data loading with `np.loadtxt()` and `np.genfromtxt()`

**Important:** `np.vectorize()` is primarily a convenience wrapper and does not automatically provide the performance benefits of true compiled vectorized operations.

## 🔗 17. Pandas and Matplotlib Integration

NumPy works alongside other popular Python data libraries.

### NumPy + Pandas

```python
import numpy as np
import pandas as pd

arr = np.array([100, 200, 300])

df = pd.DataFrame({
    "Sales": arr
})

print(df)
print(df["Sales"].mean())
```

### NumPy + Matplotlib

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 6)
y = x ** 2

plt.plot(x, y, marker="o")
plt.xlabel("X")
plt.ylabel("X squared")
plt.title("NumPy Data Visualization")
plt.grid(True)
plt.show()
```

These integrations are useful for EDA, data validation, numerical analysis, and reporting.

## 🤖 18. NumPy for AI/ML Testing

NumPy can help validate numerical outputs and investigate data issues throughout an AI/ML pipeline.

| Testing Area | NumPy Application |
|---|---|
| Data validation | Check dimensions, types, ranges, and invalid values |
| Preprocessing | Validate transformations and normalization |
| Model output testing | Compare actual and expected arrays |
| Regression testing | Detect numerical changes across model versions |
| Classification testing | Analyze prediction arrays and class counts |
| Numerical stability | Investigate NaN, infinity, and precision errors |
| Statistical analysis | Calculate means, variances, and percentiles |
| Synthetic test data | Generate controlled numerical inputs |
| Drift investigation | Compare feature distributions and summary statistics |
| Performance validation | Analyze latency and throughput measurements |

### Example: Validate Model Predictions

```python
import numpy as np

actual = np.array([0.25, 0.50, 0.75])
expected = np.array([0.25, 0.50, 0.75])

if np.allclose(actual, expected, rtol=1e-5, atol=1e-8):
    print("PASS: Predictions match within tolerance")
else:
    print("FAIL: Prediction mismatch")
```

### Example: Validate Data Quality

```python
data = np.array([10.0, 20.0, 30.0, np.nan, 50.0])

print("Missing values:", np.isnan(data).sum())
print("Finite values:", np.isfinite(data).sum())
print("Mean excluding NaN:", np.nanmean(data))
```

### Example: Compare Model Errors

```python
actual = np.array([100, 200, 300, 400])
predicted = np.array([110, 190, 310, 390])

mae = np.mean(np.abs(actual - predicted))
rmse = np.sqrt(np.mean((actual - predicted) ** 2))

print("MAE:", mae)
print("RMSE:", rmse)
```

These examples demonstrate numerical checks; production testing should additionally define acceptance criteria, expected behavior, tolerances, and appropriate evaluation metrics.

## 🧪 19. Practical Projects

Build these projects to strengthen your NumPy skills.

| Project | Description | Skills |
|---|---|---|
| 01. Student Marks Analyzer | Analyze scores and grades | Arrays, filtering, statistics |
| 02. Test Result Analyzer | Summarize automated test outcomes | Boolean masks, aggregation |
| 03. API Performance Analyzer | Analyze response-time measurements | Percentiles, mean, standard deviation |
| 04. Data Quality Validator | Identify missing and invalid numerical values | NaN, infinity, conditions |
| 05. ML Prediction Validator | Compare expected and actual predictions | Tolerance, array comparison |
| 06. Synthetic Test Data Generator | Generate repeatable numerical datasets | Random generation |
| 07. Model Error Analyzer | Calculate regression errors | Vectorization, aggregation |
| 08. Dataset Distribution Analyzer | Compare numerical distributions | Percentiles, statistics |
| 09. Matrix Operations Practice | Solve numerical linear systems | Linear algebra |
| 10. NumPy Visualization Project | Plot arrays and trends | Matplotlib integration |

## 🎤 20. Interview Preparation

Prepare to explain these topics with examples:

1. What is NumPy, and why is it used?
2. What is the difference between a Python list and a NumPy array?
3. What are `ndim`, `shape`, `size`, and `dtype`?
4. What is the difference between `arange()` and `linspace()`?
5. What is broadcasting?
6. What is vectorization?
7. What is the difference between a view and a copy?
8. How do `reshape()`, `flatten()`, and `ravel()` differ?
9. How does Boolean masking work?
10. What is the difference between `axis=0` and `axis=1`?
11. How do you handle NaN and infinity?
12. How do you compare floating-point values safely?
13. How do you generate reproducible random test data?
14. How can NumPy support ML model validation?
15. How would you compare prediction outputs between two model versions?

---

## ▶️ 21. How to Run the Repository

### Option 1: Clone the repository

```bash
git clone https://github.com/kunchinareshkumar/machinelearning_numpy_python.git

cd machinelearning_numpy_python
```

### Option 2: Create a virtual environment on macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### Option 3: Install NumPy and Jupyter

```bash
python -m pip install --upgrade pip

python -m pip install numpy pandas matplotlib jupyter
```

### Option 4: Launch Jupyter Notebook

```bash
python -m jupyter notebook
```

Open the relevant `.ipynb` notebook from the repository and run the cells in sequence.

> **Note:** The commands above provide a general setup. Notebook-specific dependencies and filenames may vary depending on the actual contents of the repository.

## 🗺️ 22. Learning Roadmap

Follow this recommended sequence.

| Stage | Focus | Goal |
|---|---|---|
| 🟢 Beginner | Arrays, data types, creation | Understand NumPy fundamentals |
| 🟡 Intermediate | Slicing, reshaping, filtering | Manipulate numerical data |
| 🟠 Upper Intermediate | Broadcasting, statistics, random data | Perform efficient calculations |
| 🔵 Advanced | Linear algebra, views, memory | Understand advanced operations |
| 🟣 Data Analysis | NumPy, Pandas, Matplotlib | Explore and validate datasets |
| 🔴 AI/ML QA | Numerical validation, metrics, edge cases | Test data and model outputs |
| ⭐ Portfolio | Practical projects and GitHub documentation | Demonstrate applied skills |

## 📚 23. Official References

- [NumPy Official Documentation](https://numpy.org/doc/)
- [NumPy User Guide](https://numpy.org/doc/stable/user/)
- [NumPy API Reference](https://numpy.org/doc/stable/reference/)
- [NumPy Absolute Beginners Guide](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/)

---

## 👨‍💻 About the Author

**Naresh Kumar**

Learning and sharing practical resources in Python, NumPy, Pandas, Matplotlib, QA automation, data quality, and AI/ML testing.

This repository is part of a hands-on learning journey toward applying Python and numerical computing in data analysis and AI/ML quality engineering.

## 🤝 Contributions and Feedback

Suggestions, corrections, and learning improvements are welcome. Explore the repository, practice the examples, and contribute ideas that make numerical computing easier to understand.

If you find this resource useful:

- ⭐ Star the repository.
- 🍴 Fork it for your own practice.
- 🐛 Report issues or corrections.
- 🔗 Share it with other Python and QA learners.

---

<p align="center">

### 🚀 Learn • Practice • Analyze • Validate • Build

**From Python fundamentals to numerical computing for AI/ML quality engineering.**

</p>
