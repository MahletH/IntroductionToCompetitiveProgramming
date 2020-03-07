class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        an=[]
        i,j=0,0
        while i<len(popped):
            if an:
                if popped[i]==an[-1]:
                    an.pop()
                    i+=1
                    continue
            if j==len(pushed):
                break
            an.append(pushed[j])
            j+=1
        while i<len(popped) and an:            
            if popped[i]!=an[-1]:
                return False
            an.pop()
            i+=1
        return True
