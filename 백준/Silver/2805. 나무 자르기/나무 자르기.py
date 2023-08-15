import math

N,M = map(int,input().split())
arr = list(map(int,input().split()))
# arr.sort()

def binary_search(start,end):
    global M
    if start > end:
        return end
    mid = (start+end)//2

    s = 0
    for i in arr:
        if i>=mid:
            s+=i-mid

    if s>=M:
        return binary_search(mid+1,end)
    else:
        return binary_search(start,mid-1)


print(binary_search(1,max(arr)))



