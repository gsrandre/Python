import os
import sys
from time import sleep

secret_word = ''
correct_letters = []
wrong_letters = []
attempts = 10 
new_word ='' 

def msg ():
    print('-'*16,'Jogo Adivinhe!','-'*16)
    print('Criador: André GSR - 15-01-2026')
    print('-'*50)

while True:
    os.system('cls')     
    if secret_word=='':
        msg()
        try:  
            secret_word = str(input('1° Jogador Informe a palavra secreta: ').strip().upper())
            os.system('cls')  
            if secret_word.isalpha() == False:
                input('Digite uma palavra sem números!') 
                secret_word =''                
        
        except Exception:
            print('Erro desconhecido, tente novamente!')
            break

    if attempts == 0:
      print('Você perdeu!')
      print('Palavra Secreta: ', secret_word) 
      sleep(5) 
      break

    print('-' *15, 'Adivinhe a Palavra', '-'*15)               
    print('Palavra Screta: ', new_word)
    print('Letras Acertadas: ',correct_letters)
    print('Letras Erradas: ',wrong_letters)
    print('-'*48)  

    try:
        if secret_word != '':
            print(f'2° Jogador, você perde se errar "{attempts}" vezes.')
            letter=input(str('Informe uma letra: ')).strip().upper() 

        if len(letter) > 1:
            input('Digite apenas uma letra.')
            continue
        
        if letter.isalpha() == False:
            input('Digite uma letra do alfabeto A-Z')
            continue    

        if letter in secret_word:          
            correct_letters.append(letter)
        else:
             wrong_letters.append(letter)
             attempts -= 1 

        new_word = ''     
        for i in secret_word:
            if i in correct_letters:
                    new_word += i               
            else:
                new_word += '*'    
        
        if new_word == secret_word:
            print('Parabêns! Você Acertou!')
            print('Palavra Secreta: ', secret_word)
            sleep(5)
            break

        resp=''         
        while resp != 'S':     
            resp=str(input('Deseja continuar?[S/N]: ')).strip().upper()
            if resp == 'S':                   
                continue
            elif resp == 'N':    
                os.system('cls')
                print('Obrigado por jogar!')
                sleep(3) 
                sys.exit()                 
        
    except Exception:
        print('Erro desconhecido, tente novamente!') 
print('Obrigado por jogar!')  
