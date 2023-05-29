print("FUNÇÕES\n")

print("1 Soma\n")
print("2 Multiplicação\n")
print("3 Maior Numero\n")
print("4 Menor Numero\n")

res=int (input("Qual função você quer fazer??? "))

if res==1:
    num1=int(input("Digite o primeiro numero: "))
    num2=int(input("Digite o segundo numero: "))
    def somar(num1,num2):
        total = num1+num2   
        return total
    print("Soma: ",somar(num1,num2))
if res==2:
    num1=int(input("Digite o primeiro numero: "))
    num2=int(input("Digite o segundo numero: "))
    def multi(num1,num2):
        total = num1*num2   
        return total
    print("Multiplicação: ",multi(num1,num2))
if res==3:
    num1=int(input("Digite o primeiro numero: "))
    num2=int(input("Digite o segundo numero: "))
    def maior(num1,num2):
        nummaior = max (num1,num2)
        print("Maior Numero: ",nummaior)
    maior(num1,num2)
if res==4:
    num1=int(input("Digite o primeiro numero: "))
    num2=int(input("Digite o segundo numero: "))
    def menor(num1,num2):
        nummenor = min (num1,num2)
        print("Menor Numero: ",nummenor)
    menor(num1,num2)