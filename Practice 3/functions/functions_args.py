def Hello(name):
  print("Hello"+name)

Hello("Adilzhan")
Hello("Amanzhol")
Hello("Batman")

def pos(x):
  if x>0:
    print(x)
  else:
    print(-x)
 
pos(2)
pos(-3)

def distance(x1,y1,x2,y2):
  print(((x2-x1)**2+(y1-y2)**2)**0.5)

distance(1,2,4,6)

def max(a,b,c):
  mx=a
  if b>mx:
    mx=a
  if c>mx:
    mx=c
  print(mx)

max(1,2,3)
