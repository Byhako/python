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
  'camion',
  'termodinamica',
  'amistad',
  'sinonimo'
]

def randomWord(WORDS=WORDS):
  id = random.randint(0, len(WORDS)-1)
  return WORDS[id]

def showBoard(hiddenWord, tries):
  subprocess.call(['clear'])
  print('= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =\n')
  print(' ',' ',' ',cont,'\n')
  print('= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =\n')
  print(IMAGES[tries])
  print('')
  print(hiddenWord,'\n')
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
        print('\nPerdiste. La palabra correcta era {}.\n'.format(word))
        break
    else:
      for i in letter_index:
        hiddenWord[i] = letter

      letter_index = []

    try:
      hiddenWord.index('_ ')
    except ValueError:
      print('\nFelicidades. Tu ganaste. La palabra es {}.\n'.format(word))
      break

#===========================================================
#if __name__ =='__main__':

saludo = ['B','I','E','N','V','E','N','I','D','O']
cont = []

subprocess.call(['clear'])

for i in saludo:
  cont.append(i)
  print('= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =\n')
  print(' ',' ',' ',cont)
  time.sleep(0.3)
  subprocess.call(['clear'])


run()
