def archive(file_code):
    frequency_table(file_code)


def frequency_table(code):
    a = {}
    for i in range(len(code)):
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
    print(a)
