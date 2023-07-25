from queue import PriorityQueue

N = int(input())

que_up = PriorityQueue()
que_down = PriorityQueue()

zero = False

for _ in range(N):
    S = int(input())
    if S>0:
        que_up.put(-1*S)
    elif S<0:
        que_down.put(S)
    elif S==0:
        zero=True

sum = 0

while not que_up.empty():
    a = que_up.get()
    if que_up.empty():
        sum+=-1*a
        break
    b = que_up.get()
    if a==-1 or b==-1:
        sum+=-1*(a+b)
    else:
        sum+=a*b

while not que_down.empty():
    a = que_down.get()
    if que_down.empty():
        if not zero:
            sum+=a
        break
    b = que_down.get()

    sum+=a*b

print(sum)