def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: divisão por zero!"
    else:
        return x / y


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nEscolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")


opcao = input("Digite o número da operação desejada: ")


if opcao == '1':
    print("Resultado da adição:", adicao(num1, num2))
elif opcao == '2':
    print("Resultado da subtração:", subtracao(num1, num2))
elif opcao == '3':
    print("Resultado da multiplicação:", multiplicacao(num1, num2))
elif opcao == '4':
    print("Resultado da divisão:", divisao(num1, num2))
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")
