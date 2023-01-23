import random
list=[]
a= int(input("enter a random number ="))

for i in range(a):
    number=random.randint(3 , 33)
    list.append(number)
print(list)
