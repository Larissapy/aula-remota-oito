def zero(n):
    lista_1 = []
    for z in range(n):
        lista_1.append(0)
    return lista_1

def sequencia(n):
    lista_2 = []
    for s in range(1, n + 1):
        lista_2.append(s)
    return lista_2

def lidos_teclado(n):
    lista_3 = []
    for l in range(n):
        num = int(input())
        lista_3.append(num)
    return lista_3

def inverso(n):
    lista_4 = []
    for i in range(n):
        num = int(input())
        lista_4.append(num)
    return lista_4[:: -1]

def main():
    n = int(input())

    l_1 = zero(n)
    print(l_1)
    l_2 = sequencia(n)
    print(l_2)
    l_3 = lidos_teclado(n)
    print(l_3)
    l_4 = inverso(n)
    print(l_4)

if __name__ == "__main__":
    main()