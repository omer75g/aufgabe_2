from random import randint


def text_1():
    random_text = randint(0,3)
    awesome_text = ['I didn’t fall down. I did attack the floor, though.',
                    'I am nobody. Nobody is perfect. I am perfect.',
                    'I’m never late. The others are just too early!',
                    'There’s no “we” in fries.']

    return awesome_text[random_text]

