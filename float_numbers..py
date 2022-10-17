# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
# Пример:
# o	[1.1, 1.2, 3.1, 5, 10.01] => 0.19


def diff_fract_parts(numbers):
    new_numbers = [round(x % 1, 2) for x in numbers if x % 1 != 0]
    return max(new_numbers) - min(new_numbers)


num = [1.1, 1.2, 3.1, 5, 10.01]
print(diff_fract_parts(num))
