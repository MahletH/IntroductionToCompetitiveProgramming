class Solution:
    def trailingZeroes(self, n: int) -> int:
        res=n//5
        while(n//5>=5):
            n=n//5      
            res+=n//5      
        return res

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
            n = int(line);
            
            ret = Solution().trailingZeroes(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
