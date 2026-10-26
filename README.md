# NumPy Learning Roadmap

A structured, beginner-to-advanced path through NumPy. Every topic has a definition, explanation,
runnable code with real output, and exercises.

## How to use this repo

1. `pip install -r requirements.txt`
2. Read the lessons in order (`lessons/01_...` to `lessons/20_...`), or
3. Open the single notebook: `jupyter notebook NumPy_Complete_Guide.ipynb`

## Roadmap

| # | Topic | Level |
|---|-------|-------|
| 01 | [Introduction to NumPy](lessons/01_introduction.md) | Beginner |
| 02 | [Creating Arrays](lessons/02_creating-arrays.md) | Beginner |
| 03 | [Array Attributes and Data Types](lessons/03_attributes-dtypes.md) | Beginner |
| 04 | [Indexing and Slicing](lessons/04_indexing-slicing.md) | Beginner |
| 05 | [Reshaping, Transposing, Joining and Splitting](lessons/05_reshaping-joining.md) | Beginner |
| 06 | [Arithmetic Operations and Universal Functions](lessons/06_operations-ufuncs.md) | Beginner |
| 07 | [Broadcasting](lessons/07_broadcasting.md) | Intermediate |
| 08 | [Aggregations and Statistics](lessons/08_aggregations-statistics.md) | Intermediate |
| 09 | [Boolean Masking, Fancy Indexing and np.where](lessons/09_boolean-fancy-indexing.md) | Intermediate |
| 10 | [Sorting, Searching, and Set Operations](lessons/10_sorting-searching.md) | Intermediate |
| 11 | [Linear Algebra](lessons/11_linear-algebra.md) | Intermediate |
| 12 | [Random Number Generation](lessons/12_random.md) | Intermediate |
| 13 | [Copies vs Views](lessons/13_copy-vs-view.md) | Intermediate |
| 14 | [Missing Values: NaN and Inf](lessons/14_missing-values.md) | Intermediate |
| 15 | [Saving and Loading Data](lessons/15_file-io.md) | Intermediate |
| 16 | [Vectorization and Performance](lessons/16_performance.md) | Advanced |
| 17 | [Advanced Features: vectorize, einsum, Structured and Masked Arrays](lessons/17_advanced-features.md) | Advanced |
| 18 | [Mini Project 1: Student Grade Analysis](lessons/18_project-student-grades.md) | Project |
| 19 | [Mini Project 2: Image Processing with Arrays](lessons/19_project-image-processing.md) | Project |
| 20 | [NumPy Cheat Sheet and Next Steps](lessons/20_cheat-sheet.md) | Reference |

## Repo layout

```
numpy-learning-roadmap/
├── README.md
├── requirements.txt
├── NumPy_Complete_Guide.ipynb   # all topics in one notebook
├── lessons/                     # one markdown file per topic
├── data/                        # files created by the I/O lesson
└── build.py, topics.py          # source used to generate the lessons and notebook
```

## Suggested study plan

- Week 1: topics 01-06 (arrays, indexing, reshaping)
- Week 2: topics 07-11 (math, broadcasting, statistics, masking, sorting)
- Week 3: topics 12-16 (linear algebra, random, copies/views, NaN, file I/O)
- Week 4: topics 17-20 (performance, advanced features, projects, cheat sheet)

## Further reading

- Official docs: https://numpy.org/doc/stable/
- NumPy user guide: https://numpy.org/doc/stable/user/index.html
