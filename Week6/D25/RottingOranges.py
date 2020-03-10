class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(grid):
            neighbours=[[0,1],[0,-1],[1,0],[-1,0]]
            que=collections.deque()
            ctr=0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==2:
                        start=i,j,0
                        que.append(start)
                    elif grid[i][j]==1: 
                        ctr+=1
            if not ctr:
                return 0
            while que:
                cur=que.popleft()
                for i in range(4):
                    neighbour=cur[0]+neighbours[i][0],cur[1]+neighbours[i][1]
                    if neighbour[0]>=0 and neighbour[0]<len(grid) and neighbour[1]>=0 and neighbour[1]<len(grid[0]) and grid[neighbour[0]][neighbour[1]]==1:
                        grid[neighbour[0]][neighbour[1]]=2
                        next_=neighbour[0],neighbour[1],cur[2]+1
                        que.append(next_)
                        ctr-=1
                        if not ctr:
                            return next_[2]
            if ctr:
                return -1
        return bfs(grid)
