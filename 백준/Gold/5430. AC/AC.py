from collections import deque
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    error = False
    command = list(sys.stdin.readline().rstrip())
    count = int(sys.stdin.readline().rstrip())

    direction= -1

    if count == 0:
        sys.stdin.readline()
        arr = deque()
    else:
        arr = deque(deque(sys.stdin.readline().rstrip()[1:-1].split(",")))
    
    for i in command:
        if i == "R":
            direction = direction*-1
        if i == "D":
            if not arr:
                error = True
                break
            else:
                if direction == -1:
                    arr.popleft()
                else:
                    arr.pop()

    if error:
        print("error")
    else:
        if direction == 1:
            arr.reverse()
        print(f"[{','.join(list(arr))}]")

# 1
# R
# 0
# []