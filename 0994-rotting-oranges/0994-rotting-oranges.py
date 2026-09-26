class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dq = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    dq.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        time_taken = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while dq:
            for _ in range(len(dq)):
                r, c = dq.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        dq.append((nr, nc))
            
            if dq:
                time_taken += 1
            
        return time_taken if fresh == 0 else -1