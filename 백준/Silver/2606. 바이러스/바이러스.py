def dfs(v):
    visit[v] = 1
    for i in graph[v]:
        if(visit[i] == 0):
            # visit[i] = 1
            dfs(i)


com = int(input())
con = int(input())
graph = [[] for _ in range(com)]
visit = [0 for _ in range(com)]
for _ in range(con):
    a,b = map(int,input().split())
    a -=1
    b -=1
    graph[a].append(b)
    graph[b].append(a)
visit[0] = 1
dfs(0)
count = 0
for i in visit[1::]:
    if(i == 1):
        count +=1
print(count)