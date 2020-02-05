class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        lst=[0]*len(cost)
        lst[0],lst[1]=cost[0],cost[1]
        for i in range(2,len(cost)):
            lst[i]=min(lst[i-1],lst[i-2])+cost[i]
        return min(lst[-1],lst[-2])
