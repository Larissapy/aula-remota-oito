def soma(num):
    som = 0
    for s in range(10):
        som += num[s]
    return som


def multiplicacao(num):
    mult = 1
    for m in range(10):
        mult *= num[m]
    return mult

def main():
    num = []
    for n in range(10):
        n = int(input())
        num.append(n)

    s = soma(num)
    m = multiplicacao(num)

    print(num)
    print(s)
    print(m)

if __name__ == "__main__":
    main()