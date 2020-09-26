from email_validator import validate_email, EmailNotValidError # pip install email_validator

email = input("Digite um e-mail: ")

try:
    validate_email(email)
    print("E-mail válido")
except EmailNotValidError as e:
    print(f"E-mail inválido {e}")