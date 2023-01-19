#Reading the class in another file for clean writing
from classs import person

#The attribute of each person
person1 = person("Ali", 22, "whait","Iran")
person2 = person("Michael",29,"black","United States")

#print attribute 
print(person1.name)
print(person1.age)
print(person1.country)
print(person1.colorskin)
print(person2.name)
print(person2.age)
print(person2.country)
print(person2.colorskin)
