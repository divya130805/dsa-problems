import array as ar
arr=ar.array('i',[1,2,3,4,5,5,6,7,8])
print(arr)
count=0
for i in arr:
    count=count+1
    print(count)
print( "the total count is :",count)