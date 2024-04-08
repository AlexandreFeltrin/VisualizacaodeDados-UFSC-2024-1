frutas=["Maçã","Pessêgo","Laranja","Melancia","Melão","Pêra"]

frutas.sort(reverse=True)

print(frutas)

frutas.pop(1)

print(frutas)

frutas.append("Uva")
frutas.insert(0,"Banana")

print(frutas)
n=0

for i in range(0,len(frutas)-1):
    if(frutas[i]=="Morango"):
     n=1

if(n==1):
   print("A Lista possui Morango")
else:
   print("Não há morangos na lista")  
    
