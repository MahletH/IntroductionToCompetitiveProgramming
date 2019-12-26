class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z,o,t=0,0,0
        for i in nums:
            if i==0:
                z+=1
            elif i==1:
                o+=1
            elif i==2:
                t+=1
        for i in range(len(nums)):
            if i<z:
                nums[i]=0
            elif i<z+o:
                nums[i]=1
            elif i<z+o+t:
                nums[i]=2

def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            
            ret = Solution().sortColors(nums)

            out = integerListToString(nums)
            if ret is not None:
                print "Do not return anything, modify nums in-place instead."
            else:
                print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
