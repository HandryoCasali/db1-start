def MostrarMensagemAloMundo():
    print("Alo mundo")


def MostrarNumero():
    numero = input("Digite um numero: ")
    print("O Numero digitado foi", numero)


def MostrarSomaDoisNumeros():
    numero1 = int(input("Digite um numero: "))
    numero2 = int(input("Digite outro numero: "))
    soma = numero1 + numero2
    print(f"A soma de {numero1} + {numero2} é igual a {soma}")


def MostrarMedia():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"A media das notas {nota1} + {nota2} + {nota3} + {nota4} é {media}")


def ConverterMetroParaCentimetro():
    metro = float(input("Digite o valor em metro: "))
    centimetro = metro * 100
    print(f"{metro} m  são  {centimetro} cm")

from math import pi
def CalcularAreaCirculo():
    raio = float(input("Digite o valor do raio do circulo: "))
    area = pi * raio ** 2
    print(f"O Circulo com um raio de {raio} unidade(s) terá {round(area, 2)} unidade(s) de area")

def CalcularAreaQuadrado():
    lado = float(input("Digite valor do lado do quadrado: "))
    area = lado * lado
    print(f"Um quadrado com seu lado valendo {lado} unidade(s) tem como: ")
    print(f"Area: {area} unidade(s)")
    print(f"Dobro da area: {area * 2} unidade(s)")


# MostrarMensagemAloMundo()
# MostrarNumero()
# MostrarSomaDoisNumeros()
# MostrarMedia()
# ConverterMetroParaCentimetro()
# CalcularAreaCirculo()
# CalcularAreaQuadrado()
