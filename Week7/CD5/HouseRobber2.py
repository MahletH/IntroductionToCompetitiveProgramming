class Solution:
    def rob(self, nums: List[int]) -> int:
        if(not nums):
            return 0
        if(len(nums)<=3):
            return max(nums)
        with_=[0 for i in range(len(nums))]
        with_out=[0 for i in range(len(nums))]
        with_[0],with_[1]=nums[0],nums[1]
        with_out[0],with_out[1]=nums[0],nums[1]
        with_[2],with_[3]=nums[0]+nums[2],nums[3]+max(nums[0],nums[1])
        with_out[2],with_out[3]=nums[2],nums[3]+nums[1]
        for i in range(4,len(nums)):
            with_[i]=nums[i]+max(with_[i-2],with_[i-3])
            with_out[i]=nums[i]+max(with_out[i-2],with_out[i-3])
        return max(with_[len(nums)-2],with_out[-1],with_[len(nums)-3])
            
