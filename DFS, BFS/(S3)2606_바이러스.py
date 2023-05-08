# dfs
def dfs(graph, start, visited):
    visited.append(start) # 지금 이 노드 방문

    for node in graph[start]: # 그 노드랑 연결된 노드들 방문
        if node not in visited: # 방문 안되있으면 재귀
            dfs(graph, node, visited)
    
    return visited

n = int(input())

lst = []
# 2차원 빈 배열
for i in range(n+1):
    lst.append(list())

edge = int(input())
# 간선을 리스트 형태로 연결 -> 나중에 그래프로
for i in range(edge):
    a, b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

# 그래프 연결
graph = {}
for k,v in enumerate(lst):
    graph[k] = v

visited = [] # 방문 노드 넣을 곳
dfs(graph, 1, visited) # dfs -> 1번이랑 연결된 모든 노드 방문

print(len(visited)-1) # 1번빼고 나머지