"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# class Solution:
#     def __init__(self):
#         self.visited = {}

#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if not node:
#             return node

#         if node in self.visited:
#             return self.visited[node]

#         clone_node = Node(node.val, [])
#         self.visited[node] = clone_node

#         if node.neighbors:
#             clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

#         return clone_node
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        visited = {}
        queue = [node]
        clone_node = Node(node.val, [])
        visited[node] = clone_node
        
        while queue:
            curr_node = queue.pop(0)
            for neighbor in curr_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[curr_node].neighbors.append(visited[neighbor])
        
        return clone_node

        