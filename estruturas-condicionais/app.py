
def MaiorDosNumeros():
    numero1 = int(input("Digite um numero: "))
    numero2 = int(input("Digite mais um numero: "))

    if (numero1 > numero2):
        print(f"O numero {numero1} é maior que o numero {numero2} !")
    elif (numero2 > numero1):
        print(f"O numero {numero2} é maior que o numero {numero1} !")
    else:
        print("Os dois números são iguais!")

def ValorPositivoOuNegativo():
    numero = int(input("Digite um numero: "))

    if (numero > 0):
        print(f"O número {numero} é positivo!")
    elif (numero < 0):
        print(f"O número {numero} é negativo!")
    else:
        print(f"O número é neutro! Portanto é igual a zero!")

def InformarSexoMasculinoOuFeminino():
    sexo = input("Digite M para masculo ou F para feminino: ").upper()
    
    if (sexo == "M"):
        print("Sexo Masculino")
    elif (sexo == "F"):
        print("Sexo Feminino")
    else:
        print("Opção inválida")

def VogalOuConsoante():
    vogais = ("A", "E", "I", "O", "U")

    letra = input("Digite uma letra para saber se é vogal ou consoante: ").upper()
    
    if (letra in vogais):
        print(f"A Letra {letra} é uma vogal!")
    else:
        print(f"A Letra {letra} é uma consoante!")

def MaiorEMenorEntreTresNumeros():
    numero1 = int(input("Digite um numero: "))
    numero2 = int(input("Digite mais numero: "))
    numero3 = int(input("Digite o ultimo numero: "))

    maior = menor = 0
    if( numero1 >= numero2 and numero1 >= numero3 ):
        maior = numero1
        menor = numero2 if numero2 <= numero3 else numero3

    elif( numero2 >= numero1 and numero2 >= numero3 ):
        maior = numero2
        menor = numero1 if numero1 <= numero3 else numero3
    else:
        maior = numero3
        menor = numero1 if numero1 <= numero3 else numero3
    
    print(f"O maior numero é {maior} e o menor numero é {menor}")

def ProdutoMaisBarato():
    preco1 = float(input("Digite o preço do primeiro produto: "))
    preco2 = float(input("Digite o preço do segundo  produto: "))
    preco3 = float(input("Digite o preço do terceiro produto: "))

    menorValor = 0
    if ( preco1 <= preco2 and preco1 <= preco3 ):
        menorValor = preco1
    elif ( preco2 <= preco1 and preco2 <= preco3 ):
        menorValor = preco2
    else:
        menorValor = preco3
    
    print(f"O produto mais barato é o que custa {menorValor:.2f}")

def OrdemDecrescenteEntreTresNumeros():
    numero1 = int(input("Digite um numero: "))
    numero2 = int(input("Digite mais um numero: "))
    numero3 = int(input("Digite outro numero: "))
    
    if(numero1 >= numero2 and numero1 >= numero3):
        if(numero2 >= numero3):
            print(f"Em ordem Decrescente: {numero1} - {numero2} - {numero3}")
        else:
            print(f"Em ordem Decrescente: {numero1} - {numero3} - {numero2}")
    elif(numero2 >= numero1 and numero2 >= numero3):
        if(numero1 >= numero3):
            print(f"Em ordem Decrescente: {numero2} - {numero1} - {numero3}")
        else:
            print(f"Em ordem Decrescente: {numero2} - {numero3} - {numero1}")
    else:
        if(numero1 >= numero3):
            print(f"Em ordem Decrescente: {numero3} - {numero1} - {numero2}")
        else:
            print(f"Em ordem Decrescente: {numero3} - {numero2} - {numero1}")

def MostrarTurno():
    turno = input("Digite M-Matutino V-Vespertino N-Noturno: ").upper()

    if(turno == "M"):
        print("Bom dia!")
    elif(turno == "V"):
        print("Boa tarde!")
    elif(turno == "N"):
        print("Boa noite!")
    else:
        print("Opção inválida")

def MediaEntreDuasNotas():
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    media = (nota1 + nota2) / 2
    
    if(media == 10):
        print("Aprovado com distinção")
    elif(media >= 7):
        print("Aprovado")
    else:
        print("Reprovado")

def ReajusteSalarial():
    salario = float(input("Digite o salario do colaborador: "))
    
    reajuste = 0
    if(salario >= 1500):
        reajuste = 5
    elif(salario >= 700):
        reajuste = 10
    elif(salario > 280):
        reajuste = 15
    elif(salario > 0 and salario <= 280):
        reajuste = 20
    else:
        print("Salario negativo!")
    
    aumento = salario * (reajuste / 100)

    print(f"O salario de R$ {salario:.2f} com um reajuste de {reajuste}% terá um aumento de R$ {aumento:.2f}")
    print(f"Novo salário passará a ser R$ {salario + aumento}")

