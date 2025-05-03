a={1,2,3,4,5,6,7,8,9,10}
b={'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
comb=list(zip(a,b))
print(comb)


a=[1,2,3,4,5,6,7,8,9,10]
b=[11,22,33,44,55,66,77,88,99,100]
for i,j in zip(a,b[::-1]):
    print(i,j)


stock=["reliance", "hdfc", "icici"]  
price=[1000,2000,3000] 
dict={price:stock for stock,price in zip(stock,price)}
print(dict)
 


