
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        return f"{self.name} está trabajando mucho."


# Creao Obj
person1 = Person("Ignacio", 90)
person2 = Person("Laura", 40)

# Llamo metodos
print(person1.work())
print(person2.work())
