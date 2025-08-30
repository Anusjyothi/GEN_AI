#Weight converter

weight=float(input("Weight: "))
units=input("(K)g or (L)bs: ")

if 'l' in units or 'L' in units:
    weight=weight/0.45
    print("Weight in kg: "+str(weight))
else:
    weight=weight*0.45
    print("Weight in lbs: "+str(weight))



