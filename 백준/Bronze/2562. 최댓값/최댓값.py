arr=[]
for _ in range(9):
    arr.append(int(input()))

M = max(arr)

print(M)
print(arr.index(M)+1)