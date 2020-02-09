class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            for j in range(m):
                if(not i and not j):
                    continue
                elif(not i):
                    grid[i][j]=grid[i][j]+grid[i][j-1]
                elif(not j):
                    grid[i][j]=grid[i][j]+grid[i-1][j]
                else:
                    grid[i][j]=grid[i][j]+min(grid[i-1][j],grid[i][j-1])    
        return grid[n-1][m-1]
