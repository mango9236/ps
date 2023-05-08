from collections import deque 
import sys
input = sys.stdin.readline

def bfs(start, find):
    queue = deque()
    queue.append((start,0)) # 초기에는 거리 0 대입
    visited = [start]

    while queue:
        node, d = queue.popleft() # 노드, 합친 거리 
        
        if node == find: # 만약 find를 찾았으면 합한 거리 return
            return d
        
        for next, len in graph[node]: # 튜플 언패킹 (연결노드, 연결 거리)
            if next not in visited:
                visited.append(next)
                queue.append((next, d+len)) # (다음노드, 거리합) 큐에 담기


# 빈 그래프 생성
n,m = map(int, input().split()) # 입력 n개 찾을거 m개쌍
graph = []
for i in range(n+1):
    graph.append(list())

# 그래프 연결 
# (매우 중요) 가중치 = 거리요소 넣을시 튜플로 그냥 넣어주면됨!
for i in range(n-1):
    a, b, d = map(int, input().split()) # 노드 1,2 + 거리
    graph[a].append((b,d))
    graph[b].append((a,d))


for i in range(m):
    n1, n2 = map(int, input().split())
    print(bfs(n1,n2))
