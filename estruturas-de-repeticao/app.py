
def TotalSalarioHorasTrabalhadas():
    vlrHora = 0
    nmrHora = 0
    while True:
        vlrHora = float(input("Digite quanto ganha por hora: "))
        if(vlrHora > 0):
            break
        else:
            print("digite um valor maior que 0")
    
    while True:
        nmrHora = int(input("Digite a quantidade de horas trabalhadas no mês: "))
        if(nmrHora > 0):
            break
        else:
            print("digite um valor maior que 0")
    
    salario = vlrHora*nmrHora
    print(f"Você irá ganhar nesse mês: R$ {salario:.2f}")


def MaiorEMenorEntreTresNumeros():
    numero = int(input("Digite o 1º numero: "))
    maior = numero
    menor = numero
    for i in range(1,3):
        novoNumero = int(input(f"Digite o {i}º numero: "))
        if novoNumero > maior:
            maior = novoNumero
        if novoNumero < menor:
            menor = novoNumero
    
    print(f"O maior numero digitado foi: {maior}")
    print(f"O menor numero digitado foi: {menor}")


def ProdutoMaisBarato():
    listaDePrecos = []

    print("Digite três preços para saber qual é o melhor produto pra comprar")
    for i in range(1,4):
        preco = float(input(f"Digite o {i}º preço: "))
        listaDePrecos.append(preco)
    
    print(f"O melhor produto é o que tem o valor de {min(listaDePrecos)}")

# Faça um Programa que leia três números e mostre-os em ordem decrescente.
def NumerosEmOrdemDecrescente():
    # listaDeNumeros = [50,2,3,10,29,100,1]
    listaDeNumeros = [5,10,2]

    # print("Digite três numeros")
    # for i in range(1,4):
    #     numeroDigitado = int(input(f"Digite o {i}º numero: "))
    #     listaDeNumeros.append(numeroDigitado)
    
    print(f"Lista desordenada: {listaDeNumeros}")

    for i in range(len(listaDeNumeros)):
        for j in range(len(listaDeNumeros)):
            if(listaDeNumeros[i] > listaDeNumeros[j]):
                listaDeNumeros[i],listaDeNumeros[j] = listaDeNumeros[j],listaDeNumeros[i]

    print(f"Lista decrescente: {listaDeNumeros}")            

def NumerosEmOrdemDecrescenteOutroMetodo():
    # listaDeNumeros = [50,2,3,10,29,100,1]
    listaDeNumeros = [5,10,2]
    print(f"Lista desordenada: {listaDeNumeros}")

    for i in range(len(listaDeNumeros)):
        for j in range(len(listaDeNumeros)-1):
            if(listaDeNumeros[j] < listaDeNumeros[j+1]):
                listaDeNumeros[j], listaDeNumeros[j+1] = listaDeNumeros[j+1], listaDeNumeros[j]
    
    print(f"Lista decrescente: {listaDeNumeros}") 
