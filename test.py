def hanoi(a,b,c,n,arr):
    global count
    if(n==1):
        arr.append((a,c))
        count +=1
    else:
        hanoi(a,c,b,n-1,arr)
        arr.append((a,c))
        hanoi(b,a,c,n-1,arr)
        count +=1
t = int(input())
count = 0
arr= []
hanoi(1,2,3,t,arr)
print(count)
for i,j in arr:
    print(i,j)