#upper & lower

s="Iam so Good" #object that act as like remote. 
#here upper and lower are like button of remote that has it's own abilities
print(s.upper())
print(s.lower())

#find()...to find index of a letter if so in a string. 01234-->index
print(s.find('o'))
#'O'-->caps O is not prsnt. so return negative -1
print(s.find('O'))
#find 'so'
print(s.find('so'))

#Replace function

print(s.replace('so','too'))

#if no to be replaced one , then s remain the same
print(s.replace('what','23'))

#alternative for find 'in'

print('so' in s)