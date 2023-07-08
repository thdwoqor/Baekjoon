from queue import PriorityQueue

INF = 1e8

N,M,X = map(int,input().split())

graph = [[] for _ in range(N+1)]

graph2 = [[] for _ in range(N+1)]


for _ in range(M):
  u, v, w = map(int, input().split())  
  graph[u].append((v, w))  
  graph2[v].append((u, w))  

result = 0

def dijkstra(start,a):
    distance = [INF] * (N+1)

    pq = PriorityQueue()
    pq.put((0, start))
    distance[start] = 0

    while not pq.empty():
        dist, now = pq.get()

        if distance[now] < dist:
            continue
        
        for i in a[now]:
            if dist+i[1] < distance[i[0]]:
                distance[i[0]] = dist+i[1]
                pq.put((dist+i[1],i[0]))
    return distance

a = dijkstra(X,graph)
b = dijkstra(X,graph2)

for i in range(1,N+1):
    if a[i] == INF or b[i] == INF:
        continue
    result = max(result,a[i]+b[i])

print(result)