test = input()
croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in croa:
    test = test.replace(i, 'a')
print(len(test))
