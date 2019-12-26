class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        valid=True
        peri=0
        maxPeri=0
        A.sort()
        for i in range(len(A)-2):
            j=i+1
            k=j+1
            if((A[i]+A[j]<=A[k]) or (A[i]+A[k]<=A[j]) or (A[j]+A[k]<=A[i])):
                valid=False
            if(valid):
                peri=A[i]+A[j]+A[k]
                if(maxPeri<peri):
                    maxPeri=peri
            valid=True
        return maxPeri

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
            
            ret = Solution().largestPerimeter(A)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
