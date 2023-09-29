import math
#
#base: float; altura: float; area: float; perimetro: float; diagonal: float
#
base = float(input(f"Escreva a base: "))
altura = float(input(f"Escreva a altura: "))
#
area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(math.pow(base,2) + math.pow(altura,2))
#
print(f"Area: {area:.2f}")
print(f"Perimetro: {perimetro:.2f}")
print(f"Diagonal: {diagonal:.2f}")