class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        for i in range(len(shifts)-2,-1,-1):
            shifts[i]=shifts[i]+shifts[i+1]
        res=[]
        for i in range(len(S)):
            c=ord(S[i])-97
            res.append(str(chr((c+shifts[i])%26+97)))
        return "".join(res)
    
