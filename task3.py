# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc


def coding(my_list):
    new_str = ''
    caunt = 1
    for i in range(0, len(my_list)-1):
        if my_list[i] == my_list[i+1]:
            caunt += 1
        else:
            new_str += str(caunt) + my_list[i]
            caunt = 1
    new_str += str(caunt) + my_list[i+1]
    #new_list = []
    #i = 0
    # while i < len(my_list):
    #     new_list.append(str(my_list.count(my_list[i])))
    #     new_list.append(my_list[i])
    #     i += my_list.count(my_list[i])
    # new_list = ''.join(new_list)
    print(f'сжатый техт: {new_str}')
    with open('coding.txt', 'w') as cod:
        cod.write(new_str)


def decoding(fail):
    new_text = ''
    my_list = list(fail)
    caunt = 0
    for i in range(len(my_list)):
        if my_list[i].isdigit():
            caunt += int(my_list[i])
        else:
            new_text += my_list[i] * caunt
            caunt = 0
    print(f'Востановленный техт: {new_text}')
    with open('decoding.txt', 'w') as decod:
        decod.write(new_text)


with open('text.txt', 'r', encoding='UTF-8') as text:
    my_list = text.read()
print(f'техт для кодирования: {my_list}')
coding(my_list)

with open('coding.txt', 'r', encoding='UTF-8') as cod:
    fail = cod.read()

decoding(fail)

