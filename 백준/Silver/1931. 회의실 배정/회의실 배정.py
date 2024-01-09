n = int(input())
meet = []
for _ in range(n):
    a,b = map(int,input().split())
    meet.append([a,b])

meet.sort(key=lambda x:x[0])
meet.sort(key=lambda x:x[1])
count = 1
cur_fin = meet[0][1]
for i in range(1,n):
    if(meet[i][0] >= cur_fin):
        count+=1
        cur_fin = meet[i][1]
print(count)
