
class Person:
    species = "Humano"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Atributo protejido
        self._energy = 100
        # Atributo privado
        self.__password = "1234"

    def work(self):
        return f"{self.name} está trabajando mucho."

    # Metodo protejido
    def _waste_energy(self, quantity):
        self._energy -= quantity
        return self._energy

    def __generate_password(self):
        return f"$${self.name}{self.age}$$"


# Creo Obj
person1 = Person("Ignacio", 90)
person2 = Person("Laura", 40)

# Llamo metodos
print(person1.work())
print(person1._waste_energy(10))

# Intento ingresar al atributo privado
print(person1._Person__password)
print(person1._Person__generate_password())

print(person2.work())
