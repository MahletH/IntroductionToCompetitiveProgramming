# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:    
    def lowestCommonAncestorOfDeepestLeaves(self, root: TreeNode) -> TreeNode:        
        def find_depth(root,depth):
            if not root.left and not root.right:
                return root,depth
            
            elif root.left and not root.right:
                return find_depth(root.left,depth+1)
            
            elif root.right and not root.left:
                return find_depth(root.right,depth+1)
            
            left_child_depth=find_depth(root.left,depth+1)
            right_child_depth=find_depth(root.right,depth+1)
            
            if left_child_depth[1]==right_child_depth[1]:
                return root,left_child_depth[1]
            
            if left_child_depth[1]>right_child_depth[1]:
                return left_child_depth
            
            return right_child_depth
        
        return find_depth(root,0)[0]
