class Solution:
    def maxProduct(self, nums: List[int]) -> int: 
        max_=0
        if nums:
            max_=prev=alt=nums[0]
        for i,num in enumerate(nums):
            if not i:
                continue
            nums[i]=max(num,prev*num,alt*num)
            alt=min(num,prev*num,alt*num)
            prev=nums[i]
            max_=max(max_,prev)
        return max_
