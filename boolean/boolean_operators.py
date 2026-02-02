#1
x=["apple", "banana"]
y=["apple", "banana"]
z=x
print(x is z)
print(x is y)
print(x==y)

#2
x=["apple", "banana"]
y=["apple", "banana"]
print(x is not y)

#3
x=[1, 2, 3]
y=[1, 2, 3]
print(x==y)
print(x is y)

#4
fruits=["apple", "banana", "cherry"]
print("banana" in fruits)

#5
fruits=["apple", "banana", "cherry"]
print("pineapple" not in fruits)

#6
text="Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)