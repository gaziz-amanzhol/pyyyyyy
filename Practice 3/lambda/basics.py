x = lambda a : a + 1000
print(x(5))

x = lambda a, b : a * b
print(x(2,3))

x = lambda a, b, c : a + b + c
print(x(1, 6, 2))

x=lambda name : "name is "+name
print(x("Akylbek"))

x=lambda a,b : a if a>b else b
print(x(1,2))

x=lambda mas: max(mas)
print(x([1,5,3,94]))
