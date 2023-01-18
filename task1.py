from random import randint as ri

basket = int(input('Сколько конфет в корзине?: '))

def im(x, basket: int) -> int:
    while x < 1 or x > 28:
        print('Взять можно не более 28 попробуй ещё: ',end='')
        x = int(input(f'осталось {basket} конфет, сколько взять?: '))
    return x


def bot(x):
    n = 1
    if x <= 28:
        n = x
    elif x <= 56:
        n = x - 29

    while x - n < 0:
        n = ri(1, 28)
    x -= n
    return x

game = int(input('С кем играем? человек-человек->"1" человек-бот->"2": '))
if game == 1:
    a1 = input('Первый игрок представтесь: ')
    b2 = input('Второй игрок представтесь: ')
    if ri(1,2) == 1:
        while basket != 0:
            basket -= im((int(input(f'в корзинке {basket} конфет, сколько {a1} взять?: '))), basket)
            if basket > 0:
                basket -= im((int(input(f'в корзинке {basket} конфет, сколько {b2} взять?: '))), basket)
                if basket == 0:
                    print(f'Победил {b2}!!!')
            else:
                print(f'Победил {a1}!!!')
        print("Игра закончена!!!")
    else:
        while basket != 0:
            basket -= im((int(input(f'в корзинке {basket} конфет, сколько {b2} взять?: '))), basket)
            if basket > 0:
                basket -= im((int(input(f'в корзинке {basket} конфет, сколько {a1} взять?: '))), basket)
                if basket == 0:
                    print(f'Победил {a1}!!!')
            else:
                print(f'Победил {b2}!!!')
        print("Игра закончена!!!")
else:
    print('Игра с ботом')

    if ri(0, 1) == 0:
        while basket != 0:
            basket = bot(basket)
            if basket > 0:
                basket -= im((int(input(f'в корзинке {basket} конфет, сколько взять?: '))), basket)
                if basket == 0:
                    print('Ура!! вы победили!!!')
            else:
                print('Победил бот!!!')
        print('Игра закончена.')
    else:
        while basket != 0:
            basket -= im((int(input(f'в корзинке {basket} конфет, сколько взять?: '))), basket)
            if basket == 0:
                print('Ура!! вы победили!!!')
            basket = bot(basket)
            if basket == 0:
                print('Победил бот!!!')
        print('Игра закончена.')






