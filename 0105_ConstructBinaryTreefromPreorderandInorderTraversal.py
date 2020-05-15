# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def build(root, preorder, inorder, lbound, rbound, p):
    
    # Base case: subtree is non-existent
    if lbound == rbound:
        return p
    # Base case: root is leaf
    if rbound == lbound + 1:
        return p+1
    
    # Identifying and finding tree root
    q = int()
    for q in range(lbound, rbound):
        if inorder[q] == preorder[p]:
            break
            
    if lbound != q:
        root.left = TreeNode(preorder[p+1])
        p = build(root.left, preorder, inorder, lbound, q, p+1)
    else:
        p += 1
    if q != rbound - 1:
        root.right = TreeNode(preorder[p])
        p = build(root.right, preorder, inorder, q+1, rbound, p)
    
    return p
    
    

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # Special case: Tree is empty
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        build(root, preorder, inorder, 0, len(preorder), 0)
        return root