N = int(input())
n_arry = list(map(int,input().split()))
n_arry.sort()
M = int(input())
m_arry = list(map(int,input().split()))

for i in m_arry:
    if i in n_arry:
        print(1)
    else:
        print(0)