#✅ Task: Write a Python program that takes a list of numbers and prints the square of each.
i=int(input("Enter the no: of numbers: "))
n=1
list=[]
while n<=i:
    item=int(input("Enter: "))
    list.append(item)
    n+=1
print(list)

for n in list:
    print(n**2,end=" ")