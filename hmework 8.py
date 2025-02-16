# 1 Быки и коровы - Bulls and cows
import random

def generate_num():
    user_value = []
    loop_counter = 0
    while loop_counter < 4:
        random_val = random.randint(0, 9)
        if random_val not in user_value:
            user_value.append(random_val)
            loop_counter += 1
        else:
            pass
    return user_value


def num_get_from_user():
    data_is_correct = False
    get_data = 0
    while data_is_correct is False:
        get_data = input('Введите число из 4 '
                         'неповторяющихся цифр формата XXXX:')
        if get_data.isdigit() and len(set(list(get_data))) == 4:
            data_is_correct = True
    user_value = []
    for x in list(get_data):
        user_value.append(int(x))
    return user_value


def bulls_cows_game():
    computer_user_value = generate_num()
    print('computers number', computer_user_value)  # for dev only
    bull_counter = 0
    while bull_counter != 4:
        num_from_user = num_get_from_user()
        matched_numbers = set(computer_user_value).intersection(num_from_user)
        if matched_numbers:
            cows_num = list(matched_numbers)
            bulls_num = []
            for matched_num in matched_numbers:
                check_flag = False
                for _ in computer_user_value:
                    if (num_from_user.index(matched_num) ==
                            computer_user_value.index(matched_num)):
                        check_flag = True
                        break
                if check_flag is True:
                    bulls_num.append(matched_num)
                    cows_num.remove(matched_num)
            cows_num_output = len(cows_num)
            bulls_num_output = len(bulls_num)
            bull_counter = len(bulls_num)
            cows_name_num = ''
            bulls_name_num = ''
            if bull_counter == 4:
                print(f'Вы угадали число {computer_user_value}')
            else:
                if cows_num_output == 0:
                    cows_name = '0'
                    cows_name_num = 'коров'
                elif cows_num_output == 1:
                    cows_name = 'корова'
                    cows_name_num = 'одна'
                else:
                    cows_name = 'коровы'
                    if cows_num_output == 2:
                        cows_name_num = 'две'
                    if cows_num_output == 3:
                        cows_name_num = 'три'
                    if cows_num_output == 4:
                        cows_name_num = 'четыре'
                if bulls_num_output == 0:
                    bulls_name = 'быков'
                    bulls_name_num = '0'
                elif bulls_num_output == 1:
                    bulls_name = 'бык'
                    bulls_name_num = 'один'
                else:
                    bulls_name = 'быка'
                    if bulls_num_output == 2:
                        bulls_name_num = 'два'
                    if bulls_num_output == 3:
                        bulls_name_num = 'три'
                    if bulls_num_output == 4:
                        bulls_name_num = 'четыре'
                print(f'{cows_name_num} {cows_name}, '
                      f'{bulls_name_num} {bulls_name}')
        else:
            print('ноль коров, ноль быков')
    return


# 2 Пирамида - pyramid
# numb_given = input('введите количество:')
# for n in range(0, int(numb_given)+1):
stars_counter = 1
for n in range(1, 11):
    if n == 1:
        pyramid_str = '*'
        print(pyramid_str.center(20, ' '),
              'len = ', len(pyramid_str), 'line num = ', n)
    else:
        stars_counter += 2
        pyramid_str = '*' * stars_counter
        print(pyramid_str.center(20, ' '),
              'len = ', len(pyramid_str), 'line num = ', n)

# 3 Статуи - statues
# Для статуй = [6, 2, 3, 8] результат должен быть = 3.
# Иными словами, у Вас отсутствуют статуи размеров 4, 5 и 7

unsorted_list = [6, 2, 3, 8]
def missing_statues_counter(sorted_list):
    sorted_list.sort()
    missing_values = []
    for current_val in sorted_list[1:]:
        prev_val_index = sorted_list.index(current_val) - 1
        for some_val in range(sorted_list[prev_val_index]+1, current_val):
            missing_values.append(some_val)
    missing_values.reverse()
    #print('missing_values', missing_values)
    answer_is = len(missing_values)
    return print(f'количество недостающих статуй равно {answer_is}')


if __name__ == "__main__":
    bulls_cows_game()
    missing_statues_counter(unsorted_list)
