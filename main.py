from algorithms.rc4 import *
from algorithms.huffman import *
from communication.communication import *


meeting()
while True:
    answer = str(input())

    if answer == 'команды':
        get_command()
    elif answer == 'архивировать':
        archive(str(input()))
    elif answer == 'разархивировать':
        unarchieve(str(input()))
    elif answer == 'выйти':
        break
    else:
        print('Такой команды нет, чтобы узнать о функционале введи: команды')