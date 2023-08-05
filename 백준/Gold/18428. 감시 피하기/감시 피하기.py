N = int(input())

graph = [ list(input().split()) for _ in range(N)]

result = False

teacher =[]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(N):
     for j in range(N):
          if graph[i][j]=="T":
               teacher.append((i,j))

def result():
    # for i in graph:
    #     print(i)
    # print("#######")
    for i,j in teacher:
        for k in range(4):
            ii = i
            jj = j
            while True:
                ii += dx[k]
                jj += dy[k]
                if not (0<=ii<N and 0<=jj<N):
                    break
                if graph[ii][jj]=="S":
                    return True
                if graph[ii][jj]=="O":
                    break
    return False

for a in range(N*N-2):
    if graph[a//N][a%N] == "S" or graph[a//N][a%N] == "T":
         continue
    for b in range(a+1,N*N-1):
        if graph[b//N][b%N] == "S" or graph[b//N][b%N] == "T":
            continue
        for c in range(b+1,N*N):
                if graph[c//N][c%N] == "S" or graph[c//N][c%N] == "T":
                    continue
                graph[a//N][a%N]="O"
                graph[b//N][b%N]="O"
                graph[c//N][c%N]="O"

                if not result():
                     print("YES")
                     exit()

                graph[a//N][a%N]="X"
                graph[b//N][b%N]="X"
                graph[c//N][c%N]="X"


print("NO")