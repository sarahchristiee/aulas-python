senha = "123"

while True:
    tentativa = input("Digite a senha: ")
    if tentativa != senha:
        print("Senha Incorreta!")
    else:
        print("Senha Correta!")
        break