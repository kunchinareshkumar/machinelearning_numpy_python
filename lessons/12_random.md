# 12. Random Number Generation

**Level:** Intermediate

## Definition

NumPy's random module generates pseudo-random numbers from many distributions. The modern API uses a `Generator` created by `np.random.default_rng(seed)`.

## Explanation

Using a fixed seed makes results reproducible. The generator offers `random`, `integers`, `normal`, `uniform`, `choice`, `shuffle`, `permutation`, `binomial`, `poisson`, and more. Prefer `default_rng` over the legacy `np.random.seed` / `np.random.rand` functions.

## Code

```python
rng = np.random.default_rng(42)

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
print("sample mean/std:", sample.mean().round(3), sample.std().round(3))
```

## Output

```text
uniform [0,1): [0.774 0.439 0.859]
integers     : [1 5 2 1 4]
normal       : [51.28 46.84 49.83]
choice       : ['blue' 'blue' 'green' 'green']
permutation  : [1 0 2 4 3]
shuffled     : [0 9 8 4 7 2 3 5 6 1]
mean of 10k dice rolls: 3.475
sample mean/std: -0.004 1.004
```

## Exercises

1. Simulate 1000 coin flips and count heads.
2. Draw 5 random samples without replacement from 1..20.
