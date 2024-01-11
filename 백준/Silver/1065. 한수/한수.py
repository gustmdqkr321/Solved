def sol(n):
    global count
    check = True
    if(int(n) < 100):
        count += 1
        return
    sub = int(n[1]) - int(n[0])
    for i in range(2,len(n)):
        if(int(n[i]) - int(n[i-1]) != sub):
            check = False
            return
    if check:
        count += 1

t = input()
count = 0
for i in range(1,int(t)+1):
    sol(str(i))
print(count)