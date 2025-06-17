from algorithms.rc4 import *

def rc4_test():
    key = b"123"
    data = b"Something"

    #дешифрованные шифрованные данные равны исходным
    assert data == rc4(key, rc4(key, data))
    assert data != rc4(key, data)

    #один и тот же ключ дает один и тот же ключевой поток
    key1 = key
    assert rc4(key, data) == rc4(key1, data)

    #разные ключи дают разные ключевые потоки
    key2 = b"124"
    assert  rc4(key2, data) != rc4(key1, data)

    #пустой поток данных равен пустому ключевому потоку
    data2 = b""
    assert data2 == rc4(key, data2)
