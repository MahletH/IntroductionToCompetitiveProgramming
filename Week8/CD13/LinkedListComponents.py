# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        ans=[]
        node=set()
        for i in G:
            node.add(i)
        temp=head
        lst=[]
        while temp:
            if temp.val in node:
                lst.append(temp.val)                
            else:
                if len(lst):
                    ans.append(lst)
                    lst=[]
            temp=temp.next
        if len(lst):
            ans.append(lst)
        return len(ans)
