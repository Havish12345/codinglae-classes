
amount=1599

rupee_100=(amount//100)
rupee_50=(amount%100)//50
rupee_10=((amount%100)%50)//10
rupee_1=(((amount%100)%50)%10)//1

print(rupee_100)
print(rupee_50)
print(rupee_10)
print(rupee_1)