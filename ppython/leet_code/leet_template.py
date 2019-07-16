class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rmaxes = [0] * len(grid)
        cmaxes = [0] * len(grid)

        for r_i in range(len(grid)):
            for c_i in range(len(grid)):
                rmaxes[r_i] = max(rmaxes[r_i], grid[r_i][c_i])
                cmaxes[c_i] = max(cmaxes[c_i], grid[r_i][c_i])

        ans = 0

        for r_i in range(len(grid)):
            for c_i in range(len(grid)):
                ans += min(rmaxes[r_i], cmaxes[c_i]) - grid[r_i][c_i]
        return (ans)
