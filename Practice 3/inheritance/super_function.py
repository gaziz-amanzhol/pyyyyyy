class Person:
  def __init__(self, fname, lname,age,country):
    self.firstname = fname
    self.lastname = lname
    self.age=age
    self.country=country

  def getinfo(self):
    print(self.firstname, self.lastname, self.age,self.country)

class Student(Person):
  def __init__(self, fname, lname,age,country):
    super().__init__(fname, lname,age,country)

  def info(self):
    print(self.firstname, self.lastname, self.age,self.country)

x=Student("Amanzhol","Adilzhan",18,"KAZ")
x.info()
