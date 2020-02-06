class Solution:
    def rob(self, nums: List[int]) -> int:
        if(not nums):
            return 0
        elif(len(nums)<3):
            return max(nums)
        lst=[0]*len(nums)
        lst[0],lst[1]=nums[0],max(nums[0],nums[1])
        for i in range(2,len(nums)):
            lst[i]=max(lst[i-1],lst[i-2]+nums[i])
        return lst[-1]
