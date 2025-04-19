def palindome(r):
    e=len(r)-1
    s=0
    while(s<e):
        if r[s]!=r[e]:
            return False
        s+=1
        e-=1
    return True
r=(1,2,3,4,5,4,3,2,13)

if palindome(r) is False:
    print("The tuple is a palindrome")
else:
    print("The tuple is not a palindrome")



a = (1,2,3,4,5,4,3,2,4)
x=a[::-1]
if a==x:
    print("The tuple is a palindrome")
else:
    print("The tuple is not a palindrome")







