# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if(root == None):
            return []
        
        return self.traverse(root, [])
    
    def traverse(self, a, l):
        if(a.left != None):
            l = self.traverse(a.left, l)
            
        l.append(a.val)
        
        if(a.right != None):
            l = self.traverse(a.right, l)
            
        return l