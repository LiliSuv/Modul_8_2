def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    global n
    n = 0
    for number in numbers:
        try:
            result += number
            n += 1
        except TypeError:
            print (f'Некорректный тип данных для подсчёта суммы - {number}')
            incorrect_data += 1
    return [result, incorrect_data]


def calculate_average(numbers):
    try:
        a = personal_sum (numbers)[0] / n
    except ZeroDivisionError:
        return 0
    except TypeError:
        print (f'В numbers записан некорректный тип данных')
        return None
    else:
        return a


print (f'Результат 1: {calculate_average ("1, 2, 3,'e'")}')
print (f'Результат 2: {calculate_average ([1, "Строка", 3, "Ещё Строка"])}')
print (f'Результат 3: {calculate_average (567)}')
print (f'Результат 4: {calculate_average ([42, 15, 36, 13])}')

