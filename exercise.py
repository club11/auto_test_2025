'''
Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
Напишите программу, которая добавляет ‘ing’ к словам
В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
Напишите программу которая удаляет пробел в начале, в конце строки
Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы. Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению. "pARiS" >> "Paris"
Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
"I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него строку => "I love arrays they are my favorite"
Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6
После выполнения домашнего задания, зафиксируйте свои изменения и сделайте PR, так же как вы это делали в ДЗ по Git
'''

# 1. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
origin_string = 'www.my_site.com#about'
enhanced_string = origin_string.replace('#', '/')
print(enhanced_string, '!!!!!')

# 2. Напишите программу, которая добавляет ‘ing’ к словам
def add_ing():
    print("Enter a word or a sentence to 'ing' modify:")
    given_data = input()
    ing_added_word= ''
    if type(given_data) is str:
        ing_added_word = given_data + 'ing'
    return print('Your ing added text is:   ', ing_added_word)

add_ing()

#3. В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
ivanov_str = 'Ivanou Ivan'
lst_name, name = ivanov_str.split(' ')
ivanov_str_new = name + ' ' + lst_name
print(ivanov_str_new)

#4. Напишите программу которая удаляет пробел в начале, в конце строки
def del_space_in_string():
    print("Enter a word or a sentence to delete spaces:")
    given_data = input()
    modified_word= ''
    if type(given_data) is str:
        modified_word = given_data.strip()
    return print('Your modified text is:', modified_word)

del_space_in_string()

#5. Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы. Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению. "pARiS" >> "Paris"
wrong_name = "pARiS"
corrected_name = wrong_name.capitalize()
print(corrected_name)

#6. Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
#6.1. "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
robin_string = "Robin Singh"
robin_list = list(robin_string.split(' '))
print(robin_list)

array_string = "I love arrays they are my favorite"
array_list = list(array_string.split(' '))
print(array_list)

#7. Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus. Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
ivan_list = ['Ivan', 'Ivanou']
minsk_str = 'Minsk'
belarus_str = 'Belarus'
print(f'Привет, {ivan_list[0]} {ivan_list[1]}! Добро пожаловать в {minsk_str} {belarus_str}')

#8. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него строку => "I love arrays they are my favorite"
list_given = ["I", "love", "arrays", "they", "are", "my", "favorite"]
str_got = ' '.join(str(x) for x in list_given)
print(str_got)

#9. Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6
ten_elements_list = ['съешь', 'же', 'ещё', 'этих', 'мягких', 'французских', 'булок', 'да', 'выпей', 'чаю']
print(len(ten_elements_list))
ten_elements_list.insert(3, 'Император защищает!')
print(ten_elements_list, len(ten_elements_list))
ten_elements_list.pop(6)
print(ten_elements_list)


