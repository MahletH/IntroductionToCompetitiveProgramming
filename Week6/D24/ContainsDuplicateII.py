class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        col={}
        for i in range(len(nums)):
            if nums[i] not in col:
                col[nums[i]]=i
            else:
                if (abs(col[nums[i]]-i)<=k):
                    return True
                else:
                    col[nums[i]]=i
        return False
            
