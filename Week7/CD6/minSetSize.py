class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        col={}
        lst=[]
        for i in arr:
            if i not in col:
                col[i]=1
            else:
                col[i]+=1
        for i in col:
            lst.append(col[i])
        if(len(lst)==len(arr)):
            return len(arr)//2
        lst.sort()
        lst.reverse()
        tot=0
        ctr=0
        half=len(arr)//2
        for i in lst:
            if(tot>=half):
                break
            tot+=i
            ctr+=1
        return ctr
