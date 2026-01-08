import array as ar
arr=ar.array('i',[1,2,3,4,5,6,7,8,9])
print(arr)
total=0
for i in arr:
    if (i%2!=0):
        total=total+i
print(total)

