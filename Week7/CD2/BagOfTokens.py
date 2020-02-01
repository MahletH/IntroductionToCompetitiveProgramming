class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        max_points,points=0,0
        start=0
        end=len(tokens)-1
        while(start<=end):
            if(P-tokens[start]>=0):
                points+=1
                P-=tokens[start]
                start+=1
                if(max_points<points):
                    max_points=points
            else:
                if(points==0):
                    return max_points
                points-=1
                P+=tokens[end]
                end-=1
        return max_points
                
            
