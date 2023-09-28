'''Exemplo Terreno'''
comprimento: int; area: int; preco: int
largura: float; mQuadrado: float;
#
#
largura = float(input(f"Digite a largura do terreno: "))
comprimento = int(input(f"Digite o comprimento do terreno: "))
mQuadrado = float(input(f"Digite o valor do m^2 do terreno: "))
#
area = largura * comprimento
preco = area * mQuadrado 
#
print(f"Área do terreno: {area:.2f}")
print(f"Preço do terreno: {preco:.2f}")