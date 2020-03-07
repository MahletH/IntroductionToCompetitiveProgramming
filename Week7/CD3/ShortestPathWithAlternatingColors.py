import collections
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        ans=[-1 for _ in range(n)]
        que=collections.deque()
        visited=set()
        start=(0,0,0)
        que.append(start)
        visited.add((0,1))
        visited.add((0,-1))
        while que:
            cur=que.popleft()
            if ans[cur[0]]==-1:
                ans[cur[0]]=cur[1]
            if not cur[0]:
                for red_edge in red_edges:
                    if red_edge[0]==0 and red_edge[1]:
                        que.append((red_edge[1],1,1))
                        visited.add((red_edge[1],1))
                for blue_edge in blue_edges:
                    if blue_edge[0]==0 and blue_edge[1]:
                        que.append((blue_edge[1],1,-1))
                        visited.add((blue_edge[1],-1))
            elif cur[2]==1:                    
                for blue_edge in blue_edges:
                    if blue_edge[0]==cur[0] and (blue_edge[1],-1) not in visited:
                        que.append((blue_edge[1],cur[1]+1,-1))
                        visited.add((blue_edge[1],-1))
            else:
                for red_edge in red_edges:
                    if red_edge[0]==cur[0] and (red_edge[1],1) not in visited:
                        que.append((red_edge[1],cur[1]+1,1))
                        visited.add((red_edge[1],1))
        return ans
