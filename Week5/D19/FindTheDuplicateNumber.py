class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lst=[0]*len(nums)
        for i in nums:
            if lst[i]==0:
                lst[i]=i
            else:
                return i

def stringToIntegerList(input):
    return json.loads(input)

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
            
            ret = Solution().findDuplicate(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
