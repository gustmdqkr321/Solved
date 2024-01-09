a,b,v = map(int,input().split())
count = (v-a)//(a-b)
if((v-a)%(a-b) == 0):
    count = count +1
else:
    count = count +2
print(count)