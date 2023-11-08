valor: int;

valor = int(input(f"deseja a tabuada para qual valor? "))

produto = 10

for i in range(produto):
    produto = valor * i
    print(f"{valor} X {i} = {produto}")
