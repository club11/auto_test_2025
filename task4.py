"""task4"""


# def add_one_to_list(some_list):
#     reversed_list = reversed(some_list)
#     some_list = list(reversed_list)
#     for n in some_list:
#         print(some_list.index(n))
#         if n < 9:
#             index = some_list.index(n)
#             some_list.insert(index, n + 1)
#             return some_list
#         some_list[n] = 0
#     return [1] + some_list
#
# result = add_one_to_list([1, 2, 3])
# print(result)

def add_one_to_list(some_list):
    """
    add 1
    """
    n = len(some_list)
    for i in range(n - 1, -1, -1):
        if some_list[i] < 9:
            some_list[i] += 1
            return some_list
        some_list[i] = 0
    return [1] + some_list

number = [1, 2, 3]
result = add_one_to_list(number)
print(result)
