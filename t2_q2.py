def contador(l, v):
    ocorre = 0
    for num in l:
        if num == v:
            ocorre += 1
    return ocorre

def main():
    lista = []

    while True:
        num = int(input())
        if num == 0:
            break
        lista.append(num)

    valor = int(input())

    print(lista)
    print(valor)

    resultado = contador(lista, valor)
    print(resultado)

if __name__ == "__main__":
    main()