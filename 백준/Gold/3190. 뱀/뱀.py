from collections import deque


N = int(input())
K = int(input())

borad = [[[0] for _ in range(N+1)] for _ in range(N+1)]

for _ in range(K):
    x,y = map(int,input().split())
    borad[x][y]=1

L = int(input())

queue = []
for _ in range(L):
    x,c = input().split()
    queue.append((x,c))

snake = deque()
snake.append((1,1))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

direction = {"R":3,"L":2,"D":1,"U":0}
now = "R"
convert = {
    ("R","D"):"D",
    ("R","L"):"U",
    ("D","D"):"L",
    ("D","L"):"R",
    ("L","D"):"U",
    ("L","L"):"D",
    ("U","D"):"R",
    ("U","L"):"L"
    }
time = 0
index = 0
now_x=1
now_y=1

while True:
    if index<len(queue) and time==int(queue[index][0]):
        now = convert[(now,queue[index][1])]
        index+=1

    dxx = now_x + dx[direction[now]]
    dyy = now_y + dy[direction[now]]

    # 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
    if not (0<dxx<=N and 0<dyy<=N) or (dxx,dyy) in snake:
        print(time+1)
        break

    # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
    snake.appendleft((dxx,dyy))
    
    if borad[dxx][dyy]!=1:
        snake.pop()
    else:
        borad[dxx][dyy]=0
    now_x=dxx
    now_y=dyy

    time+=1
