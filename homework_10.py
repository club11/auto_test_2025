"""Homework 10"""

def solution_1(text_to_check:str):
    """
    1.  ̶И̶м̶п̶е̶р̶а̶т̶о̶р̶ ̶з̶а̶щ̶и̶щ̶а̶е̶т̶!̶ рекурсия решает
    """
    text_to_check_list = list(text_to_check)
    if '#' not in text_to_check_list:
        return ''.join(text_to_check_list)
    for n in text_to_check_list:
        if n == '#':
            if text_to_check_list.index(n) == 0:
                text_to_check_list.remove(n)
            else:
                prev_val_index = text_to_check_list.index(n) - 1
                text_to_check_list.remove(text_to_check_list[prev_val_index])
                text_to_check_list.remove(n)
    return solution_1(''.join(text_to_check_list))


def solution_2(candl, pieces_for_one_candle):
    """
    2. candles
    """
    candles_burn = 0
    rest_piec = 0
    def burn_candle(candles, num_to_divide, rest_pieces, candles_burned):
        while candles != 0:
            candles_burned += candles
            rests = candles
            candles = (rests + rest_pieces) // num_to_divide
            rest_pieces = (rests + rest_pieces) % num_to_divide
            return burn_candle(candles, num_to_divide, rest_pieces, candles_burned)
        return candles_burned
    return burn_candle(candl, pieces_for_one_candle, rest_piec, candles_burn)


def solution_3(some_str):
    """
    3. coincidence_counter
    """
    if not some_str:
        return ''
    current_el = some_str[0]
    res_list = []
    counter = 0
    for letter in some_str:
        if letter == current_el:
            counter += 1
        else:
            if counter != 1:
                step = current_el + str(counter)
            else:
                step = current_el
            res_list.append(step)
            current_el = letter
            counter = 1
    if counter != 1:
        step = current_el + str(counter)
    else:
        step = current_el
    res_list.append(step)
    return ''.join(res_list)


# 1. task 1
assert solution_1("a#bc#d") == "bd"
assert solution_1("abc#d##c") == "ac"
assert solution_1("abc##d######") == ""
assert solution_1("#######") == ""
assert solution_1("") == ""

# 2. task 2 - candles
assert solution_2(5, 2) == 9
assert solution_2(1, 2) == 1
assert solution_2(15, 5) == 18
assert solution_2(12, 2) == 23
assert solution_2(6, 4) == 7
assert solution_2(13, 5) == 16
assert solution_2(2, 3) == 2

# 3. task 3 - coincidence_counter
assert solution_3("cccbba") == "c3b2a"
assert solution_3("abeehhhhhccced") == "abe2h5c3ed"
assert solution_3("aaabbceedd") == "a3b2ce2d2"
assert solution_3("abcde") == "abcde"
assert solution_3("aaabbdefffff") == "a3b2def5"


if __name__ == "__main__":
    pass
