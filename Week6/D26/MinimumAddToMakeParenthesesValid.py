class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        op,cl=0,0
        for i in S:
            if(not op):
                if i==')':
                    cl+=1
                else:
                    op+=1
            else:
                if(i=='('):
                    op+=1
                else:
                    op-=1
                    
        return op+cl
                
