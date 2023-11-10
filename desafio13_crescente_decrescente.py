x: int; 

while True:

    x = int(input(f"digite dois números: \n"))
    y = int(input(f""))
    
    if x == y:
        
        break
    if x > y:
        print("Decrescente!!")
    elif x < y:
        print("Crescente!!")