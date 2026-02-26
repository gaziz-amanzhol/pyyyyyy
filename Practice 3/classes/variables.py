class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

x= Person("Adilzhan", 18)
print(x.age)

x.age = 26
print(x.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

y = Person("Messi", 39)

del y.age

print(y.name)
