'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''


def fibonacciChecker(number):
    fibList = [0, 1]
    fib = 0
    while (fib < number):
        fib = fibList[-1] + fibList[-2]
        fibList.append(fib)
    
    if fib == number:
        print("O número pertence à sequência\n")
        return True
    
    print("O número não pertence à sequência\n")
    return False

number = float(input("Digite um número: "))
fibonacciChecker(number)
