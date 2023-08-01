from collections import deque


N = int(input())
graph = [list(map(int,list(input()))) for _ in range(N)]
# visit = [[0]*N for _ in range(N)]

home = []

for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            home.append((i,j))

count = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b):
    queue = deque()
    c = 1
    queue.append((a,b))
    graph[a][b]=0

    while queue:
        x,y = queue.popleft()

        for z in range(4):
            xx = x + dx[z]
            yy = y + dy[z]

            if 0<=xx<N and 0<=yy<N:
                if graph[xx][yy]==1:
                    graph[xx][yy]=0
                    queue.append((xx,yy))
                    c+=1
    
    return c

for i,j in home:
    if graph[i][j]==1:
        count.append(bfs(i,j))

print(len(count))
count.sort()
print(*count,sep="\n")