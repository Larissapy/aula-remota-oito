from random import *

print('Gerador de Cumprimentos')
print('----- ----------')

adjetivos = ['maravilhoso', 'acima da média', 'excelente', 'incrível', 'muito bom']

hobbies = ['andar de bicicleta', 'progamar', 'fazer chá', 'fazendo doces', 'idiomas' ]

nome = input("Qual o seu nome?: ")
print('Aqui está o seu cumprimento', nome, ':')

print(nome , 'você é' , choice(adjetivos) , 'em' , choice(hobbies) )
print('De nada!')
