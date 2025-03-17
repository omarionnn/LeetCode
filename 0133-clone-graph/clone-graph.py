"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        holder = {}

        def dfs(root):
            if not root:
                return 

            if root in holder:
                return holder[root]

            copy = Node(root.val)
            holder[root] = copy

            for n in root.neighbors:
                copy.neighbors.append(dfs(n))

            return copy

        return dfs(node)
        