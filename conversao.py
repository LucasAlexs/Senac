salario1: float; salario2: float
nome1: str; nome2: str; sexo: str
idade: int

nome1 = input("Nome da primeira pessoa: ")
salario1 = float(input("Salário da primeira pessoa: "))

nome2 = input("Nome da segunda pessoa: ")
salario2 = float(input("Salário da segunda pessoa: "))

idade = int(input("Digite uma idade: "))
sexo = input("Digite um sexo (F/M): ")

#print(f"nome 1: {nome1}\nSalário 1: {salario1:.2f}\nNome 2: {nome2}\nSalário 2: {salario2:.2f}")
print(f"nome 1: {nome1}")
print(f"salário 1: {salario1:.2f}")
print(f"nome 2: {nome2}")
print(f"salario 2: {salario2:.2f}")
print(f"sexo: {sexo}")
print(f"idade: {idade}")