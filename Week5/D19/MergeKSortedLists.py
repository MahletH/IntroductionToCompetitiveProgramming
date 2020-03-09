# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        arr=[]
        for node in lists:
            while node:
                arr.append(node.val)
                node=node.next
        if not len(arr):
            return None
        heapq.heapify(arr)
        root=ListNode(heapq.heappop(arr))
        temp=root
        while len(arr):
            temp.next=ListNode(heapq.heappop(arr))
            temp=temp.next
        return root
