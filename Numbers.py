try:
    text = input(f'Введите строку : ')
    result = ''
    for item in text:
     if item.isdigit() and result.count(item)==0:
        result+=item
        print(f'{result}')
        if not text:
            print(f'NO')
except ValueError as e:
    print(f'Произошла ошибка: {e}')