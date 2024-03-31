
n=int(input("Digite um número: "))
count=0;
for i in range (2,n):
    if(n%i==0):
        count+=1
    
if(count==0):
    print("É um numero primo");
else:
    print("Não é primo");