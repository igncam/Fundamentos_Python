try:
    # Escribir
    with open('test.txt', mode="w") as my_file:
        text = my_file.write(":) ")
    # Leer
    with open('test.txt', mode="r") as my_file:
        print(my_file.readlines())
    # Leer y escribir
    with open('test.txt', mode="r+") as my_file:
        print(my_file.readlines())
        text = my_file.write("Hola mundo")
    # apped
    with open('test.txt', mode="a") as my_file:
        text = my_file.write("123")
        print(text)
except FileNotFoundError:
    print(f"El archivo no existe.")
except Exception as err:
    print(f"Ocurrió un error: {err}")
