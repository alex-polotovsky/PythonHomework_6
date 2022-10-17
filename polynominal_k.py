# 33). Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k и приравняйте его к нулю.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# 2*x*2 + 4*x + 5 = 0
# или
# 2*x^2 + 4*x + 5 = 0


from random import randint


def get_polinom_var(n):
    """Принимает натуральное значение степени полинома.
    Возвращает список его переменных.
    """
    pvar = [f'x^{i}' for i in range(n, 1, -1)]
    pvar.append('x')
    print('Список переменных: ', pvar)
    return pvar


def get_polinom_index(n):
    """Принимает натуральное значение степени полинома.
    Возвращает список его коэффициентов.
    """
    pind = [randint(0, 100) for i in range(n + 1)]
    if pind[0] == 0:
        pind[0] = randint(1, 100)
    pind = list(map(str, pind))
    print('Список коэффициентов: ', pind)
    return pind


def get_equation_terms(pln_ind, pln_var):
    """Принимает списки коэффициентов и переменных.
    Возвращает список членов полинома
    """
    pln_terms = list(map(lambda x, y: x + y, pln_ind, pln_var))
    pln_terms.append(pln_ind[len(pln_ind) - 1])
    print('Список членов полинома: ', pln_terms)
    return pln_terms


def create_file(text):
    """Принимает текст и создаёт файл с этим текстом.
    """
    name = input('Задайте путь к файлу: ')
    with open(name, 'w') as f:
        f.write(text)


k = int(input('Задайте натуральную степень полинома: '))

ind = get_polinom_index(k)
var = get_polinom_var(k)
terms = get_equation_terms(ind, var)
equation = ' + '.join(terms) + ' = 0'
print('Полином: ', equation)
create_file(equation)
