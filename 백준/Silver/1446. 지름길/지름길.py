from collections import deque

N,D = map(int,input().split())

graph = [[] for _ in range(10_001)]
INF = 1e8
arr = [INF for _ in range(10_001)]

save = []
number = []

kk = []

for i in range(D+1):
    graph[i].append((i+1,1))

for _ in range(N):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

dq = deque()
arr[0]=0
dq.append((0,0))

while dq:
    x,y = dq.popleft()

    for i in graph[x]:
        if y+i[1] < arr[i[0]]:
            arr[i[0]] = y+i[1]
            dq.append((i[0],y+i[1]))

print(arr[D])