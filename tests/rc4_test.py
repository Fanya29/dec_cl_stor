from algorithms.rc4 import *

def rc4_test():
    key = b"Password123"
    data = b"Attack at dawn"

    assert data== rc4(key, rc4(key, data))