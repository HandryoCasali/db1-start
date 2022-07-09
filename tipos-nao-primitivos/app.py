def SomarItensLista():
    listaDeNumeros = [10, 5, 3, 7, 19, 3]

    print( sum(listaDeNumeros) )

def MultiplicarItensLista():
    listaDeNumeros = [10, 5, 3, 7, 19, 3]

    multiplicador = 2
    for indice, valor in enumerate(listaDeNumeros):
        listaDeNumeros[indice] = valor * multiplicador

    print(f"Lista com seus valores dobrados: {listaDeNumeros}")

# ja fiz a lógica "na mão" em outro exercício, vou fazer diferente aqui
# Poderia fazer de várias outras maneiras
def MaiorEMenorItemLista():
    listaDeNumeros = [10, 5, 3, 7, 19, 3]
    listaDeNumeros.sort()

    print(f"Menor valor da lista: {listaDeNumeros[0]}")
    print(f"Maior valor da lista: {listaDeNumeros[-1]}")


def QuantidadeCaracteresString():
    frase = "google.com"
    nmrLetras = {}
    
    for c in frase:
        nmrLetras.update({c:frase.count(c)})
    
    print(nmrLetras)


def StringMaiorQue2ELetrasIguais():
    listaDeFrases = ['abc','xyz','aba','1221']

    contador = 0
    for i in listaDeFrases:
        if (i[0] == i[-1] and len(i) > 2):
            contador += 1

    print(contador)


def OrdenarTruplaOrdemCrescente():
    listaDeTupla = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    for i in range(len(listaDeTupla)):
        for j in range(len(listaDeTupla)-1):
            if(listaDeTupla[j][-1] > listaDeTupla[j+1][-1]):
                listaDeTupla[j], listaDeTupla[j+1] = listaDeTupla[j+1], listaDeTupla[j]
    
    print(listaDeTupla)
 
def OrdenarTruplaOrdemCrescenteOutro():
    listaDeTupla = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    listaDeTupla.sort(key = lambda x: x[-1])
    print(listaDeTupla)


def AdicionarChaveDicionario():
    dicionario = {}
    chave = input("Digite a chave: ")
    valor = input("Digita o valor: ")
    dicionario[chave] = valor
    print(dicionario)


def ConcatenarDicionarios():
    dic1 = {1:10, 2:20}
    dic2 = {3:30, 4:40}
    dic3 = {5:50, 6:60}
    
    dic1.update(dic2)
    dic1.update(dic3)
    print(dic1)

