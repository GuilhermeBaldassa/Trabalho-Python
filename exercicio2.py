
#O usuário inseri o nome e o sobrenome.
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

#É selecionado apenas o primeiro caracter de nome e sobrenome.
nome1 = nome[0]
sobrenome1 = sobrenome[0]

#É realizado o print do e-mail com as primeiras letras do nome e sobrenome do usuário.
print('Sr. {} {}, seu email é: {}{}30@algoritimos.com.br'.format(nome,sobrenome,nome1,sobrenome1))