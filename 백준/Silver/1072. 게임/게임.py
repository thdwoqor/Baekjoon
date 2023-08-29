import math

X,Y = map(int,input().split())
Z = math.floor(100*Y/X)

if X==Y or Z==99:
    print(-1)
else:
    def binary_search(start, end):
        global Z,Y,X
        
        mid = (start+end)//2
        if start>end:
            return end
        
        ZZ = math.floor(100*(Y+mid)/(X+mid))

        if ZZ==Z:
            return mid
        elif ZZ>Z:
            return binary_search(start,mid-1)  
        elif ZZ<Z:
            return binary_search(mid+1,end)
            
    N = binary_search(1,X*2)

    while True:
        ZZZ = math.floor(100*(Y+N)/(X+N))

        if ZZZ!=Z:
            print(N)
            break
        N=N+1
