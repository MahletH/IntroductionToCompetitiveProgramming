class Solution:
    def check(self, arr: List[int], start: int, visited: set) -> bool:
        if(not arr[start]):
            return True
        move=arr[start]
        left=start-move
        right=start+move
        if(left>=0 and left not in visited):
            visited.add(left)
            if(self.check(arr,left,visited)):
                return True
        if(right<len(arr) and right not in visited):
            visited.add(right)
            if(self.check(arr,right,visited)):
                return True
        return False    
    def canReach(self, arr: List[int], start: int) -> bool:
        visited=set()
        return self.check(arr,start,visited)
