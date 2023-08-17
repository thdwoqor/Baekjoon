N = int(input())
arr = list(map(int,input().split()))
M = int(input())
arr.sort()

def binary_search(start,end):
    global arr, M

    if start>end:
        print(end)
        return

    min = (start+end)//2

    s = 0
    for i in arr:
        if i>=min:
            s+=min
        else:
            s+=i
    
    if s>M:
        binary_search(start,min-1)
    elif s<M:
        binary_search(min+1,end)
    else:
        print(min)
        return

if sum(arr)<=M:
    print(max(arr))
else:
    binary_search(1,max(arr))