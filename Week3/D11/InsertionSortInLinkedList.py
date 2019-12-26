# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if(head==None):
            return None
        elif(head.next==None):
            return head
        cur=head
        pretemp=cur
        temp=head.next
        numNode=ListNode(temp.val)
        if(numNode.val<cur.val):
            cur.next=temp.next
            pretemp=cur
            temp=temp.next
            numNode.next=cur
            cur=numNode
        else:
            pretemp=temp
            temp=temp.next
        if(temp==None):
            return cur
        while(temp.next!=None):
            pre=cur
            pos=cur.next
            numNode=ListNode(temp.val)
            while(pos!=temp):
                if(numNode.val<cur.val):
                    pretemp.next=temp.next
                    numNode.next=cur
                    temp=temp.next
                    cur=numNode
                    break
                elif(numNode.val<pos.val):
                    pretemp.next=temp.next
                    pre.next=numNode
                    temp=temp.next
                    numNode.next=pos
                    break
                pre=pos
                pos=pos.next
            if(pos==temp):
                pretemp=temp
                temp=temp.next
        pre=cur
        pos=cur.next
        numNode=ListNode(temp.val)
        while(pos!=temp):
            if(numNode.val<cur.val):
                pretemp.next=None
                numNode.next=cur
                cur=numNode
                break
            elif(numNode.val<pos.val):
                pretemp.next=None
                pre.next=numNode
                numNode.next=pos
                break
            pre=pos
            pos=pos.next
        return cur
