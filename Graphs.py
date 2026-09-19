# BFS Traversal using Queue

from collections import deque

# Graph represented as adjacency list
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}


def bfs(graph, start):

    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:

        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)




# Driver Code
print("BFS Traversal:")
bfs(graph, 1)


# DFS Traversal using Recursion

# Graph represented as adjacency list
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}


def dfs(graph, node, visited):

    if node not in visited:

        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


# Driver Code
visited = set()

print("DFS Traversal:")
dfs(graph, 1, visited)