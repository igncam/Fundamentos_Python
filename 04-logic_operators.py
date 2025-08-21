
# AND
age = 25
licensed = True

if age >= 18 and licensed:
    print("Puedes manejar")

# OR
is_student = False
membership = True

if is_student or membership:
    print("Obtiene precio especial.")

# NOT
is_admin = False
if not is_admin:
    print("Accesso denegado")

# Short circuiting

name = False
print(name and name.upper())
