import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre=[0]*numCourses
        for lst in prerequisites:
            pre[lst[0]]+=1
        que=collections.deque()
        res=[]
        visited=set()
        for i in range(numCourses):
            if not pre[i]:
                que.append(i)
                visited.add(i)
        while(len(que)):
            curr=que.popleft()
            res.append(curr)
            for lst in prerequisites:
                if lst[1]==curr:
                    pre[lst[0]]-=1
                if not pre[lst[0]] and lst[0] not in visited:
                    que.append(lst[0])
                    visited.add(lst[0])                    
        if len(res)==numCourses:
            return res
        return []
