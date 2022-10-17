# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# o	[2, 3, 4, 5, 6] => [12, 15, 16];
# o	[2, 3, 5, 6] => [12, 15]


def pair_product(numbers):
    product_numbers = [numbers[i] * numbers[-1 + (-i)]
                       for i in range((len(numbers)+1) // 2)]
    return product_numbers


num_1 = [2, 3, 4, 5, 6]
print(pair_product(num_1))

num_2 = [2, 3, 5, 6]
print(pair_product(num_2))
