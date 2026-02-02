import os
from time import sleep
print('-'*16,'Jogo Adivinhe!','-'*16)
print('Criador: André GSR - 15-01-2026')

while True:  
  try:      
    print('-' *15, 'Adivinhe a Palavra', '-'*15)
    pSecreta = str(input('1° Jogador Informe a palavra secreta: ').strip().upper())
    if pSecreta.isalpha() == False:
      print('Digite uma palavra sem números!')  
      continue  
    if pSecreta != '':
       break
  except Exception:
    print('Erro desconhecido, tente novamente!')
    break

letras_acertadas = []
letras_erradas = []
tentativas = 10 
novPalavra =''
while True:  
  os.system('cls') 
  try:
    if tentativas == 0:
      print('Você perdeu!')
      print('Palavra Secreta: ', pSecreta) 
      sleep(5) 
      break    

    print('-' *10, 'Adivinhe a Palavra', '-'*10)               
    print('Palavra Screta: ', novPalavra)
    print('Letras Acertadas: ',letras_acertadas)
    print('Letras Erradas: ',letras_erradas)
    print('-'*50)   

    print(f'2° Jogador, você perde se errar "{tentativas}" vezes.')
    letra=input(str('Informe uma letra: ')).strip().upper() 

    if len(letra) > 1:
          print('Digite apenas uma letra.')
          continue
    
    if letra.isalpha() == False:
          print('Digite uma letra do alfabeto A-Z')
          continue    

    if letra in pSecreta:          
      letras_acertadas.append(letra)
    else:
      letras_erradas.append(letra)
      tentativas -= 1 

    novPalavra = ''     
    for i in pSecreta:
        if i in letras_acertadas:
                  novPalavra += i               
        else:
              novPalavra += '*'    
    
    if novPalavra == pSecreta:
      print('Parabêns! Você Acertou!')
      print('Palavra Secreta: ', pSecreta)
      sleep(5)
      break  

    resp=''  
    while resp != 'S':     
      resp=str(input('Deseja continuar?[S/N]: ')).strip().upper()
      if resp == 'S':                   
        continue
      elif resp == 'N':    
        os.system('cls')  
        break
    
  except Exception:
      print('Erro desconhecido, tente novamente!')   
      
print('Obrigado por jogar!')
