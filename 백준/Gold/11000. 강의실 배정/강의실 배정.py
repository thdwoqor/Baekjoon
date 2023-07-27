
import heapq

N = int(input())

arr = []
que = []

for _ in range(N):
    S,T=map(int,input().split())
    arr.append((S,T))

arr.sort()

heapq.heappush(que, arr[0][1])

for i in range(1,N):
    if arr[i][0] < que[0]:
        heapq.heappush(que, arr[i][1])
    else:
        heapq.heappop(que)
        heapq.heappush(que, arr[i][1])

print(len(que))
