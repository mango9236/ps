import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split()) # 세로, 가로
graph = []

for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))
    
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_x, start_y = i,j


# 동서남북 
dx = [1,-1,0,0]
dy = [0,0,-1,1]

queue = deque([start_x, start_y])

# bfs
while queue:
    current = queue.popleft()
    c_x, c_y = current[0], current[1]

    for i in range(4):
        n_x, n_y = 


