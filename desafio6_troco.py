preco_p: float; quanti: float; dinheiroCliente: float; troco: float

preco_p = float(input(f"informe o preço do produto: "))
quanti = float(input(f"informe a quantidade do produto: "))
dinheiroCliente = float(input(f"informe o seu dinheiro: "))

troco = dinheiroCliente - preco_p * quanti

if dinheiroCliente > troco:
    print(f"Você deverá: {troco}")
else:
    print(f"Seu troco: {troco}")
