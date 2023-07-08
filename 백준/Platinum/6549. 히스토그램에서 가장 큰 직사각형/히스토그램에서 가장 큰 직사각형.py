from collections import deque

s = deque()

while True:
    i = input()
    if i == "0":
        break
    arr = list(map(int,i.split()))
    stack = deque()
    result = 0

    for i,hight in enumerate(arr):
        if i==0:
            continue
        index = i
        while stack and stack[-1][1] >= hight:
            x,y = stack.pop()

            index = x
            w = i-index
            result = max(result,w*y)

        stack.append((index,hight))
    
    while stack:
        x,y = stack.pop()
        result = max(result,(arr[0]-x+1)*y)
    print(result)