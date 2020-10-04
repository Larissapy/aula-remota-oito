def comprimento(lista):
    c = len(lista)
    return c

def inverter(lista):
    inv = lista[:: - 1]
    return inv

def minimo(lista):
    menor = min(lista)
    return menor

def maximo(lista):
    maior = max(lista)
    return maior

def soma(lista):
    s = sum(lista)
    return s

def main():
    lista = []

    while True:
        num = int(input())
        if num == 0:
            break
        lista.append(num)

    print(lista)

    contador = comprimento(lista)
    print(contador)

    inv = inverter(lista)
    print(inv)

    menor = minimo(lista)
    print(menor)

    maior = maximo(lista)
    print(maior)

    soma_valores = soma(lista)
    print(soma_valores)

if __name__ == "__main__":
    main()