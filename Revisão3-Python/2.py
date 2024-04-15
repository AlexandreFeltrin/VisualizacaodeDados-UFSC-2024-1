notas={"João":8,"Maria":6.5,"Laura":9,"José":7.5}
nome=""
nota=0

while True:
    print("1. Cadastar novo aluno")
    print("2.Visualizar notas")
    print("0. Sair")
    
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print("Digite o nome do aluno:")
        nome=input()
        print("Digite a nota: ")
        nota=int(input())
        notas[nome]=nota
    elif escolha == "2":
        print(notas)
    
    elif escolha == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.")


print(notas["João"])
print("--------------------------")

del notas["João"]

for x,y in notas.items():
  print(x,y)



