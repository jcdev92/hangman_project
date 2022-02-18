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
        
    while guion != word:
            print(guion, end=' ')
            enter = str(input('\nIngrese una letra: '))
            for z in word:
                y = word.find(z)
                w = word.find(z, y+1)
                if enter == z:
                    l = list(guion)
                    l[y] = enter
                    l[w] = enter
                    guion = "".join(l)
            clear()
    else:
        print(guion, end=' ')
        print('Felicidades Ganaste!!')
        clear()


def run():
    words()

if __name__ == '__main__':
    run()