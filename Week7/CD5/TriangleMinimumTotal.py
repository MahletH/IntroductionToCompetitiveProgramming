class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        last=len(triangle)-2
        while(last>=0):
            for i in range(len(triangle[last])):
                triangle[last][i]=triangle[last][i]+min(triangle[last+1][i],triangle[last+1][i+1])
            last-=1
        return triangle[0][0]
