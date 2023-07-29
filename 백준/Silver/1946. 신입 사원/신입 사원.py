import sys

T=int(sys.stdin.readline().rstrip())
for _ in range(T):
    N=int(sys.stdin.readline().rstrip())
    count = 0
    arr = []
    for _ in range(N):
        x,y = map(int,sys.stdin.readline().rstrip().split())
        arr.append((x,y))
    arr_sorted = sorted(arr)

    end = arr_sorted[0][1]
    for i in arr_sorted[1:]:
        if i[1] < end:
            end = i[1]
            count+=1
    print(count+1)

    