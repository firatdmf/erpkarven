from datetime import date
x = date.today()
print(x)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        # below two are the same thing
        # return("{}{}".format(self.name,self.age))
        return(f"{self.name}{self.age}")

    def introduce_self(self):
        return f'Hello my name is {self.name}, and my age is {self.age} '
    

p1 = Person("Firat",25)
# print("Name: {}, Age: {}".format(p1.name,p1.age))
print("Hello World")
print(p1)
print(p1.introduce_self())


def frt(input):
    return input

