# 16. Vectorization and Performance

**Level:** Advanced

## Definition

Vectorization replaces explicit Python loops with array expressions so the work happens in optimized C loops, often 10x to 100x faster.

## Explanation

Avoid iterating over elements in Python. Use ufuncs, broadcasting, boolean masks and `np.where`. Memory layout matters too: C-contiguous arrays are fastest when traversed along the last axis. Use `%timeit` in notebooks or `time.perf_counter` in scripts to measure.

## Code

```python
import time

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

print("C-contiguous:", np.zeros((3, 3)).flags["C_CONTIGUOUS"])
```

## Output

```text
same result: True
python loop: 131.3 ms
numpy      : 2.1 ms
speed-up   : about 61x
C-contiguous: True
```

## Exercises

1. Time a loop vs vectorized computation of the sum of squares for 10 million numbers.
2. Rewrite `[x if x > 0 else 0 for x in a]` with NumPy.
