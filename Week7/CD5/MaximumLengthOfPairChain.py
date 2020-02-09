class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        col={}
        for lst in pairs:
            n=0
            for key in col:
                if key<=lst[0]:
                    if col[key]>n:
                        n=col[key]
            if not n:
                if lst[1]+1 not in col:
                    col[lst[1]+1]=1
            else:
                n+=1
                if lst[1]+1 not in col:
                    col[lst[1]+1]=n
                else:
                    m=col[lst[1]+1]
                    if(n>m):
                        col[lst[1]+1]=n
        lst=list(col.values())
        return max(lst)
        
