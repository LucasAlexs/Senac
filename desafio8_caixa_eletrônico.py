saldo_d: int; saque: int; resto: int 

saque = int(input(f"Valor do saque: "))
saldo_d = 1000
if saque <= saldo_d:
    resto = saldo_d - saque
    print(f"Saldo restante para saque: {resto}")
else:
    print(f"Saldo indiponível para saque, saldo disponível para saque: {saldo_d}")