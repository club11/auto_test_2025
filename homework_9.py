"""Homework 9"""
def solution(sequence) :
    """1. Последовательность"""
    if len(sequence) == 1:
        return print('True'), True
    sequence_disturb = len(sequence) - len(set(sequence))
    prev_val = 0
    for el in sequence:
        current_val = el
        if current_val < prev_val:
            sequence_disturb += 1
            if sequence_disturb >= 2:
                return print('False'), False
        prev_val = max(prev_val, el)
    return print('True'), True


def solution_two(n, f_number):
    """2. Число напротив"""
    step = n/2
    looking_num = step + f_number
    if looking_num < 10:
        print('looking_num =', looking_num)
        return looking_num
    looking_num -= n
    print('looking_num =', looking_num)
    return looking_num


def card_validate():
    """3. Validate - Алгоритм Луна"""
    def luhn_check(digit_val_list):
        odd_digits = digit_val_list[-1::-2]
        even_digits = digit_val_list[-2::-2]
        sum_to_double_odd_digits = sum(odd_digits)
        sum_to_double_even_digits = 0
        for d in even_digits:
            control_val  = d * 2
            if control_val > 9:
                control_val -= 9
            sum_to_double_even_digits += control_val
        control_summ = sum_to_double_even_digits + sum_to_double_odd_digits
        # print('control_summ =', control_summ )
        return control_summ
    list_numbers = []
    while True:
        card_number = input('введите номер карты:')
        if card_number.isdigit():
            for dig in card_number:
                list_numbers.append(int(dig))
            break
    # а_дачу_маму_билеты_мы_переживём = luhn_check(list_numbers) % 10
    # if not а_дачу_маму_билеты_мы_переживём = luhn_check(list_numbers) % 10
    if not luhn_check(list_numbers) % 10:
        return print('карта валидна')
    return print('карта не валидна')


if __name__ == "__main__":
    solution([1, 2, 3, 4, 5, 3, 5, 6])
    assert solution_two(10, 2) == 7
    card_validate()
