class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid)==0:
            return 0
        if obstacleGrid[0][0]:
            return 0
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j]:
                    obstacleGrid[i][j]=0
                else:
                    if i-1<0 and j-1<0:
                        obstacleGrid[i][j]=1
                    elif i-1<0:
                        obstacleGrid[i][j]=obstacleGrid[i][j-1] 
                    elif j-1<0:
                        obstacleGrid[i][j]=obstacleGrid[i-1][j] 
                    else:
                        obstacleGrid[i][j]=obstacleGrid[i][j-1] +obstacleGrid[i-1][j]
        return obstacleGrid[-1][-1]
