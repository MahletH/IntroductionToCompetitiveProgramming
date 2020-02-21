# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self,root,parent):
        if not root:
            return 0,0
        left=self.traverse(root.left,root)
        right=self.traverse(root.right,root)
        total=left[0]+right[0],left[1]+right[1]
        load=total[1]-(root.val-1)
        if not parent:
            return total
        return total[0]+abs(load),load
    def distributeCoins(self, root: TreeNode) -> int:
        return self.traverse(root,None)[0]
        
