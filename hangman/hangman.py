import random
import os

def clear(): #También la podemos llamar cls (depende a lo que estemos acostumbrados)
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")    


def word():
    with open('./WORDS/words.txt', 'r') as f:
        words = list(map(lambda w: w.rstrip('\n'), f))
    word = random.choice(words)
    guion = ''
    
    for x in word:
        guion += '-'
    print(guion, end=' ')
    enter = input('\nIngrese una letra: ')
    clear()
    
    while enter != x:
        print(guion, end=' ')
        enter = input('\ningrese una letra: ')
        clear()
    else:
        for i in range(guion.length()):
            s = guion
            l = list(s)
            l[guion] = enter
            s = "".join(l)
            print(s, end=' ')
    
    



def run():
    word()

if __name__ == '__main__':
    run()