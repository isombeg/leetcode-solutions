# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # Special case: Tree is empty
        if not root:
            return []
        
        stack, rslt = list(), list()
        stack.append(root)
        holder = TreeNode(-1)
        
        while len(stack):
            if holder is stack[-1].left or holder is stack[-1].right:
                holder = stack.pop()
                rslt.append(holder.val)
                
            else:
                if stack[-1].right:
                    stack.append(stack[-1].right)
                    
                    if stack[-2].left:
                        stack.append(stack[-2].left)
                
                elif stack[-1].left:
                    stack.append(stack[-1].left)
                
                else:
                    holder = stack.pop()
                    rslt.append(holder.val)
            
        return rslt