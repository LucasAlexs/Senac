senha = 2002

x = int(input(f"Digite a senha: "))

while True:
    if x == senha:
        print("Acesso permitido!!")
        break
    elif x != senha:
        x = int(input("senha invalida! tente novamente:"))
