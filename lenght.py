try:
    text = input(f'Введите строку : ')
    result = ''
    for item in text:
     if item.isalnum() and result.count(item)==0:
        result+=item
        print(f'{result}')
        if not text:
            print(f'NO')
            result = len(f'{text}')
except ValueError as e:
    print(f'Произошла ошибка: {e}')