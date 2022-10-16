"(1+2)*3"


def parse(s):
    res = [int(i) if i.isdigit() else i for i in s]
    return res

def calc(lst):
    result = 0.0
    # op = [el for el in lst if el in ['*', '/', '+', '-']]
    while '*' in lst:
        index = lst.index('*')
        result = lst[index - 1] * lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '/' in lst:
        index = lst.index('/')
        result = lst[index - 1] / lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '+' in lst:
        index = lst.index('+')
        result = lst[index - 1] + lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '-' in lst:
        index = lst.index('-')
        result = lst[index - 1] - lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]

    return result


def brackets(lst):
    brk_lst = list(filter(lambda x: x[1] == '(' or x[1] == ')', enumerate(lst)))
    for i in range(0, len(brk_lst), 2):
        lst = lst[:brk_lst[i][0]] + [calc(lst[brk_lst[i][0] + 1:brk_lst[i + 1][0]])] \
              + lst[brk_lst[i + 1][0] + 1:]
    return lst


s = "4+6"
result = parse(s)
result = brackets(result)
print(calc(result))

# print(parse("(1+2)*3"))
