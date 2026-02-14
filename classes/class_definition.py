#1
class MyClass:
  x = 5

print(MyClass)

#2
class Myclass:
  x=5
p1=Myclass()
print(p1.x)

#3
class Person:
  pass

#4
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1

print(p1)
