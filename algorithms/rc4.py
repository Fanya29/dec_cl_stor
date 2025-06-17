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