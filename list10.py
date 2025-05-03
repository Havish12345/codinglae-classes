a=[1,2,3,4,5,6,7,8,9,10]
num=[x for x in a if x%2==0]
print(num)



def s(a):
    return a ** 10

a=(1,2,3,4,5,6,7,8,9,10)
num=map(s,a)
print(list(num))


dict={str(x):x**2 for x in range(1,11)}
print(dict)


