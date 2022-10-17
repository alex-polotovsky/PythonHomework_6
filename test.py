"(1+2)*3"

from copy import copy


def parse(input_str):
    res = [int(i) if i.isdigit() else i for i in input_str]
    return res


def calc(lst):
    edit_lst = copy(lst)
    res = 0
    op_prod_div = list(filter(lambda x: x[1] == '*' or x[1] == '/', enumerate(lst)))

    for i in range(len(op_prod_div)):
        if op_prod_div[i][1] == '*':
            res = lst[op_prod_div[i][0] - 1] * lst[op_prod_div[i][0] + 1]
        else:
            res = lst[op_prod_div[i][0] - 1] / lst[op_prod_div[i][0] + 1]
        if i == 0:
            edit_lst = edit_lst[:op_prod_div[i][0] - 1] + [res] + \
                       edit_lst[op_prod_div[i][0] + 2:]
        else:
            edit_lst = edit_lst[:op_prod_div[i][0] - 3] + [res] + \
                       edit_lst[op_prod_div[i][0]:]

    op_sum_diff = list(filter(lambda x: x[1] == '+' or x[1] == '-', enumerate(lst)))

    for i in range(len(op_sum_diff)):
        if op_sum_diff[i][1] == '+':
            res = lst[op_sum_diff[i][0] - 1] + lst[op_sum_diff[i][0] + 1]
        else:
            res = lst[op_sum_diff[i][0] - 1] - lst[op_sum_diff[i][0] + 1]
        if i == 0:
            edit_lst = edit_lst[:op_sum_diff[i][0] - 1] + [res] + \
                       edit_lst[op_sum_diff[i][0] + 2:]
        else:
            edit_lst = edit_lst[:op_sum_diff[i][0] - 3] + [res] + \
                       edit_lst[op_sum_diff[i][0]:]
    return res


def brackets(lst):
    brk_lst = list(filter(lambda x: x[1] == '(' or x[1] == ')', enumerate(lst)))
    for i in range(0, len(brk_lst), 2):
        lst = lst[:brk_lst[i][0]] + \
              [calc(lst[brk_lst[i][0] + 1:brk_lst[i + 1][0]])] + \
              lst[brk_lst[i + 1][0] + 1:]
    return lst


USER_STR = "8*2/4"
result = parse(USER_STR)
result = brackets(result)
print(calc(result))

# print(parse("(1+2)*3"))
