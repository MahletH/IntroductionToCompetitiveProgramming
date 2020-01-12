class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        numA1=""
        numA2=""
        for i in a:
            if i=="i":
                break;
            elif i!="+":
                numA2+=i
            else:
                numA1=numA2
                numA2=""
        numB1=""
        numB2=""
        for i in b:
            if i=="i":
                break;
            elif i!="+":
                numB2+=i
            else:
                numB1=numB2
                numB2=""
        n=int(numA1)*int(numB1)-int(numA2)*int(numB2)
        c=int(numA1)*int(numB2)+int(numA2)*int(numB1)
        return str(n)+"+"+str(c)+"i"

def stringToString(input):
    import json

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
            a = stringToString(line);
            line = next(lines)
            b = stringToString(line);
            
            ret = Solution().complexNumberMultiply(a, b)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
