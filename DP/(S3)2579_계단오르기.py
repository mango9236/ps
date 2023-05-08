import sys
input = sys.stdin.readline

n = int(input())
step = [0]*(n+1)
max_value = [0]*(n+1)

for i in range(1,n+1):
    step[i] = int(input())

max_value[1] = step[1] 
if n>=2: # 계단이 1개만 있을 경우를 방지
    max_value[2] = step[1] + step[2]
if n>=3: # 계단이 2개만 있을 경우를 방지
    max_value[3] = max(step[1]+step[3], step[2]+step[3]) # 1칸 -> 2칸 or # 2칸 -> 1칸 더 큰것

for i in range(4,n+1):
    max_value[i] = max(max_value[i-2]+step[i], max_value[i-3]+step[i-1]+step[i]) # 2칸전 합 + 지금 계단 or 3칸전 합 + 전 계단 + 지금 계단

print(max_value[n])