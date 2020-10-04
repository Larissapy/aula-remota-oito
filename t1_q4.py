def p_i(l):
    par = []
    impar = []
    for p in l:
        if p % 2 == 0:
            par.append(p)
        else:
            impar.append(p)

    return par, impar


def main():
    lista = []
    for n in range(20):
        num = int(input())
        lista.append(num)

    print(lista)

    par, impar = p_i(lista)

    print(par)
    print(impar)

if __name__ == "__main__":
    main()