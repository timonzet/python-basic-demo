"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(numbers):
    filter_list = []
    for number in numbers:
        for i in range(2, (number//2)+1):
            if number % i == 0:
                return False
        return filter_list.append(number)


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == 'odd':
        return [number for number in numbers if number % 2 != 0]
    if filter_type == 'even':
        return [number for number in numbers if number % 2 == 0]
    if filter_type == 'prime':
        return is_prime(numbers)


filter_numbers([1, 2, 3], ODD)