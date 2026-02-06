#for loop comtinue
x="Adilzhan"
cnt=0
for i in x:
    if i.islower():
        cnt+=1
    elif i.isupper():
        continue
print(cnt)

#some basic example

#print only odds
for i in range(1,8):
    if i%2==0:
        continue
    print(i)

#skip A,a
name="Adilzhan"
for i in name:
    if i=="A" or i=="a":
        continue
    print(i,end=" ")