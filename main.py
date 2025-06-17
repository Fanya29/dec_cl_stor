from algorithms.rc4 import *
from algorithms.huffman import *
from communication.communication import *
from tests.rc4_test import rc4_test
from tests.huffman_test import huffman_test


rc4_test()
huffman_test()
meeting()
while True:
    answer = str(input())

    if answer == 'команды':
        get_command()
    elif answer == 'архивировать':
        print('Введите путь к файлу')
        archive(str(input()))
    elif answer == 'разархивировать':
        print('Введите путь к файлу')
        unarchieve(str(input()))
    elif answer == 'шифровать' or answer == 'расшифровать':
        print('Введите путь к файлу')
        crypt(str(input()))
    elif answer == 'выйти':
        break
    else:
        print('Такой команды нет, чтобы узнать о функционале введи: команды')
    print('Задача выполнена')



