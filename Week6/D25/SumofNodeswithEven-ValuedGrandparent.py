# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self,root: 'Node', lsts: List[int]) -> int:        
        temp=root
        if(root.val%2==0):
            if(not root.left and not root.right):
                return 
            if(root.left):
                temp=root.left
                if(temp.left):
                    lsts.append(temp.left.val)
                if(temp.right):
                    lsts.append(temp.right.val)
            if(root.right):            
                temp=root.right
                if(temp.left):
                    lsts.append(temp.left.val)
                if(temp.right):
                    lsts.append(temp.right.val)
            if(root.left):
                self.pathSum(root.left,lsts)
            if(root.right):
                self.pathSum(root.right,lsts)
        else:
            if(root.left):
                self.pathSum(root.left,lsts)
            if(root.right):
                self.pathSum(root.right,lsts)
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if(not root):
            return 0
        lst=[]
        self.pathSum(root,lst)
        return sum(lst)
        
