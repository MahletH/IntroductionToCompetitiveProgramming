class Solution:
    def racecar(self, target: int) -> int:
        que=collections.deque()
        visited=set()
        start=(0,0,1)
        path={}
        path[start]=0
        que.append(start)
        visited.add(start)
        while (que):
            cur=que.popleft()            
            next_node=(cur[0] + cur[2]*(2**cur[1]), cur[1]+1, cur[2])
            path[next_node]=path[cur]+1
            if next_node[0] == target:
                return path[next_node]
            if next_node not in visited:
                que.append(next_node)
                visited.add(next_node)
                
            next_node=(cur[0],0,(cur[2])*-1)
            path[next_node]=path[cur]+1
            if next_node[0] == target:
                return path[next_node]
            if next_node not in visited:
                que.append(next_node)
                visited.add(next_node)
