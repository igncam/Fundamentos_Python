
def required_auth(func):
    def wrapper(user):
        if user == "Admin":
            return func(user)
        else:
            return "Acceso denegado"
    return wrapper


def admin_dashboard(user):
    return f"Bienvenido al panel, {user}"


auth_view_dashboard = required_auth(admin_dashboard)


print(auth_view_dashboard("Admin"))
print(auth_view_dashboard("Guest"))
