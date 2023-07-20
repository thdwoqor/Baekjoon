from queue import PriorityQueue
from sys import stdin

N = int(stdin.readline())

que = PriorityQueue()

for _ in range(N):
    que.put(int(stdin.readline()))

result = 0

if N==1:
    print(0)
else:
    while not que.empty():
        a = que.get()
        b = que.get()
        result += a+b
        
        if que.empty():
            break

        que.put(a+b)

    print(result)