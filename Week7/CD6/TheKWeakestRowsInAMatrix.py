class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        col={}
        for m in range(len(mat)):
            cur=sum(mat[m])
            if(cur not in col):
                col[cur]=[m]
            else:
                col[cur].append(m)
        lst=list(col.keys())
        lst.sort()
        i=0
        new=[]
        for c in lst:
            cur=col[c]
            for j in cur:
                if(i==k):
                    break
                nw.append(j)
                i+=1
        return new
