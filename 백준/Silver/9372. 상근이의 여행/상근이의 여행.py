from sys import stdin

class Adjacencylist:
    def __init__(self, node:int, edge:int, adj):
        self.node = node
        self.edge = edge
        self.adj = adj
        self.visit = [0  for _ in range(node+2)]

    def prt(self):
        for i in range(1,self.node+1):
            print('*',i,*self.adj[i])

    def solve(self):
        return self.node-1
            

                

T=int(input())
for _ in range(T):
    node, edge = map(int, stdin.readline().split())
    adj = [ [] for _ in range(node+2)]

    for _ in range(edge):
        src, dest = map(int, stdin.readline().split())
        adj[src].append(dest)
        adj[dest].append(src)
        
    adjList = Adjacencylist(node, edge, adj)

    # adjList.prt()
    print(adjList.solve())
