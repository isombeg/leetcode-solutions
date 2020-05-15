# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # Special case: Tree is empty
        if root == None:
            return []
        
        rslt, stack = list(), list()
        stack.append(root)
        
        while len(stack):
            holder = stack.pop()
            if holder.right:
                stack.append(holder.right)
            if holder.left:
                stack.append(holder.left)
            rslt.append(holder.val)
            
        return rslt