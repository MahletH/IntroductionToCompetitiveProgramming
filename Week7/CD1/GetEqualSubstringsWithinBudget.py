class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        lst=[]
        anLst=[]
        for i in range(len(s)):
            lst.append(abs(ord(s[i])-ord(t[i])))
        total=0
        lastind=0
        for i in range(len(lst)):
            total+=lst[i]
            if(total>maxCost):
                anLst.append(i-lastind)
                total-=lst[lastind]
                lastind+=1
            else:
                anLst.append(i-lastind+1)
        return max(anLst)       
                
            
        
