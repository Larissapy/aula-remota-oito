def mais_alto(a_j, n_j):
    alto = a_j[0]
    nome_alto = n_j[0]
    pos = 0
    for a in a_j:
        if a > alto:
            alto = a
            nome_alto = n_j[pos]
        pos += 1
    return alto, nome_alto

def media_altura(a_j):
    soma = 0
    cont = 0
    for num in a_j:
        soma += num
        cont += 1
    media = soma / cont
    return media

def mais_alto_media(a_j, n_j):
    media = media_altura(a_j)
    pos = 0
    maior_que_media = []
    for a in a_j:
        if a > media:
            maior_que_media.append(n_j[pos])
            maior_que_media.append(a)
        pos += 1
    return maior_que_media

def main():
    nomes_jogadores = []
    alturas_jogadores = []

    for c in range(12):
        nome = str(input())
        nomes_jogadores.append(nome)

        altura = float(input())
        alturas_jogadores.append(altura)

    alto, nome_alto = mais_alto(alturas_jogadores, nomes_jogadores)

    print('JOGADOR MAIS ALTO DO TIME')
    print(nome_alto)
    print('{:.2f}'.format(alto))

    media = media_altura(alturas_jogadores)

    print('ALTURA MÉDIA DO TIME')
    print('{:.2f}'.format(media))

    maior_que_media = mais_alto_media(alturas_jogadores, nomes_jogadores)

    print('JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')

    pos = 0
    for n in maior_que_media:
        if pos % 2 == 0:
            print(maior_que_media[pos])
        else:
            print('{:.2f}'.format(maior_que_media[pos]))
        pos += 1

if __name__ == "__main__":
    main()