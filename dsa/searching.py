import array as arr
ar=arr.array('i',[1,2,3,4,5,6,7,8,9,0])
print(ar)
search=8
for x in ar:
    if(search==x):
         print(x)
print("the element was found:")