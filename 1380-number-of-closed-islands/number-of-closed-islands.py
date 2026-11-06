class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visited[i][j]:
                    stack = [(i, j)]
                    visited[i][j] = True
                    is_closed = True
                    while stack:
                        r, c = stack.pop()
                        if r == 0 or r == m-1 or c == 0 or c == n-1:
                            is_closed = False
                        for dr, dc in directions:
                            nr = r + dr
                            nc = c + dc
                            if (0 <= nr < m and
                                0 <= nc < n and
                                grid[nr][nc] == 0 and
                                not visited[nr][nc]):
                                visited[nr][nc] = True
                                stack.append((nr, nc))
                    if is_closed:
                        count += 1
        return count