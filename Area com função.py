base=int(input("Digite a base para calcular a area: "))
altura=int(input("Digite a altura para calcular a area: "))


def area (base,altura):
    total=base*altura
    return total
print("Area do terreno: ",area(base,altura))