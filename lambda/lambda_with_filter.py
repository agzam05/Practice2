#1
numbers=[1,2,3,4]
doubled=list(map(lambda x:x*2,numbers))
print(doubled)

#2
numbers=[1,2,3,4]
odd_numbers=list(filter(lambda x:x%2!=0, numbers))
print(odd_numbers)

#3
students=[("Agzam",18),("Alibek",17)]
sor=list(sorted(students, key=lambda x: x[1]))
print(sor)

#4
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
