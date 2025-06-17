from algorithms.huffman import *
from algorithms.encoder import *

def huffman_test():
    data_hex = '01ff'
    data_bin = '111111111'
    assert bin2hex(data_bin) == data_hex

    data_bin = '11'
    data_hex = '3'
    assert hex2bin(data_hex) == data_bin