H,W,X,Y=map(int,input().split())

graph = [ list(map(int,input().split())) for _ in range(H+X) ]
arr = [[0]*W for _ in range(H)]

for i in range(H):
    for j in range(0,Y):
        arr[i][j]=graph[i][j]

for i in range(0,X):
    for j in range(W):
        arr[i][j]=graph[i][j]

for i in range(X,H):
    for j in range(Y,W):
        arr[i][j]=graph[i][j]-arr[i-X][j-Y]

for i in arr:
    print(*i)