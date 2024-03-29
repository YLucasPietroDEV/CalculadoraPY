#Função soma
def somar(a, b):
    return a + b
#Função subtração
def subtrair(a, b):
    return a - b
#Função Dividir, com filtro de erro para nao existir divisão por 0
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"
#Função Multiplicação
def multiplicar(a, b):
    return a * b
#Função principal do codigo
def main():
    print("Calculadora")
        
    escolha = input("Digite o número da operação desejada\n1. Somar\n2. Subtrair\n3. Dividir\n4. Multiplicar\n:")
    
    while True:  # Loop para garantir que o usuário insira um número válido
        try:
            num1 = float(input("Digite o Primeiro número: "))
            num2 = float(input("Digite o Segundo número: ")) 

            if escolha == '1':
                print("Resultado: ", somar(num1, num2))
            elif escolha == '2':
                print('Resultado: ', subtrair(num1, num2))
            elif escolha == '3':
                print('Resultado: ', dividir(num1, num2))
            elif escolha == '4':
                print('Resultado: ', multiplicar(num1, num2))
            else:
                print("Escolha inválida")
            break  # Se os números forem válidos, saia do loop
        except ValueError:
            print("Erro: Por favor, digite um número válido.")
#Looping para fazer outras operações, ele chama a função principal até que o usuario escolha sair
while True:
    if __name__ == "__main__":
        main()
        
    refazer = input("Deseja fazer outra conta?\n(sim/não)")
    if refazer.lower() != "sim":
        break

print("Fim do programa")
