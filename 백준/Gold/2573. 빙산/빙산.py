from collections import deque


N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0

ice = []

def bfs(x,y):
    delIce= []
    queue = deque()
    queue.append((x,y))
    visited[x][y] =1
    while queue:
        a,b = queue.popleft()
        zero = 0

        for k in range(4):
            aa = a+ dx[k]
            bb = b+ dy[k]
            if graph[aa][bb] == 0:
                zero += 1
            elif visited[aa][bb]==0 and graph[aa][bb]>0: 
                queue.append((aa,bb))
                visited[aa][bb]=1
        if zero>0: 
            delIce.append((a,b,zero))

    for g,h,j in delIce:
        if graph[g][h]-j>=0:
            graph[g][h]=graph[g][h]-j
        else:
            graph[g][h]=0

    return 1

for i in range(N):
   for j in range(M): 
       if graph[i][j]>0:
           ice.append((i,j))

count = 0

while ice:
    visited = [[0] * M for _ in range(N)]
    group = 0
    delIce = []

    for x,y in ice:
        if graph[x][y]>0 and visited[x][y]==0:
            group += bfs(x,y)
        if graph[x][y]==0:
            delIce.append((x,y))
    
    if group>1:
        print(count)
        break

    ice = sorted(list(set(ice) - set(delIce)))
    count += 1

if group<2:
    print(0)
