class NumArray:

    def __init__(self, nums: List[int]):
        self.lst=[]
        if(len(nums)):
            self.lst.append(nums[0])
        for i in range(1,len(nums)):
            self.lst.append(self.lst[i-1]+nums[i])
        self.nums=nums
    def sumRange(self, i: int, j: int) -> int:
        return self.lst[j]-self.lst[i]+self.nums[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
