class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n=len(M)
        lst=[1]*n
        visited=set()
        circle=0
        for ind in range(n):
            if(lst[ind]):
                que=[ind]
                visited.add(ind)
                circle+=1
                k=0
                while(k<len(que)):
                    curr=que[k]
                    lst[curr]=0
                    k+=1
                    for j in range(n):
                        if(M[curr][j]==1):
                            if(j not in visited):
                                que.append(j)
                                visited.add(j)
                                lst[j]=0
        return circle
                            
