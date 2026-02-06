#The boolean_operators
a=True 
b=False
print(a and b)
print(a or b )
print(not a,not b)
#some basic examples
profit=int(input())
race=input()
print(profit>=1000000 and race=="Asian")

prof=input()
print(not (prof=="doctor"))

#some adavanced logic operators
a=True
b=False
print(a^b) #this is xor
print((a^b)==((a and not b) or (not a and  b))) #this is the def of the xor

a=True
b=False
imp=(not a) or b #this is an impication
print(imp)

a=True
b=False
eq=(a==b)
print(a==b) #This is the  equivalence
