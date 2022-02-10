import random
def words():
    with open('./WORDS/words.txt', 'r') as f:
        palabras = list(map(lambda w: w.rstrip('\n'), f))
    word = random.choice(palabras)
    for x in word:
        print('-', end=' ')
    enter = input('\nIngresa una letra: ')

    


def run():
    words()

if __name__ == '__main__':
    run()