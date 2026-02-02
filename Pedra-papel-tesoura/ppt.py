# ppt = pedra, papel e tesoura.
import random
import os
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
def cpu ():# Para verificar escolha do cpu
    number = random.randrange(1,4)
    if number == 1:
        escolha2='Papel'
    elif number == 2:
        escolha2 = 'Pedra'
    else:
        escolha2 = 'Tesoura'
    return escolha2
def check():
    escolha2 = cpu()
    if escolha1 == 'Papel' and escolha2 == 'Pedra':
        print('Você escolheu "{}" e o CPU escolheu "{}"'.format(escolha1,escolha2))
        print('      Você ganhou!')
    elif escolha1 == 'Papel' and escolha2 == 'Tesoura':
        print('Você escolheu "{}" e o CPU escolheu "{}"'.format(escolha1,escolha2))
        print('      Você perdeu!')
    elif escolha1 == 'Pedra' and escolha2 == 'Papel':
        print('Você escolheu "{}" e o CPU escolheu "{}"'.format(escolha1,escolha2))
        print('      Você perdeu!')
    elif escolha1 == 'Pedra' and escolha2 == 'Tesoura':
        print('Você escolheu "{}" e o CPU escolheu "{}"'.format(escolha1,escolha2))
        print('      Você ganhou!')
    elif escolha1 == 'Tesoura' and escolha2 == 'Papel':
        print('Você escolheu "{}" e o CPU escolheu "{}"'.format(escolha1,escolha2))
        print('      Você ganhou!')
    elif escolha1 == 'Tesoura' and escolha2 == 'Pedra':
        print('Você escolheu "{}" e o CPU escolheu "{}"'.format(escolha1,escolha2))
        print('      Você perdeu!')
    else:
        print('Você escolheu "{}" e o CPU escolheu "{}"'.format(escolha1,escolha2))
        print('      Empatou!')
while True:
    print(40 * '=')
    print((12*'-') + ' Game - Jokenpô ' + (12*'-'))
    print(40 * '=')
    # Menu de opções
    print('Digite uma opção abaixo:')
    print('1 - Papel')
    print('2 - Pedra')
    print('3 - Tesoura')
    print('4 - Sair')
    opcao = input('Digite uma opção: ') #Entrada está como string
    if opcao == '1':
        escolha1 = 'Papel'
        #print(escolha1)
        limpar_terminal()
        check()
    elif opcao == '2':
        escolha1 = 'Pedra'
        #print(escolha1)
        limpar_terminal()
        check()
    elif opcao == '3':
        escolha1 = 'Tesoura'
        #print(escolha1)
        limpar_terminal()
        check()
    elif opcao == '4':
        limpar_terminal()
        print('Obrigado pela sua participação!')
        break
    else:
        limpar_terminal()
        print('Opção incorreta!')
        continue