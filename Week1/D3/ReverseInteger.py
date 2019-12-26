class Solution:
    def reverse(self, x: int) -> int:
        signed=False
        y=""
        if x>=0:
            y=str(x)
            
        elif x<0:
            signed=True
            y=str(x)
            y=y[1:]
        rev=""
        for k in y:
            rev=k+rev
        if(signed):
            rev="-"+rev
        num=int(rev)
        if(num>=2147483647 or num<=-2147483648):
            return 0
        
        return num

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
            x = int(line);
            
            ret = Solution().reverse(x)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
