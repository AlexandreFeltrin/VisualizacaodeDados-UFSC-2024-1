frase="Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam"

letras=set()

frase=frase.lower()
frase=frase.replace(" ", "")
frase=frase.replace(".","")
frase=frase.replace(",","")

print()
print(frase)

for letra in frase:
    letras.add(letra)
        
print("-------------------------------------------------------------------------------------------------------------------------------------")
print(letras)
print("-------------------------------------------------------------------------------------------------------------------------------------")

print(sorted(letras))