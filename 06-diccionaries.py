
user = {
    "name": "Ignacio",
    "age": 29,
    "email": "ignacio@mail.com",
    "active": True,
    (19.12, -31.33): "Argentina"
}

user["active"] = False
user["age"] = 31
user["country"] = "Buenos Aires"

print(user[(19.12, -31.33)])

print(user)
