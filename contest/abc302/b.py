def find_snuke(H, W, grid):
    # Check each position in the grid
    for i in range(H):
        for j in range(W):
            # Check horizontally
            if j <= W - 5 and grid[i][j : j + 5] == "snuke":
                return [(i + 1, j + n) for n in range(1, 6)]
            if j <= W - 5 and grid[i][j : j + 5][::-1] == "snuke":
                return [(i + 1, j + n) for n in reversed(range(1, 6))]

            # Check vertically
            if i <= H - 5 and "".join(grid[k][j] for k in range(i, i + 5)) == "snuke":
                return [(i + n, j + 1) for n in range(1, 6)]
            if (
                i <= H - 5
                and "".join(grid[k][j] for k in range(i, i + 5))[::-1] == "snuke"
            ):
                return [(i + n, j + 1) for n in reversed(range(1, 6))]
            # Check diagonally
            if (
                i <= H - 5
                and j <= W - 5
                and "".join(grid[i + k][j + k] for k in range(5)) == "snuke"
            ):
                return [(i + n, j + n) for n in range(1, 6)]
            if (
                i - 4 >= 0
                and j - 4 >= 0
                and "".join(grid[i - k][j - k] for k in range(5)) == "snuke"
            ):
                return [(i - n + 1, j - n + 1) for n in range(5)]
            if (
                i - 4 >= 0
                and j <= W - 5
                and "".join(grid[i - k][j + k] for k in range(5)) == "snuke"
            ):
                return [(i - n + 1, j + n + 1) for n in range(5)]
            if (
                i <= H - 5
                and j - 4 >= 0
                and "".join(grid[i + k][j - k] for k in range(5)) == "snuke"
            ):
                return [(i + n + 1, j - n + 1) for n in range(5)]


# Read the input
H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# Find the position of "snuke"
pos = find_snuke(H, W, grid)

for p in pos:
    print(*p)
