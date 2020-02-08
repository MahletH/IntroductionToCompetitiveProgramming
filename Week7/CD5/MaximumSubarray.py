class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tot=0
        lst=[]
        pos=0
        for i in range(len(nums)):
            if(not pos):
                lst.append(nums[i])
                if(nums[i]>=0):
                    pos=1
                    tot=nums[i]
            else:
                tot+=nums[i]
                if(tot<0):
                    tot=0
                lst.append(tot)
        return max(lst)