def CalculoFolhaPagamento():
    salarioBruto = float(input("Digite o salário bruto do colaborador: "))
    sindicato = salarioBruto * ( 3 / 100 )
    fgts = salarioBruto * (11 / 100)

    impostoRenda = 0
    
    if(salarioBruto <= 900):
        impostoRenda = 0
    elif(salarioBruto <= 1500):
        impostoRenda = 5
    elif(salarioBruto <= 2500):
        impostoRenda = 10
    elif(salarioBruto > 2500):
        impostoRenda = 20
    
    descontoImpostoRenda = salarioBruto * (impostoRenda / 100)
    salarioLiquido = salarioBruto - descontoImpostoRenda - sindicato

    print(f"Com um salário bruto de R$ {salarioBruto:.2f} terá os seguintes valores: ")
    print(f"Imposto de Renda {impostoRenda}%: R${descontoImpostoRenda:.2f}")
    print(f"Sindicato: R$ {sindicato:.2f}")
    print(f"FGTS: R$ {fgts:.2f}")
    print(f"Salário Líquido: R$ {salarioLiquido:.2f}")

def DiaCorrespondenteDaSemana():
    numero = int(input("Digite um numero de 1 a 7 para saber o dia da semana correspondente: "))
    if(numero == 1):
        print("Domingo")
    elif(numero == 2):
        print("Segunda-feira")
    elif(numero == 3):
        print("Terça-feira")
    elif(numero == 4):
        print("Quarta-feira")
    elif(numero == 5):
        print("Quinta-feira")
    elif(numero == 6):
        print("Sexta-feira")
    elif(numero == 7):
        print("Sábado")
    else:
        print("Opção inválida!")

def MediaAlunoComConceito():
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    media = (nota1 + nota2) / 2
    letraMedia = ""

    if(media > 9 and media <= 10):
        letraMedia = "A"
    elif(media > 7.5 and media <= 9):
        letraMedia = "B"
    elif(media > 6 and media <= 7.5):
        letraMedia = "C"
    elif(media > 4 and media <= 6):
        letraMedia = "D"
    elif(media > 0 and media <= 4):
        letraMedia = "E"
    else: 
        print("Notas inválidas para média!")
    
    aprovadoOuReprovado = "APROVADO" if letraMedia == "A" or "B" or "C" else "REPROVADO"
    
    print(f"O aluno com as notas: {nota1} e {nota2} Obteve a média {media}")
    print(f"O conceito correspondente foi: {letraMedia} e o aluno foi {aprovadoOuReprovado}")
    
def ClassificacaoTriangulo():
    lado1 = float(input("Digite o primeiro lado do triangulo: "))
    lado2 = float(input("Digite o segundo lado do triangulo: "))
    lado3 = float(input("Digite o terceiro lado do triangulo: "))
    ehTriangulo = lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1
    tipoTriangulo = ""
    if(lado1 != lado2 != lado3 != lado1):
        tipoTriangulo = "escaleno"
    elif(lado1 == lado2 == lado3 == lado1):
        tipoTriangulo = "equilátero"
    else:
        tipoTriangulo = "isósceles"
    
    if (ehTriangulo):
        print(F"É possível formar um triângulo {tipoTriangulo} com os valores fornecidos!")
    else:
        print("Não é possível formar um triângulo com os valores fornecidos!")

from math import sqrt

def RaizesEquacaoSegundoGrau():
    print("Fórmula da equação do segundo grau = Ax² + Bx + C")
    a = float(input("Digite o valor de A da equação do segundo grau: "))
    b = float(input("Digite o valor de B da equação do segundo grau: "))
    c = float(input("Digite o valor de C da equação do segundo grau: "))

    delta = b**2 - 4*a*c
    if (delta > 0):
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print(f"Possui duas raízes sendo elas: ({x1} e {x2})")
    elif (delta == 0):
        x1 = (-b + sqrt(delta)) / (2 * a)
        print(f"Possui uma raíz sendo ela:  ({x1})")
    else:
        print("Não possui raiz nos conjuntos dos numeros reais.")

def AnoBissexto():
    ano = int(input("Digite o ano para saber se é ano bissexto: "))
    
    if(ano % 400 == 0):
        print(f"Ano {ano} é bissexto")
    elif(ano % 4 == 0 and ano % 100 != 0):
        print(f"Ano {ano} é bissexto")
    else:
        print(f"Ano {ano} não é bissexto")

import re
def DataValida():
    dataDigitada = input("Digite a data no formato dd/mm/aaaa: ")
    if(re.search("^[0-3][0-9]/[0-1][0-9]/\d{4}", dataDigitada)):
        print("A data está no formato válido")
    else:
        print("Data está em um formato inválido")


def QuebrarNumero():
    numero = int(input("Digite um numero inteiro entre 0 e 9999: "))
    milhar = numero // 1000
    centena = numero // 100 % 10
    dezena = numero // 10 % 10
    unidade = numero % 10

    print(f"Dado o numero {numero}")
    print(f"O milhar é: {milhar}")
    print(f"A centena é: {centena}")
    print(f"A dezena é: {dezena}")
    print(f"A unidade é: {unidade}")
