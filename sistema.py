import os
from time import sleep


def separador():
    print('-*'*20)


def inicio():
    print('*'*40)
    print('SISTEMA SEPARADOR DE DOMÍNIOS DE EMAILS')
    sleep(1)
    print('INICIANDO...')
    sleep(1)
    print('Por favor, comece adicionando um e-mail.')
    sleep(1)
    print('*' * 40)
    sleep(1)
    print('')


def menu():
    print('1 - Adicionar E-mail')
    print('2 - Listar endereços Gmail')
    print('3 - Listar endereços conectanuvem')
    print('4 - Listar endereços de outros domínios')
    print('5 - Sair')


emails = []


def adicionar():
    temp = [input('Entre com o e-mail: ')]
    print('E-mail adicionado com sucesso.')
    while True:
        adicionar = input('Deseja adicionar outro número? [S/N]').strip().upper()[0]
        if adicionar == 'S':
            n = input('Entre com e-mail: ')
            if n not in temp:
                temp.append(n)
                print('E-mail adicionado com sucesso.')
            else:
                print('E-mail já cadastrado.')
        elif adicionar == 'N':
            break
        else:
            print('Opção inválida!')
    for x in temp:
        emails.append(x)
    separador()


def listaGmail():
    print('Lista de e-mails do GMAIL:')
    for x in gmail:
        print(x)
    os.system('pause')
    separador()


def listaConecta():
    print('Lista de e-mails do CONECTANUVEM:')
    for x in conecta:
        print(x)
    os.system('pause')
    separador()


def listaOutros():
    print('Lista de e-mails de outros domínios:')
    for x in outros:
        print(x)
    os.system('pause')
    separador()


def contador():
    print('Total de e-mails cadastrados: ', len(emails))
    print('')


inicio()
opc = 0
while opc != 5:
    contador()
    menu()
    opc = int(input('Opção: '))
    if opc == 1:
        adicionar()
        splitado = list(map(lambda x: x.split('@'), emails))

        gmail = []
        conecta = []
        outros = []

        for x in splitado:
            if x[1] == 'gmail.com':
                gmail.append(x[0] + '@' + x[1])
            elif x[1] == 'conectanuvem.com.br':
                conecta.append(x[0] + '@' + x[1])
            elif x[1] != 'gmail.com' and x[1] != 'conectanuvem.com.br':
                outros.append(x[0] + '@' + x[1])

    elif opc == 2:
        listaGmail()
    elif opc == 3:
        listaConecta()
    elif opc == 4:
        listaOutros()
    elif opc == 5:
        print('Programa finalizado!')
    else:
        print('Opção Inválida!')

