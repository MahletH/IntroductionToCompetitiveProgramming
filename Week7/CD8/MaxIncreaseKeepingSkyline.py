class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        grid2=[]
        for i in range(len(grid)):
            col=[]
            for j in range(len(grid)):
                col.append(grid[j][i])
            grid2.append(col)
        tot=0
        for i in range(len(grid)):
            for j in range(len(grid)):
                n=min(max(grid[i]),max(grid2[j]))
                if grid[i][j]<n:
                    tot+=n-grid[i][j]
        return tot
