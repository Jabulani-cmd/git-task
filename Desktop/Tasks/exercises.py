def minesweeper(grid):
    if not grid: return []

    rows, cols = len(grid), len(grid[0])
    result = [[0] * cols for _ in range(rows)]

    # All 8 possible adjacent directions (northwest to southeast)
    directions = ((-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1))

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '#':
                result[i][j] = '#'
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and result[ni][nj] != '#':
                        result[ni][nj] += 1

    return result