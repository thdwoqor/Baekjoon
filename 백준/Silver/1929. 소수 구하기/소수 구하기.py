N,M=map(int,input().split())

arr = [False,False] + [True]*(1_000_000)

for i in range(2,M+1):
  if arr[i]:
    for j in range(i+i,M+1, i):
        arr[j] = False

for i in range(N,M+1):
   if arr[i]:
        print(i)

