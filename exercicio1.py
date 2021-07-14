dados = (input('Deseja inserir dados?   0 - Não      1 - Sim '))

#laço de repetição enquanto o usuário desejar inserir a nota.
while (dados == '1'):
        nome = input('Digite seu nome: ')
        nota = float(input('Digite sua nota: '))

        #Condicional para evitar que o usuário digite uma nota maior que 10.
        while nota > 10:
            print('Nota inválida,')
            nome = input('Digite seu nome novamente: ')
            nota = float(input('Digite sua nota novamente: '))
            print('Nota inválida,')
            break

        #Assim que o usuário digita o nome e a nota, é feito o print na tela.
        else:
            print('\nNome do aluno: {}'.format(nome))
            print('Nota final: {}'.format(nota))

            #Condicionais para cada faixa de nota, que retorna o conceito que o aluno se enquadra.
            if (nota >= 9.0) and (nota <= 10.0):
                print('O aluno {} tirou a nota {} e se enquadra no conceito A.'.format(nome,nota))

            elif (nota >= 7.0) and (nota <= 8.9):
                print('O aluno {} tirou a nota {} e se enquadra no conceito B.'.format(nome,nota))

            elif (nota >= 5.0) and (nota <= 5.9):
                print('O aluno {} tirou a nota {} e se enquadra no conceito C.'.format(nome,nota))

            elif (nota >= 3.0) and (nota <= 4.9):
                print('O aluno {} tirou a nota {} e se enquadra no conceito D.'.format(nome,nota))

            elif (nota >= 0) and (nota <= 2.9):
                print('O aluno {} tirou a nota {} e se enquadra no conceito E.'.format(nome,nota))

            #A Qualquer momento que o usuário digitar 1 o programa finaliza.
            encerrar = input('\nDigite 1 para Sair.')
            if (encerrar == '1'):
                print('Programa finalizado!')
            break
#condicional para encerramento do programa se o usuário desejar fechá-lo no início
else:
    if (dados == '0'):
        print('Programa finalizado.')