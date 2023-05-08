lst = []
n, m = map(int, input().split())
# 2차원 빈 배열
for i in range(n+1):
    lst.append(list())

# 간선을 리스트 형태로 연결 -> 나중에 그래프로
for i in range(m):
    a, b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

# 그래프 연결
graph = {}
for k,v in enumerate(lst):
    graph[k] = v

# bfs
from collections import deque
def bfs(graph, start):
       
    num = [0]*(n+1) # start노드와 각 노드간 거리를 저장해줄 리스트
    queue = deque([start])
    visited = [start]

    while(queue): # 큐 남은게 없을때까지
        
        node = queue.popleft()
        
        for i in graph[node]:
            if i not in visited: # 자식 노드가 방문한 노드가 아니면
                num[i] = num[node] + 1 # 방문할 노드 = 지금 노드의 번째 + 1칸
                visited.append(i) 
                queue.append(i) # 큐에는 바로 옆에 연결된 노드들이 연결됨.
    
    return sum(num)

result = [] # 각각 베이컨법칙의 단계를 넣음 
for i in range(1, n+1):
    result.append(bfs(graph, i))

print(result.index(min(result))+1) # 가장 작은 값을 가지는 사람 인덱스 + 1 (0번부터) = 자기 번호 (1번부터)
    