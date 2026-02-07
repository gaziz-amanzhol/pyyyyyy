#if_elif_else basic 
a=int(input(("enter the first number")))
b=int(input("enter the second number"))
if(a>b):
    print("a is more than b")
elif a<b:
    print("a is less than b")
else:
    print("a is equal to the b")
#some basic example
x1,y1=map(int,input("enter the first cord").split())
x2,y2=map(int,input("enter the second cord").split())
if ((x1==x2) and (abs(y1-y2))==1) or ((y1==y2) and (abs(x1-x2))==1):
    print("This is the Kings move")
elif ((abs(x1-x2))==abs(y1-y2)):
    print("it could be the bishop or queen")
elif ((x1==x2) or (y1==y2)):
    print("this is the rook or queen")
else:
    print("I am a Messi") #GOAT
