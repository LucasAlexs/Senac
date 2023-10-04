saldo_d: int; saque: int 

saque = int(input(f"Valor do saque"))

if saque <= 1000:
    print(f"Saldo disponível para saque")
else:
    print(f"Saldo indiponível para saque")