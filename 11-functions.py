# # Parametros
# def hello(greet="Hello", name="Guest"):
#     print(f"{greet}, {name}")


# # Argumentos
# hello("Hola", "Ignacio")
# hello("Hola", "Mario")
# hello()

# hello(name="Ted", greet="Hello")

def big_function(*args, **kwargs):
    print(args)
    print(kwargs)
    return kwargs


print(big_function(1, 2, 3, 4, 5, 6, num1=300))
