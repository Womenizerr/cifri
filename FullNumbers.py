first_string = input(f'Введите первую строку')
second_string = input(f'Введите вторую строку')

first_string_lower = first_string.lower()
second_string_lower = second_string.lower()

common_characters = []
 for item in first_string_lower:
     if item in second_string_lower and item not in common_characters:
         common_characters
