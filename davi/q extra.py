cor = int(input("digite uma cor verde vermelho amarelo")).lower().strip()

if  cor == "verde":
    print ("acelere")
elif cor == "amarelo":
    print ("cuidado")
elif cor == "vermelho":
    print ("pare")

else:
    print ("cor invalida")
