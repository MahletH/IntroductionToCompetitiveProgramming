class Solution:
    def posJump(self, arr: List[int], d: int, ind:int, col:dict) -> int:
        if(ind not in col):
            lst=[]
            for i in range(1,d+1):
                if(ind-i>=0 and arr[ind-i]<arr[ind]):
                    lst.append(self.posJump(arr,d,ind-i,col))
                else:
                    break
            for i in range(1,d+1):
                if(ind+i<len(arr) and arr[ind+i]<arr[ind]):
                    lst.append(self.posJump(arr,d,ind+i,col))
                else:
                    break
            if(not len(lst)):
                col[ind]=1
            else:
                col[ind]=1+max(lst)
        return col[ind]
    def maxJumps(self, arr: List[int], d: int) -> int:
        lst=[]
        col={}
        for i in range(len(arr)):
            lst.append(self.posJump(arr,d,i,col))
        return max(lst)
