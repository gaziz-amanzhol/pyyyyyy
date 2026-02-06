#the basic of for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)
x=int(input())

for i in range(x):
  print(i,end=" ")
  #some example the basic

#from  summ1 to n
sum=0
n=int(input())
for i in range(n):
  sum+=i
print(sum)

# sum odd numbers
n=int(input())
for i in range(1,n,2):
  sum+=i
print(sum)
