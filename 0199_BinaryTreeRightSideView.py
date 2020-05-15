# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def getView(root):
    # Base case: node is a leaf
    if root.left == None and root.right == None:
        return [root.val]
    
    l, r = list(), list()
    # Get right view of left
    if root.left != None:
        l = getView(root.left)
    # Get right view of right
    if root.right != None:
        r = getView(root.right)
        
    # Compare both view
    rslt = [root.val] + r
    if len(l) > len(r):
        rslt += l[len(r):]
    return rslt
    

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        #Special case: tree given is empty
        if root == None:
            return None
        
        return getView(root)