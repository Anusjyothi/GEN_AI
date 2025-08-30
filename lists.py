names=["aisu", "anu", "mary", "john"]
print(names)
print(names[0],names[3],names[-1])
#replace
names[0]="blessy"
print(names)
#selective of first 3 only
print(names[0:3])
print(names)

#list methods

#append()
numbers=[1,3,5,7,9]
numbers.append(11)
print(numbers)

#insert()
numbers.insert(0,-1)
print(numbers)

#remove()
numbers.remove(5)
print(numbers)

#to clear all in numbers
numbers.clear()
print(numbers)
numbers.append(5)
print(5 in numbers)
print(4 in numbers)

#length
print(len(numbers))
numbers.append(18)
print(len(numbers))