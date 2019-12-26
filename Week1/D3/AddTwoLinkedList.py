# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp=""
        temp2=""
        li1=l1
        li2=l2
        while(li1):
            temp=str(li1.val)+temp
            li1=li1.next
        while(li2):
            temp2=str(li2.val)+temp2
            li2=li2.next
        res=str(int(temp)+int(temp2))
        x=len(res)-1
        node=ListNode(res[x])
        node1=node
        x-=1
        while(x>=0):
            node.next=ListNode(res[x])
            node=node.next
            x-=1
        return node1
        
def stringToIntegerList(input):
    out=[]
    for i in input:
      out.append(int(i))
    return out

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

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
            l1 = stringToListNode(line);
            line = next(lines)
            l2 = stringToListNode(line);
            
            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
