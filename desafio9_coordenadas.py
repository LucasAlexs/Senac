x: float; y: float

while True:

    print(f"Digite os valores das Coordenadas X e Y: ")
    x = float(input("Coordenada de X: "))
    y = float(input("Coordenada de Y: "))

    if x == 0 or y == 0:
     break
    if (x > 0 and y > 0):
        print(f"Quadrante 1")
    elif x < 0 and y > 0:
        print(f"Quadrante 2")
    elif x < 0 and y < 0:
        print(f"Quadrante 3")
    else:
        print(f"Quadrante 4")




""" 
    if x != 0 and y != 0:
     if (x > 0 and y > 0):
        print(f"Quadrante 1")
     elif x < 0 and y > 0:
        print(f"Quadrante 2")
     elif x < 0 and y < 0:
        print(f"Quadrante 3")
     else:
        print(f"Quadrante 4")
     break
     
"""