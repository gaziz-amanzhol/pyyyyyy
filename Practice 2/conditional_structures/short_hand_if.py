#short_hand_if basic
a=111
if a>100: print("a is greater than 100")
a=123
result=("more" if a>100 else "less")
print(result)

#some basic examples

#maxi
a=int(input())
b=int(input())
print(a if a>b else b)

#even or odd
n=int(input())
print("even" if n%2==0 else "odd")

#pos or neg
n=int(input())
print("positive" if n>0 else ("negative" if n<0 else "zero"))
