speak_one = input(f'Введите  строку : ')
result = ''
for item in speak_one:
    if item.isalpha() and result.count()==0:
        result+=item
    if not item.isdigit():
        print('NO')

