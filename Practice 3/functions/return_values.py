def function():
  return "Hello from a function"

print(function())

def prime(x):
  for i in range(2,int(x**0.5)+1):
    if x%i==0:
      return "Not Prime"
  return "Prime"

print(prime(2))
a=prime(6)
b=prime(11)
print(a)
print(b)

def max(massiv):
  mx=massiv[0]
  for i in range(len(massiv)):
    if massiv[i]>mx:
      mx=massiv[i]
  return mx

massiv=[1,25,3,0]
print(max(massiv))

def swap(a,b):
  return b,a


a=1
b=2
a,b=swap(a,b)
print(a,b,sep=" ")
