import copy
import math
from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

# N, M = map(int, input().split())

# UV = [list(map(int, input().split())) for i in range(M)]

def dfs(node, graph, visited):
    """深さ優先探索による連結成分の探索"""
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node, graph, visited)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
for node in range(1, n+1):
    if not visited[node]:
        # 連結成分に含まれる頂点の個数と辺の本数が等しいかどうかを判定
        num_nodes = 0
        num_edges = 0
        dfs(node, graph, visited)
        for i in range(1, n+1):
            if visited[i]:
                num_nodes += 1
                num_edges += len(graph[i])
        if num_edges != num_nodes * 2:
            print("No")
            exit()

print("Yes")