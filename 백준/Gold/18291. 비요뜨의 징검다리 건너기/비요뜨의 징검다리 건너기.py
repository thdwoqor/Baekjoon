INF = (10**9+7)

T  = int(input())

def solve(i,j):
    result = 1
    while j>0:
        if j%2 == 1:
            result = (result * i) % INF
        i = i*i%INF
        j //=2
    return result

for _ in range(T):
    N  = int(input())
    print(solve(2,N-2))


# 1 1
# 2 1
# 3 2
# 4 4
# 5 8