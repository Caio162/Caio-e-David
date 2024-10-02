login = input("Digite seu login: ")
senha = input("Crie uma senha (min. 8 caracteres, com letras e números): ")

if len(senha) < 8:
    print("A senha deve ter pelo menos 8 caracteres.")
elif senha.isalpha() or senha.isdigit():
    print("A senha deve conter letras e números.")
else:
    print("Senha válida!")