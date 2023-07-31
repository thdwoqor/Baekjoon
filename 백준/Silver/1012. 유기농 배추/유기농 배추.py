from collections import deque
import sys

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    graph[a][b]=0
    while queue:
        aa,bb = queue.popleft()

        for i in range(4):
            dxx = dx[i] + aa
            dyy = dy[i] + bb

            if 0<=dxx<N and 0<=dyy<M:
                if graph[dxx][dyy]==1:
                    queue.append((dxx,dyy))
                    graph[dxx][dyy]=0
    return 1

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    M,N,K = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0]*M for _ in range(N)]
    cabbage = []

    for _ in range(K):
        X,Y = map(int,sys.stdin.readline().rstrip().split())
        graph[Y][X]=1
        cabbage.append((Y,X))
    
    count = 0

    for i,j in cabbage:
        if graph[i][j]==0:
            continue

        count+=bfs(i,j)

    print(count)


    
    

