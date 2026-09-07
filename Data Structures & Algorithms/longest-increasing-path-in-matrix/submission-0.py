class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        memo = {}

        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            max_length = 1
            for dr,dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr,nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and matrix[nr][nc]>matrix[r][c]:
                    max_length = max(max_length, 1+dfs(nr,nc))
            memo[(r,c)] = max_length
            return max_length
        result = 0
        for i in range(rows):
            for j in range(cols):
                result = max(result, dfs(i,j))
        return result
        