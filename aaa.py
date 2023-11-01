def calcular_media_idade():
    s = 0
    q = 0
    idade = int(input(f"digite a idade: "))
    while idade >= 0:
        s += idade
        q += 1
        idade = int(input(f"digite a idade: "))
    if q <= 0:
        print("impossivel calcular")
    else:
        media = s / q
        print(media)

calcular_media_idade()
