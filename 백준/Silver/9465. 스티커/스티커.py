T=int(input())
for _ in range(T):

    n=int(input())
    sticker=[list(map(int,input().split())) for _ in range(2)]
    point=[[0 for _ in range(n)] for _ in range(2)]
    if n==1:
        print(max(sticker[0][0],sticker[1][0]))
        continue
    point[0][0]=sticker[0][0]
    point[1][0]=sticker[1][0]
    point[0][1]=sticker[0][1]+point[1][0]
    point[1][1]=sticker[1][1]+point[0][0]


    for i in range(2,n):
        point[0][i]=max(point[1][i-2],point[1][i-1])+sticker[0][i]
        point[1][i]=max(point[0][i-2],point[0][i-1])+sticker[1][i]
    print(max(max(point[0][-1],point[1][-1]),max(point[0][-2],point[1][-2])))