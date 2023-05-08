lst = []
n, edge, start = map(int, input().split())
# 2차원 빈 배열
for i in range(n+1):
    lst.append(list())

# 간선을 리스트 형태로 연결 -> 나중에 그래프로
for i in range(edge):
    a, b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

# 방문할 수 있는 정점이 여러개 --> 정렬해서 작은것부터
for i,value in enumerate(lst): 
    lst[i] = sorted(value)


# 그래프 연결
graph = {}
for k,v in enumerate(lst):
    graph[k] = v

# dfs
def dfs(graph, start, visited):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)
    return visited


# bfs
from collections import deque
def bfs(graph, root, visited):
    
    queue = deque([root])

    while(queue): # 큐 남은게 없을때까지
        node = queue.pop()
        
        # 이 노드를 방문한적 없으면 visited 추가
        # visited 추가 후, 자식 노드를 queue에 추가
        if node not in visited:
            visited.append(node)
            queue.extendleft(graph[node])
    return visited

dfs_visited = []
dfs(graph, start, dfs_visited)
bfs_visited = []
bfs(graph, start, bfs_visited)

for i in dfs_visited:
    print(i, end=" ")
print("")
for i in bfs_visited:
    print(i, end=" ")
    