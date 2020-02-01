class Solution:       
    def removeDuplicates(self, s: str, k: int) -> str:
        prev=s[0]
        ctr=0
        prevctr=[]
        output=''
        for i in range(len(s)):
            if(s[i]==prev):
                output=output+prev
                ctr+=1
            else:
                prevctr.append(ctr)
                ctr=1
                prev=s[i]
                output=output+prev
            if(ctr==k):
                m=len(output)-k
                output=output[:m]
                if(len(output)):
                    prev=output[-1]
                    if(len(prevctr)==0):
                        ctr=0
                    else:
                        ctr=prevctr.pop()
                else:
                    prev=s[i]
                    ctr=0
        return output
                
                
            
            
