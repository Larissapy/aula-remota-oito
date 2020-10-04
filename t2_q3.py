def soma_listas(l_a, l_b):
    l_c = []
    posi = 0

    while True:
        if len(l_c) >= 20:
            break

        l_c.append(l_a[posi] + l_b[posi])

        posi += 1

    return l_c


def main():
    lista_a = []
    for a in range(20):
        num = int(input())
        lista_a.append(num)

    lista_b = []
    for b in range(20):
        num = int(input())
        lista_b.append(num)

    print(lista_a)
    print(lista_b)

    lista_c = soma_listas(lista_a, lista_b)
    print(lista_c)

if __name__ == "__main__":
    main()