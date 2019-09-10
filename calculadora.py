
def soma(a, b):
    print(" a + b = ", a+b)

def subtrai(a, b):
    print(" a - b = ", a-b)

def multiplica(a, b):
    print(" a * b = ", a*b)

def divide(a, b):

    if(b != 0):
        print(" a / b = ", a/b)
    else:
        print("Operação impossível.")




print("Calculadora simples")

num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))

soma(num1, num2)
subtrai(num1, num2)
multiplica(num1, num2)
divide(num1, num2)

