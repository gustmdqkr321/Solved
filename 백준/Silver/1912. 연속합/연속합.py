n = int(input())
nums = list(map(int,input().split()))
cur = 0
max = nums[0]
for i in nums:
    cur = cur + i
    if(cur > max):
        max = cur
    if(cur < 0):
        cur = 0
print(max)