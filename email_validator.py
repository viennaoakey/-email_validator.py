import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9]+([._]?[a-zA-Z0-9]+)*@[a-zA-Z0-9]+([.-]?[a-zA-Z0-9]+)*(\.[a-zA-Z]{2,})+$'
    if re.match(pattern, email):
        return True
    else:
        return False

email = input("Введите email-адрес для проверки: ")
if validate_email(email):
    print("Email-адрес действительный")
else:
    print("Email-адрес недействительный")
