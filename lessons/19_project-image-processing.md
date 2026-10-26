# 19. Mini Project 2: Image Processing with Arrays

**Level:** Project

## Definition

Images are just arrays: height x width (grayscale) or height x width x 3 (RGB). Slicing and arithmetic become image editing.

## Explanation

We build a synthetic 8x8 grayscale image and apply brightness change, thresholding, flipping, rotation and a 3x3 mean-blur using only NumPy.

## Code

```python
img = np.zeros((8, 8), dtype=np.uint8)
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
print("RGB shape:", rgb.shape, "| grayscale back:", (rgb @ [0.299, 0.587, 0.114]).shape)
```

## Output

```text
original:
 [[100 100 100 100 100 100 100 100]
 [  0   0   0   0   0   0   0   0]
 [  0   0 200 200 200 200   0   0]
 [  0   0 200 200 200 200   0   0]
 [  0   0 200 200 200 200   0   0]
 [  0   0 200 200 200 200   0   0]
 [  0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0]]
binary:
 [[0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 1 1 1 1 0 0]
 [0 0 1 1 1 1 0 0]
 [0 0 1 1 1 1 0 0]
 [0 0 1 1 1 1 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]]
flip LR equals img[:, ::-1]: True
rot90 shape: (8, 8)
blurred center row: [  0.   66.7 133.3 200.  200.  133.3  66.7   0. ]
RGB shape: (8, 8, 3) | grayscale back: (8, 8)
```

## Exercises

1. Implement a vertical edge detector by subtracting neighboring columns.
2. Load a real image with Pillow, convert to an array and invert it (255 - img).
