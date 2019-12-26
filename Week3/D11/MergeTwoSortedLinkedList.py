# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if(l1==None):
            return l2
        elif(l2==None):
            return l1
        head1=l1
        head2=l2
        if(head1.val<=head2.val):
            head3=ListNode(head1.val)
            cur=head3
            head1=head1.next
        elif(head1.val>head2.val):
            head3=ListNode(head2.val)
            cur=head3
            head2=head2.next
        while(head1!=None and head2!=None):
            if(head1.val<=head2.val):
                node=ListNode(head1.val)
                head1=head1.next
            elif(head1.val>head2.val):
                node=ListNode(head2.val)
                head2=head2.next
            cur.next=node
            cur=cur.next
        if(head1!=None):
            cur.next=head1
        elif(head2!=None):
            cur.next=head2
        return head3

def stringToIntegerList(input):
    return json.loads(input)

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
            
            ret = Solution().mergeTwoLists(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
