from collections import deque


N,K = map(int, input().split())

queue = deque()
visit = [-1]*100_001

queue.append((N,0))

if N<=K:
    while queue:
        location,time = queue.popleft()

        if location == K:
            print(time)
            break

        visit[location] = 1


        for j,i in enumerate([location*2,-1+location,1+location]):
            if 0<=i<=100_000 and visit[i]==-1:
                if j==0:
                    queue.append((i,time))
                else:
                    queue.append((i,time+1))
else:
    print(N-K)