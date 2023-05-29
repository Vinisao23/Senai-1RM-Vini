num1= int(input("Qual numero você quer saber a tabuada: "))

for count in range(10):
    print("{} * {} = {}" .format(num1, count+1, num1*(count+1)) )