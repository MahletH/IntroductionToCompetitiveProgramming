class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            if (i%2==0 and A[i]%2!=0):
                for j in range(i+1,len(A)):
                    if(A[j]%2==0):
                        A[i],A[j]=A[j],A[i]
                        break;
            elif (i%2!=0 and A[i]%2==0):
                for j in range(i+1,len(A)):
                    if(A[j]%2!=0):
                        A[i],A[j]=A[j],A[i]
                        break
        return A
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
