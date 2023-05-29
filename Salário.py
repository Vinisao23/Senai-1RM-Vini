sal=float(input("\nDigite seu salário: "))

if sal > 8250.00:
    ausal=round (sal*0.10,2)
    nvsal=ausal+sal
    print("\nSeu aumento de salário é: ", nvsal,"\n")
elif sal  <=8250.00:
    ausal1=round(sal*1.15,2)
    print("\nSeu aumento de salário é: ", ausal1,"\n")