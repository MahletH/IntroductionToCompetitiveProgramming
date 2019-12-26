class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return self.peakIndex(A,0)
    def peakIndex(self, A: List[int], minIndex: int) -> int:
        mid=(len(A)+1)//2-1
        if(A[mid]>A[mid-1] and A[mid]>A[mid+1]):
            return mid+minIndex
        if(A[mid]<A[mid-1]):
            return self.peakIndex(A[:mid+1],minIndex)
            
        elif(A[mid]>A[mid-1]):
            return self.peakIndex(A[mid:],minIndex+mid)
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
