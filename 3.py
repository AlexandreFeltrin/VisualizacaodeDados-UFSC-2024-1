n1=int(input("Digite o número 1 : "));
print("");
n2=int(input("Digite o número 2 : "));
print("");
n3=int(input("Digite o número 3 : "));

if(n1>n2):
    if(n2>n3):
        print("O maior é ",n1);
else:
    if(n2>n3):
        if(n3>n1):
            print("O maior é ",n2);
    else:
        if(n3>n2):
            if(n2>n1):
                print("O maior é ",n3);
            else:
                if(n1==n2==n3):
                    print("Os números são iguais");