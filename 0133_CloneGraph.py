"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

def clone(a, node, hashmap):
    a.val = node.val
    hashmap[node] = a
    for v in node.neighbors:
        if v in hashmap:
            a.neighbors.append(hashmap[v])
        else:
            b = Node()
            a.neighbors.append(b)
            hashmap = clone(b,v,hashmap)
    return hashmap

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Special case: Graph is empty
        if node == None:
            return None
        
        a = Node()
        clone(a, node, dict())
        return a