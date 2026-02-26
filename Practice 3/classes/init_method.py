class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Penaldo", 41)

print(p1.name)
print(p1.age)

class Person:
  pass

p1 = Person()
p1.name = "Adilzhan"
p1.age = 18

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Max", 28)

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Messi")
p2 = Person("Suarez", 39)

print(p1.name, p1.age)
print(p2.name, p2.age)

class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Messi", 38, "Rosarino", "Argentina")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
