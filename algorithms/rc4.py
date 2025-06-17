from algorithms.file_construction import *

def rc4(key, data):
    S = _key_schedule(key)
    keystream = _psuedo_random_generation(S)
    return bytes([x ^ next(keystream) for x in data])

def _key_schedule(key):
    S = list(x for x in range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def _psuedo_random_generation(S):
    i = j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K

def crypt(path):
    metadatas = ((path.split('/'))[-1]).split('.')
    data = file2b(metadatas[0], metadatas[1])
    print('Введите ключ для шифрования')
    crypted_data = rc4(input().encode(), data)
    b2file(crypted_data, metadatas[0], metadatas[1])
    print('Шифрование завершено')
