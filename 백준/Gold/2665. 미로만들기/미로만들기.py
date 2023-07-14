from collections import deque

N = int(input())
graph = [list(map(int,list(input()))) for _ in range(N)]
visit = [[0]*N for _ in range(N)]

dq = deque()
if graph[0][0]: 
    dq.append((0,0,0))
else:
    dq.append((1,0,0))

dx = [0,1,0,-1]
dy = [-1,0,1,0]

while dq:
    count,x,y = dq.popleft()
    visit[x][y]=1

    if x==N-1 and y==N-1:
        print(count)
        break

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<N and 0<=yy<N and visit[xx][yy]==0:
            if graph[xx][yy]==0:
                dq.append((count+1,xx,yy))
            else:
                dq.appendleft((count,xx,yy))
