#Importado do método operator o itemgetter
from operator import itemgetter

#Criado o dicionário e a lista.
estoque = {}
estoques = []

#Realizado o laço de repetição enquanto o usuário desejar inserir dados.
while True:
    terminar = input('Deseja cadastrar um item? 0 - Não  1 - Sim: 0 ')
    if terminar in '0':
        print('Finalizando o programa.')
        break
    if terminar not in '1':
        print('Digite 1 para Sim ou 0 para não.')
        continue

#Inseri e armazena os dados e ordena através do método sorted.
    estoque['codigo'] = int(input('Digite o código: '))
    estoque['estoque'] = int(input('Digite o estoque: '))
    estoque['minimo'] = int(input('Digite o mínimo: '))
    estoques.append(estoque.copy())
    listaOrdenada = sorted(estoques,key=itemgetter('codigo'))

    print(listaOrdenada)

