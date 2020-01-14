class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        word=A[0]
        col={}
        lst=[]
        for i in word:
            if i not in col:
                col[i]=1
            else:
                col[i]+=1
        for k in range(1,len(A)):
            col2={}
            word=A[k]
            for i in word:
                if i not in col2:
                    col2[i]=1
                else:
                    col2[i]+=1
            for c in col:
                if c in col2:
                    if(col2[c]<col[c]):
                        col[c]=col2[c]
                else:
                    col[c]=0
        for c in col:
            for i in range(col[c]):
                lst.append(c)
                
        return lst
                
