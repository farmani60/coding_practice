"""
Breadth First Search Algorithm:

Breadth-first search (BFS) is an algorithm for traversing or searching tree or
graph data structures. It starts at the tree root (or some arbitrary node of a
graph, sometimes referred to as a 'search key', and explores all of the
neighbor nodes at the present depth prior to moving on to the nodes at the next
depth level.
"""

visited = [] # list to keep track of visited nodes
queue = [] # initialize a queue

def BFS(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': ['F'],
  'F': []
}

BFS(visited, graph, 'A')