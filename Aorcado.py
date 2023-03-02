import random
import os
def run():

    Imagen = ['''
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


    BD=[
        "PAPA RELLANA ",
        "CAUSA",
        "CEBICHE",
        "AJI DE GALLINA",
    ]

    word=random.choice(BD)
    space=["_"] * len(word)
    attemps= 6
    while True:
       os.system("clear")
       for character in space:
           print(character,end="")
       print(Imagen[attemps])
       letter = input("Elige una letra ").upper() 

       found = False
       for idx,character in enumerate(word):
          if character == letter:
              space[idx]= letter
              found = True
       if not found:
           attemps=-1
       if "_"not in space:
           os.system("clear")
           print("Ganastes")
           break
           input()
       if attemps == 0:
           os.system("clear")
           print("Perdistes")
           break
           input()
       

if __name__== "__main__":
    run()
