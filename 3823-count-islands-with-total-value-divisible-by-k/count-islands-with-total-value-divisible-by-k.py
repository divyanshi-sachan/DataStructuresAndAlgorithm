class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            visited[r][c] = True

            total = grid[r][c]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < m and
                    0 <= nc < n and
                    grid[nr][nc] > 0 and
                    not visited[nr][nc]):

                    total += dfs(nr, nc)

            return total
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    island_sum = dfs(i, j)
                    if island_sum % k == 0:
                        count += 1
        return count