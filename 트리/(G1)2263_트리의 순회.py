import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def to_pre(left_in, right_in, left_post, right_post): # 중위순회 처음, 마지막 인덱스 + 후위순회 처음, 마지막 인덱스
    if left_in > right_in or left_post > right_post: # 역전되는 시점 그만
        return
    
    root = post[right_post]
    print(root, end=" ")
    # mid = inorder.index(root) --> 시간 많이 걸림
    mid = position[root]

    left_sub = mid - left_in # 중위 왼쪽 서브트리 길이
    right_sub = right_in - mid # 중위 오른쪽 서브트리 길이

    # 왼쪽트리 자르는 인덱스 지정 (중위,후위 왼쪽 서브트리는 인덱스 똑같음) 중위: 0~루트전 후위:0~루트전
    to_pre(left_in , mid-1, left_post, left_post + left_sub -1)
    # 오른쪽트리 중위: 중간 다음 ~ 끝, 후위: 전체-오른쪽 길이만큼 내려옴 ~ 전체-1(루트빼고)
    to_pre(mid+1, right_in, right_post-right_sub, right_post-1) 

n = int(input()) # 1~N 까지 노드 생성
inorder = list(map(int, input().split()))
post = list(map(int, input().split()))

position = [0]*(n+1) # inorder 값들의 위치 미리 저장 --> .index()가 시간이 많이 걸리므로 인덱스 값 미리 저장
for i in range(n):
    position[inorder[i]] = i 

to_pre(0, n-1, 0, n-1) # 인덱스는 실제보다 1작게 넘겨주므로



## 메모리초과 코드
# import sys
# sys.setrecursionlimit(10**5)

# n = int(input())

# def to_pre(post, inorder):
    
#     if len(post) == 1:
#         print(post[0], end=" ")
#         return 
    
#     if len(post) == 0:
#         return
    
#     root = post[-1]
#     print(root, end=" ")
#     for i,v in enumerate(inorder):
#         if v == root:
#             idx = i
#             break
#         idx = i
    
#     # inorder 서브트리 나누기
#     left_in = inorder[0:idx]
#     right_in = inorder[idx+1:]
#     # post 서브트리 나누기
#     left_post = post[:len(left_in)]
#     right_post = post[len(left_in):-1]
    
#     # print(left_in, right_in)
#     # print(left_post, right_post)

#     to_pre(left_post, left_in)
#     to_pre(right_post, right_in)


# inorder = list(map(int, input().split()))
# post = list(map(int, input().split()))


# index_lst = []
# to_pre(post, inorder)
