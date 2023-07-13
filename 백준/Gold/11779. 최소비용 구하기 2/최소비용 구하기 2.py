from collections import deque
from queue import PriorityQueue

N = int(input())
M = int(input())

INF = 1e8
graph = [[] for _ in range(N+1)]
arr=[[INF,i] for i in range(N+1)]

for _ in range(M):
    start,end,distance = map(int,input().split())
    graph[start].append((end,distance))

s,e = map(int,input().split())

if s==e:
    print(0)
    print(1)
    print(s)
else:
    arr[s][0] = 0

    dq = PriorityQueue()

    dq.put((0,s))

    while not dq.empty():
        d,current = dq.get()
        if arr[current][0]<d:
            continue
        if (arr[e][0] < d) :
            continue
        

        for i in graph[current]:
            if d+i[1]<arr[i[0]][0]:
                arr[i[0]][0] = d+i[1]
                arr[i[0]][1] = current
                dq.put((d+i[1],i[0]))

    print(arr[e][0])

    tmp = e
    route = []
    while True:
        if tmp ==s:
            route.append(tmp)
            break
        route.append(tmp)
        tmp = arr[tmp][1]
    print(len(route))
    print(' '.join(map(str,route[::-1])))