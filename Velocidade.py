vel=int(input("\nDigite sua velocidade: "))

if vel>80:
    print("\n",vel,"km/h")
    print("\nVocê foi MULTADO!!!\n")
elif vel<=80:
    print(vel,"km/h")