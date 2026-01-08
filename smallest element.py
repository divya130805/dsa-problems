import array as ar
arr=ar.array('i',[1,2,3,4,5,6,7,8,9])
print(arr)
smallest=arr[0]
for x in arr:
    if x<smallest:
        smallest=x
print("the smallest value is :",x)
