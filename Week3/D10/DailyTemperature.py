class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack=[]
        ans=[]
        for i in reversed(T):
            cur=0
            while stack:
                if stack[-1][0]>i:
                    break
                else:
                    cur+=stack.pop()[1]+1
            if stack:
                ans.append(cur+1)
            else:
                ans.append(0)
            stack.append((i,cur))
        ans.reverse()
        return ans
