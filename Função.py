print("1 Soma")
print("2 Subtração")

pergunta =int (input("Selecione a operação: "))

num1=int(input("Digite o primeiro numero: "))
num2=int(input("Digite o segundo numero: "))

if pergunta == 1:
    def somar(num1,num2):
        total = num1+num2   
        return total
    print("Soma: ",somar(num1,num2))
if pergunta == 2:
    def sub(num1,num2):
        total = num1-num2   
        return total
    print("Subtração: ",sub(num1,num2))