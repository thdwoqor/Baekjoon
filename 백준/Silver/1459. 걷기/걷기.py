X,Y,W,S = map(int,input().split())

result = (X+Y)*W

if (X+Y)%2==0:
    result = min(result,max(X,Y)*S)
else:
    result = min(result,(max(X,Y)-1)*S+W)


result = min(result,min(X,Y)*S+(max(X,Y)-min(X,Y))*W)

print(result)