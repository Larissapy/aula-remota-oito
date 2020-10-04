def media_altura(alturas_a):
    soma = 0
    cont = 0

    for num in alturas_a:
        soma += num
        cont += 1

    media = soma / cont

    return round(media, 2)


def menor_que_media(nomes_a, idades_a, alturas_a):
    media = media_altura(alturas_a)
    resultado = []

    pos = 0
    while pos <= len(alturas_a) - 1:
        if alturas_a[pos] < media:
            if idades_a[pos] > 13:
                resultado.append(nomes_a[pos])
        pos += 1

    return resultado

def main():
    nomes_alunos = []
    idades_alunos = []
    alturas_alunos = []

    for c in range(30):
        nome = str(input())
        nomes_alunos.append(nome)

        idade = int(input())
        idades_alunos.append(idade)

        altura = float(input())
        alturas_alunos.append(altura)
        
    print('MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')

    resultado = menor_que_media(nomes_alunos, idades_alunos, alturas_alunos)

    for n in range(len(resultado)):
        print(resultado[n])

if __name__ == "__main__":
    main()