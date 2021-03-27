from time import time
import sys


def fibonacci(n:int):
    if n == 1 or n == 0:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_dinamico(n:int, diccionario = {}):
    if n == 1 or n == 0:
        return 1
    try:
        return diccionario[n]
    except KeyError:
        resp = fibonacci_dinamico(n-1, diccionario) + fibonacci_dinamico(n-2, diccionario)
        diccionario[n]=resp
        return resp
def factorial(n:int, diccionario = {}):
    if n == 1 or n == 0:
        return 1
    try:
        return diccionario[n]
    except KeyError:
        resp = n * factorial(n-1, diccionario)
        diccionario[n]=resp
        return resp



if __name__ == '__main__':
    n = int(input('Escoge un número: '))
    sys.setrecursionlimit(n+10)
    resp = 0
    tiempo = time()

    #resp = fibonacci(n)
    #resp = fibonacci_dinamico(n)
    resp = factorial(n)


    print(resp)
    total = time()- tiempo
    print('Tiempo de ejecución: ',round(total, 2)) 
