class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.searchAgain(nums,target,0)
    def searchAgain(self, nums: List[int], target: int, minIndex: int) -> int:
        if(len(nums)<1):
            return -1
        mid=(len(nums)-1)//2
        if(nums[mid]==target):
            return mid+minIndex
        elif(nums[mid]>target):
            return self.searchAgain(nums[:mid],target,minIndex)
        else:
            return self.searchAgain(nums[mid+1:],target,minIndex+mid+1)
def stringToIntegerList(input):
    out=[]
    for i in input:
      out.append(int(i))
    return out

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
            A = stringToIntegerList(line);
            
            ret = Solution().peakIndexInMountainArray(A)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
