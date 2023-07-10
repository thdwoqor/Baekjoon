from collections import deque

INF = 1e8
N,M,K,X = map(int,input().split())

graph = [[] for _ in range(N+1)]
arr = [INF]*(N+1)

for _ in range(M):
    i,j = map(int,input().split())
    if j!=X:
        graph[i].append((j,1))

dq = deque()
dq.append((X,0))

while dq:
    i,j = dq.popleft()
    
    for g in graph[i]:
        if j+g[1] < arr[g[0]]:
            arr[g[0]]=j+g[1]
            dq.append((g[0],j+g[1]))

check= False

for i,j in enumerate(arr):
    if K==j:
        print(i)
        check=True

if not check:
    print(-1)