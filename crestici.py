from random import randint as ri

a = [[' ','|',' ','|',' '],
     ['-','-','-','-','-'],
     [' ','|',' ','|',' '],
     ['-','-','-','-','-'],
     [' ','|',' ','|',' ']]


def printlist(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()


def motion(a,field):
    if field == 1:
        a[0][0] = 'x'
    elif field == 2:
        a[0][2] = 'x'
    elif field == 3:
        a[0][4] = 'x'
    elif field == 4:
        a[2][0] = 'x'
    elif field == 5:
        a[2][2] = 'x'
    elif field == 6:
        a[2][4] = 'x'
    elif field == 7:
        a[4][0] = 'x'
    elif field == 8:
        a[4][2] = 'x'
    elif field == 9:
        a[4][4] = 'x'
    return a

def motion2(a,field):
    if field == 1:
        a[0][0] = 'o'
    elif field == 2:
        a[0][2] = 'o'
    elif field == 3:
        a[0][4] = 'o'
    elif field == 4:
        a[2][0] = 'o'
    elif field == 5:
        a[2][2] = 'o'
    elif field == 6:
        a[2][4] = 'o'
    elif field == 7:
        a[4][0] = 'o'
    elif field == 8:
        a[4][2] = 'o'
    elif field == 9:
        a[4][4] = 'o'
    return a


def bot(a):
    caunt = 0
    for g in range(0,len(a),2):
        for y in range(0,len(a[g]),2):
            if a[g][y] == 'x' or a[g][y] == 'o':
                caunt += 1
    if caunt == 9:
        print('Ничья')
        return a
    i = ri(0, 4)
    j = ri(0, 4)
    if a[i][j] != 'x' and a[i][j] != '|' and a[i][j] != '-' and a[i][j] != 'o':
        a[i][j] = 'o'
    else:
        bot(a)
    return a


def finish(a):
    finish = 0
    if a[0][0] == a[0][2] == a[0][4] == 'x' or a[0][0] == a[0][2] == a[0][4] == 'o':
        finish = 1
    elif a[2][0] == a[2][2] == a[2][4] == 'x' or a[2][0] == a[2][2] == a[2][4] == 'o':
        finish = 1
    elif a[4][0] == a[4][2] == a[4][4] == 'x' or a[4][0] == a[4][2] == a[4][4] == 'o':
        finish = 1
    elif a[0][0] == a[2][0] == a[4][0] == 'x' or a[0][0] == a[2][0] == a[4][0] == 'o':
        finish = 1
    elif a[0][2] == a[2][2] == a[4][2] == 'x' or a[0][2] == a[2][2] == a[4][2] == 'o':
        finish = 1
    elif a[0][4] == a[2][4] == a[4][4] == 'x' or a[0][4] == a[2][4] == a[4][4] == 'o':
        finish = 1
    elif a[0][0] == a[2][2] == a[4][4] == 'x' or a[0][0] == a[2][2] == a[4][4] == 'o':
        finish = 1
    elif a[0][4] == a[2][2] == a[4][0] == 'x' or a[0][4] == a[2][2] == a[4][0] == 'o':
        finish = 1
    return finish


gems = int(input('Выбери как играть с ботом -> "1" c другом -> "2": '))
if gems == 1:
    f = 0
    while f != 1:
        field = int(input('выбери поле OT 1 ДО 9: '))
        a = motion(a, field)
        printlist(a)
        print()
        f = finish(a)
        if f == 1:
            print('Ты победил!!')
        else:
            a = bot(a)
            printlist(a)
            f = finish(a)
            if f == 1:
                print(' Увы ты проиграл!!')
else:
    f = 0
    while f != 1:
        field = int(input('Первый игрок выбери поле OT 1 ДО 9: '))
        a = motion(a, field)
        printlist(a)
        print()
        f = finish(a)
        if f == 1:
            print('Первый игрок победил!!')
        else:
            field = int(input('Второй  игрок выбери поле OT 1 ДО 9: '))
            a = motion2(a, field)
            printlist(a)
            f = finish(a)
            if f == 1:
                print('Победа второго игрока ')
