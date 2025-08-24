
def divide_numbers():
    try:
        a = int(input("Ingresa el numerador: "))
        b = int(input("Ingresa el denominador: "))

        result = a / b
        print(result)
        return result

    except ZeroDivisionError:
        print("No se puede entre 0.")

    except ValueError:
        print("Por favor, ingresa solo números.")

    except Exception as error:
        print(type(error))

    else:
        pass

    finally:
        print(f"Gracias por usar nuesrta calculadora:")


divide_numbers()
