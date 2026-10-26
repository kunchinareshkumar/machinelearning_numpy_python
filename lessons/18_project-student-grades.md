# 18. Mini Project 1: Student Grade Analysis

**Level:** Project

## Definition

A practical exercise combining random data, aggregation, boolean masks, sorting and broadcasting.

## Explanation

We simulate marks for 8 students in 4 subjects and answer typical analytics questions without a single loop.

## Code

```python
rng = np.random.default_rng(7)
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
print("Grades:", dict(zip(students.tolist(), grades.tolist())))
```

## Output

```text
marks:
 [[96 77 81 93]
 [74 86 90 53]
 [43 58 57 92]
 [94 40 69 89]
 [47 87 47 68]
 [88 58 60 56]
 [83 55 99 66]
 [68 70 74 73]]

Top 3: [('S1', 347), ('S2', 303), ('S7', 303)]
Subject averages: {'Math': 74.1, 'Physics': 66.4, 'Chem': 72.1, 'English': 73.8}
Hardest subject : Physics
Students failing any subject (<50): ['S3' 'S4' 'S5']
Best z-score student per subject: ['S1' 'S5' 'S7' 'S1']
Grades: {'S1': 'A', 'S2': 'B', 'S3': 'C', 'S4': 'B', 'S5': 'C', 'S6': 'C', 'S7': 'B', 'S8': 'B'}
```

## Exercises

1. Add a 5th subject and recompute everything.
2. Find the correlation between Math and Physics marks.
