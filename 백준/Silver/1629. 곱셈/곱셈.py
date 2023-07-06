A, B, C = map(int,input().split())

def solve(i,j):
    if j == 0:
        return 1

    x = solve(i,j//2)
    if j%2==0:
        return int((x*x)%C)
    else:
        return int((x*x*i)%C)
        
print(int(solve(A,B)%C))