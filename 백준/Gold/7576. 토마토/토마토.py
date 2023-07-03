from collections import deque


M,N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
result = 0
ll = [-1,0,1,0]
rr = [0,1,0,-1]

def zero(l):
    count = 0
    for i in range(N):
        count += list(l[i]).count(0)
    return count

for i in range(N):
    for j in range(M):
        if arr[i][j]==1:
            queue.append((i,j,0))

while(queue):
    i,j,c = queue.popleft()

    for k in range(4):
        ii = i+ll[k]
        jj = j+rr[k]
        if N>ii>=0 and M>jj>=0:
            if arr[ii][jj] == 0:
                arr[ii][jj]=1
                queue.append((ii,jj,c+1))
    if not queue:
        result = c

if zero(arr)>0:
    print(-1)
else:
    print(result)
