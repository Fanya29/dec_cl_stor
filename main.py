from algorithms.file_construction import *
from algorithms.huffman import *
from tests.rc4_test import *

file_path = '/Users/mac/PycharmProjects/dec_cl_stor/test_files/DSC06359.ARW'
file_name = (file_path.split('/')[-1]).split('.')[0]

data = archive(file2b(path=file_path).hex(), file_name)
print(len(data))