import random
import os

def clear(): #También la podemos llamar cls (depende a lo que estemos acostumbrados)
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")    


def words():
    with open('./WORDS/words.txt', 'r') as f:
        palabras = list(map(lambda w: w.rstrip('\n'), f))
    word = random.choice(palabras)
    guion = ''
    data = ''
    for x in word:
        guion += '-'
    print(guion, end=' ')
    enter = input('\nIngrese una letra: ')
    clear()
    
    while guion != word:
        print(guion, end=' ')
        enter = input('\ningrese una letra: ')
        for y in word:
            if enter == y:
                s = guion
                l = list(s)
                l[2] = enter
                s = "".split(y)
        clear()
    else:
        print(guion, end=' ')
        
    
    



def run():
    words()

if __name__ == '__main__':
    run()