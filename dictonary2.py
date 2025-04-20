dict={"codangle":1, "python":2, "java":3, "c++":1, "javascript":5, "html":6, "css":7, "ruby":1, "swift":1, "kotlin":10}
print("The elements in the dictionary are: ", dict)  
str(dict)
a=1
count=0
for i in dict:
    if dict[i]==a:
        count=count+1
print("The number of elements in the dictionary with value 1 are: ", count)
