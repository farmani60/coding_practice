"""
Breadth First Search: Shortest Reach

Description: https://www.hackerrank.com/challenges/bfsshortreach/problem
"""

def BFS(n, edges, node):

    # build graph
    graph = dict()
    for i in range(n+1):
        graph[i] = []
    for edge in edges:
        graph[edge[0]].append(edge[1])

    # breadth first search
    reached = {}
    visited = [node]
    queue = [(node, 0)]

    while queue:
        curr_node, curr_cost = queue.pop(0)
        for nb in graph[curr_node]:
            if nb not in visited:
                visited.append(nb)
                reached[nb] = curr_cost + 6
                queue.append((nb, curr_cost + 6))

    results = []
    for vr in range(1, n+1):
        if vr != node:
            results.append(reached.get(vr, -1))
    return results

edges = [(2, 3)]
print(BFS(3, edges, 2))



