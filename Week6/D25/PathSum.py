# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self,root: 'Node',l: int, lsts: List[int]) -> int:        
        l+=root.val
        if(not root.left and not root.right):
            lsts.append(l)
            return l
        if(root.left):
            self.pathSum(root.left,l,lsts)
        if(root.right):            
            self.pathSum(root.right,l,lsts)
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if(not root):
            return False
        inSum=0
        lstOfSums=[]
        self.pathSum(root,inSum,lstOfSums)
        if sum in lstOfSums:
            return True
        return False
