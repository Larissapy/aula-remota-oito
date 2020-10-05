from random import *

executa = True
adjetivos = ['maravilhoso', 'acima da média', 'excelente']
hobbies = ['andar de bicicleta', 'progamar', 'fazer chá']

print('Gerador de Cumprimentos')
print('----- ----------')

nome = input('Qual o seu nome?: ')

print('''
Menu
  c = obter cumprimento
  a = adicionar hobby
  d = remover hobby
  p = imprimir hobbies
  q = sair
''')

while executa == True:

    menu_choice = input("\n>_").lower()

    if menu_choice == 'c':
        print('Aqui está o seu cumprimento', nome, ':')

        print(nome, 'você é', choice(adjetivos), 'em', choice(hobbies))
        print('De nada!')

    elif menu_choice == 'a':
        item_to_add = input('Adicione o hobby: ')

        if item_to_add not in hobbies:
            hobbies.append(item_to_add)
        else:
            print('O hobby já está na lista!')

    elif menu_choice == 'd':
        item_to_deleted = input('Insira o hobby a ser removido: ')

        if item_to_deleted in hobbies:
            hobbies.remove(item_to_deleted)

        else:
            print('O hobby não está na lista!')

    elif menu_choice == 'p':
        print(hobbies)

    elif menu_choice == 'q':
        executa = False

    else:
        print('Insira uma opção válida!')