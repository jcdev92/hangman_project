import random
import os

def clear():                                       #También la podemos llamar cls (depende a lo que estemos acostumbrados)
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")    


def words():
    with open('./WORDS/words.txt', 'r') as f:
        palabras = list(map(lambda w: w.rstrip('\n'), f))
    word = random.choice(palabras)
    guion = ''
    for x in word:
        guion += '-' 
    lose = 'ahorcado'
    loser = ''
    if guion != word:
            print(guion, end=' ')
            while True:
                enter = input('\nIngrese una letra: ')
                if len(enter) == 1:
                    break
                else: 
                    print('\nsolo se puede ingresar una letra por intento, intentelo de nuevo\n')
            for z in word:
                y = word.find(z)
                w = word.find(z, y)
                if enter == z:
                    l = list(guion)
                    l[y] = enter
                    l[w] = enter
                    guion = "".join(l)
                    clear()     
    elif guion == word:
        print(guion, end=' ')
        print('Felicidades Ganaste!!')

def run():
    words()

if __name__ == '__main__':
    run()