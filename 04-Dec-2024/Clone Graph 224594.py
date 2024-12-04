# Problem: Clone Graph - https://leetcode.com/problems/clone-graph/

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
        if not node:
            return None

        nodes = {}
        nodes[node.val] = Node(node.val)
        stk = [node]
        visited = set()
        while stk:
            cn = stk.pop()
            if cn.val in visited:
                continue
            
            visited.add(cn.val)
            for nb in cn.neighbors:
                if nb.val not in nodes:
                    nodes[nb.val] = Node(nb.val)
                
                nodes[cn.val].neighbors.append(nodes[nb.val])
                stk.append(nb)

        return nodes[node.val]

                
