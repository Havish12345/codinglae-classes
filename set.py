my_set={1,2,3,4,4}
print(my_set)
my_set={"hello",1,(1,2,3)}
print(my_set)
my_set=set([1,2,3])
print(my_set)
my_set={12345,1,2,3}
print(my_set)
my_set.pop()
print(my_set)   


my_set={1,2,3,4}
your_set={9,8,7,4}
all_set=my_set & your_set
print(all_set)
all_set=my_set | your_set
print(all_set)
all_set=my_set - your_set
print(all_set)