def inverso(N):
    lista = []
    for i in range(N):
        num = float(input())
        lista.append(num)

    lista_inverso = lista[::-1]
    return lista_inverso


def notas_media(N):
    notas = []
    soma = 0
    for n in range(N):
        nota = float(input())
        notas.append(nota)
        soma += nota

    if N == 0:
        media = 0
    else:
        media = soma / N

    return notas, media


def vogais_consoantes(N):
    letras = []
    for l in range(N):
        letra = input()[0]
        letras.append(letra)

    vogais = 0
    consoantes = []
    for letra in letras:
        if letra in 'aeiouAEIOU':
            vogais += 1
        elif letra in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            consoantes.append(letra)

    return vogais, consoantes

def main():
    n = int(input())

    l_inverso = inverso(n)
    print(l_inverso)

    notas, media = notas_media(n)
    if n == 0:
        print(notas)
        print('SEM NOTAS')
        print(media)
    else:
        print(notas)
        print('{:.1f}'.format(media))

    vogais, consoantes = vogais_consoantes(n)
    if n != 0:
        print(vogais)
    print(consoantes)

if __name__ == "__main__":
    main()