def bin2hex(data):
    data = f'{0 ** int(data[0])}' * (8 - len(data) % 8) + data
    new_data = ''
    for i in range(0, len(data), 8):
        char = hex(int(data[i:i+8], 2))[2:]
        if len(char) != 2:
            char = '0' + char
        new_data += char
    return new_data

def hex2bin(data):
    new_data = ''
    for i in range(0, len(data), 2):
        char = bin(int(data[i:i+2], 16))[2:]
        if len(char) != 8:
            char = '0' * (8 - len(char)) + char
        new_data += char
    k = 0
    for i in range(8):
        if new_data[i] != new_data[i+1]:
            k = i + 1
            break
    return new_data[k:]