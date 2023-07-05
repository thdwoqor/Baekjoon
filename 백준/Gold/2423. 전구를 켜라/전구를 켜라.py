from collections import deque
from queue import PriorityQueue

N, M = map(int,input().split())

arr = [list(map(lambda x: -1 if  x=="\\" else 1,list(input()))) for _ in range(N)] 
visit = [[0]*M for _ in range(N)]
cnt = 0

if arr[0][0]!=-1:
    arr[0][0]=-1
    cnt += 1
if arr[N-1][M-1]!=-1:
    arr[N-1][M-1]=-1
    cnt += 1

queue = deque()
queue.append((cnt, 0, 0, -1))


dx = [1,0,0,-1]
dy = [0,1,-1,0]

ddx = [1,-1]
ddy = [1,-1]

dddx = [1,-1]
dddy = [-1,1]

if (N+M)%2:
    print("NO SOLUTION")
else:
    while(queue):
        c,x,y,s = queue.popleft()
        visit[x][y] = 1

        if x==N-1 and y==M-1: 
            print(c)
            break

        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0<=xx<N and 0<=yy<M and visit[xx][yy]==0:
                if s != arr[xx][yy]:
                    queue.appendleft((c,xx,yy,arr[xx][yy]))
                else:
                    if not (xx==N-1 and yy==M-1):
                        queue.append((c+1,xx,yy,arr[xx][yy]*-1))

        if s == -1:
            for k in range(2):
                xx = x + ddx[k]
                yy = y + ddy[k]
                if 0<=xx<N and 0<=yy<M and visit[xx][yy]==0:
                    if s == arr[xx][yy]:
                        queue.appendleft((c,xx,yy,arr[xx][yy]))
                    else:
                        if not (xx==N-1 and yy==M-1):
                            queue.append((c+1,xx,yy,arr[xx][yy]*-1))
        if s == 1:
            for k in range(2):
                xx = x + dddx[k]
                yy = y + dddy[k]
                if 0<=xx<N and 0<=yy<M and visit[xx][yy]==0:
                    if s == arr[xx][yy]:
                        queue.appendleft((c,xx,yy,arr[xx][yy]))
                    else:
                        if not (xx==N-1 and yy==M-1):
                            queue.append((c+1,xx,yy,arr[xx][yy]*-1))

# 2 4
# \\\\
# \\/\