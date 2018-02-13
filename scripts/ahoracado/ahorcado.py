# Ascii art
import random 
import subprocess
import time

IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']

WORDS = [
  'lavadora',
  'camiseta',
  'conservatorio',
  'termodinamica',
  'procesadora',
  'sinonimo',
  'computadora',
  'fantasmagorico',
  'analogia',
  'indefinido',
  'sapodolfo'
]

def titulo():
  print('_______________________________________________\n')
  print(' ',' ',' ', end='')
  
  for j in ban:
    print(j,' ', end=' ')
  print('\n_______________________________________________\n')

def randomWord(WORDS=WORDS):
  id = random.randint(0, len(WORDS)-1)
  return WORDS[id]

def showBoard(hiddenWord, tries):
  subprocess.call(['clear'])
  titulo()
  print(IMAGES[tries])
  print('')
  for i in hiddenWord:
    print(i,end=' ')
  print('\n')
  print('--- * '*5)

def run():
  word = randomWord()
  hiddenWord = ['_ ']*len(word)
  tries = 0
  
  while(True):
    
    showBoard(hiddenWord, tries)
    letter = input('Ingresa una letra: ')

    letter_index = []

    for i in range(len(word)):
      if (word[i]==letter):
        letter_index.append(i)

    if(len(letter_index)==0):
      tries += 1
      if(tries==6):
        showBoard(hiddenWord, tries)
        print('______________________________________________________\n')
        print('\nPerdiste. La palabra correcta era {}.\n'.format(word))
        print('______________________________________________________\n')
        break
    else:
      for i in letter_index:
        hiddenWord[i] = letter

      letter_index = []

    try:
      hiddenWord.index('_ ')
    except ValueError:
      showBoard(hiddenWord, tries)
      print('______________________________________________________\n')
      print('\nFelicidades. Tu ganaste. La palabra es {}.\n'.format(word))
      print('______________________________________________________\n')
      break

#===========================================================
#if __name__ =='__main__':

saludo = ['B','I','E','N','V','E','N','I','D','O']
ban = []
s = 0
subprocess.call(['clear'])

for i in saludo:
  ban.append(i)
  print('_______________________________________________\n')
  print(' ',' ',' ', end='')
  for j in ban:
    print(j,' ', end=' ')

  print('\n')
  time.sleep(0.3)
  subprocess.call(['clear'])


run()
