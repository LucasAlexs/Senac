x_inform: int
x_inform = 0   

x_capacidade = int(input("INFORME A CAPACIDADE MÁXIMA DO RESTAURANTE: "))

'''------------------------------------------------------------------------------------------------'''

while True:
    
    print(" 1. Registrar chegada de clientes \n 2. Verificar se o restaurante o restaurante está lotado \n 3. Sair")
    x_opcao = int(input("Escolha a opção: "))

#------------------------------------------------------------------------------------------------

    if x_opcao == 3:
     print("Saindo do programa...")
     break

    if x_opcao == 1:
        x_inform = int(input("Informe o número de clientes que chegaram: "))

    if x_opcao == 2:
        x = (x_capacidade - x_inform)

        if x == 0:
           print("Restaurante lotado \n")
        elif x > 0:
           print(f"O restaurante ainda tem", x, "espaço ")

    if x_inform > x_capacidade:
       print("Clientes estão caindo fora")
    else:
        print(f"Opção errada digite a opção novamente: ")