# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        temp=root
        if(p.val>q.val):
            p,q=q,p
        if(p.val>root.val):
            root=root.right
            while(p.val>root.val):
                root=root.right
            temp=root
        if(q.val<root.val):
            #leftsum=root.val
            root=root.left
            while(q.val<root.val):
                root=root.left
            temp=root
        if(root.val<p.val):
            root=self.lowestCommonAncestor(root,p,q)
        else:
            while(temp.val!=p.val):
                if(temp.val>p.val):
                    temp=temp.left
                else:
                    temp=temp.right
        temp=root
        if(root.val>q.val):
            root=self.lowestCommonAncestor(root,p,q)
        else:
            while(temp.val!=q.val):
                if(temp.val<q.val):
                    temp=temp.right
                else:
                    temp=temp.left
        return root
