
def MaiorNumero(numeros):
    return max(numeros)
    
def SomaNumero(numeros):
    return sum(numeros)

def FatorialNumero(numero):
    if(numero == 1 or numero == 0):
        return 1
    return numero * FatorialNumero(numero - 1)

def MultiplicarNumerosLista(numeros):
    produto = 1
    for numero in numeros:
        produto *= numero
    return produto

def InversoString(texto):
    return texto[::-1]    

def QuantidadeLetraMaiusculaMinuscula(texto):
    maiuscula = 0
    minuscula = 0
    for letra in texto:
        if(letra.isupper()):
            maiuscula += 1
        elif(letra.islower()):
            minuscula += 1

    return Mostrar(f"""Quantidade de letras:
    Maiúsculas = {maiuscula}
    Minúsculas = {minuscula}""")

def Mostrar(texto):
    print(texto)

def ExecutarCodigoEmString(codigo):
    exec(codigo)

def ListaDivisores(numero):
    listaDivisores = []
    for i in range(numero, 0, -1):
        if(numero % i == 0):
            listaDivisores.append(i)
    
    return listaDivisores

def EhPrimo(numero):
    if(numero <= 1):
        return False
    if(numero % 2 == 0 and numero != 2):
        return False
    
    qntDivisores = len(ListaDivisores(numero))
    
    if(qntDivisores > 2):
        return False

    return True

def EhPerfeito(numero):
    listaDivisores = ListaDivisores(numero)

    if(sum(listaDivisores) / 2 == numero):
        return True
    return False

# esse tive que pegar a solução na internet kkkkk
def TrianguloDePascal(qntLinhas):
    n = qntLinhas
    for i in range(n): 
        for j in range(n-i+1): 
            print(end=" ") 
    
        for j in range(i+1): 
            print(FatorialNumero(i)//(FatorialNumero(j)*FatorialNumero(i-j)), end=" ")
        print() 
        