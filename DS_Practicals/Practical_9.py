
from collections import deque

graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    vertex = input("Enter vertex: ")
    graph[vertex] = []

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v = input("Enter edge (u v): ").split()
    graph[u].append(v)
    graph[v].append(u)

def dfs(vertex, visited):
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)

        for neighbour in graph[vertex]:
            dfs(neighbour, visited)

def bfs(start):
    visited = {start}
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

start = input("Enter starting vertex: ")

print("DFS Traversal:", end=" ")
dfs(start, set())

print("\nBFS Traversal:", end=" ")
bfs(start)
print()
