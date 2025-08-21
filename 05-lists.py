
list_numbers = [1, 2, 3, 2, 2, 4, 5]
list_letters = ['a', 'b', 'c']
list_mix = ["a", True, 1, [4, 2, 3]]

shopping_cart = ["Laptop", "Auriculares", "Teclado"]

print(type(list_letters))

# Metodos

# Append
print(list_numbers)
list_numbers.append(2)
print(list_numbers)

# remove el valor no el indice
list_numbers.remove(4)
print(list_numbers)

# count
print(list_numbers.count(2))
