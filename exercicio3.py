#Importado o método random.
import random

#Foi criado uma função que recebe o nome e o valor doado e se o valor é maior que 10,
#permite que o usuário tenha seu nome no sorteio quantas vezes a doação dele for múltiplo de 10.
def integrantes (nome,valor):
    global lista
    while valor >= 10:
        valor = int(valor/10)
        lista = [nome] * valor
        continue

#Inicia-se o programa principal com a pergunta ao usuário.
prossiga = input('Deseja contribuir? 0 - Não   1 - Sim')
listaSorteados = []

#Laço de repetição que vai armazenando os participantes na ListaSorteados.
while True:
    if prossiga == '1':
        nome = (input('Digite o nome: '))
        valor = int(input('Digite o valor doado: '))
        nomes = integrantes(nome,valor)
        print('{} doou R${} e participará do sorteio'.format(nome,valor))
        listaSorteados.append([lista])
        prossiga = input('Deseja contribuir? 0 - Não   1 - Sim')
        continue

#Quando o usuário não deseja mais inserir dados, é mostrado a mensagem e realizado o sorteio.
    else:
        print('O sorteio será realizado.')
        print(listaSorteados)
        break


#Utilizado o método random para realizar o sorteio.
random.shuffle(listaSorteados)
sorteio = random.choice(listaSorteados)
print('O sorteado foi: {}'.format(sorteio))










