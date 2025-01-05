import re

def check_email(email):
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$', email):
        return True
    return False

email = input("Introduce tu email: ")
if check_email(email):
    print("El email es válido:", email)
else:
    print("Email no válido")



