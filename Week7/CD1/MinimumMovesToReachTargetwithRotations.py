class State:
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
        self.dist=0
    def __hash__(self):
        return self.x1*self.x2*self.y1*self.y2+self.x1+self.x2+self.y1+self.y2
    def __eq__(self, other):
            return (self.__class__ == other.__class__ and self.x1 == other.x1 and self.x2 == other.x2 and self.y1 == other.y1 and self.y2 == other.y2)

class Solution:
    def isFree(self, neighbour: State, grid: List[List[int]], n: int, i: int) -> bool:
        if(neighbour.x1<0 or neighbour.x1>=n or
          neighbour.y1<0 or neighbour.y1>=n or
          neighbour.x2<0 or neighbour.x2>=n or
          neighbour.y2<0 or neighbour.y2>=n or
          grid[neighbour.x1][neighbour.y1] or
          grid[neighbour.x2][neighbour.y2]):
            return False
        if(i==2):
            if(grid[neighbour.x2][neighbour.y2+1] or neighbour.y1 != neighbour.y2):
                return False
        elif(i==3):
            if(grid[neighbour.x2+1][neighbour.y2] or neighbour.y1 == neighbour.y2):
                return False
        return True
    def minimumMoves(self, grid: List[List[int]]) -> int:
        que=[]
        n=len(grid)
        neighbours=[[0,1,0,1],[1,0,1,0],[0,0,1,-1],[0,0,-1,1]]
        start=State(0,0,0,1)
        end=State(n-1,n-2,n-1,n-1)
        que.append(start)
        visited=set()
        visited.add(start)
        j=0
        while(j<len(que)):
            curr=que[j]
            j+=1
            for i in range(4):
                neighbour=State(curr.x1+neighbours[i][0],curr.y1+neighbours[i][1],curr.x2+neighbours[i][2],curr.y2+neighbours[i][3])
                neighbour.dist=curr.dist+1
                if(self.isFree(neighbour,grid,len(grid),i) and not neighbour in visited):
                    que.append(neighbour)
                    visited.add(neighbour)
                    if(neighbour.x1==end.x1 and neighbour.y1==end.y1 and neighbour.x2==end.x2 and neighbour.y2==end.y2):
                        return neighbour.dist
        return -1
