n,m = map(int,input().split(' '))
g = [[] for x in range(m+1)]
for i in range(m):
    x,y=map(int,input().split(' '))
    g[x].append(y)
    g[y].append(x)

for i in range(n+1):
    print(str(i)+"--> ",end=" ")
    for j in range(len(g[i])):
        print(g[i][j],end=" ")
    print()

