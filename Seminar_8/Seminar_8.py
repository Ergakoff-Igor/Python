'''
Вычислить значение выражения:
12 + 15
12 / 15
112 * 15


1. Где операторы?
2. Где числовые значения?


Уровень 1:

- 1 действие
- 2 аргумента

Уровень 2:

- Количество действие произвольное
12 + 15 - 4


Уровень 3:
- Действия имеют приоритет

12 - 4*2

Уровень 4:
- Действия разделяются скобками

(12 - 4) * 2
'''

SIMPLE_EXPRESSION = '5 * 4 / 2 + 3 + 4 * 2'


def simple_expression(string_expression: str) -> None:
    '''парсер простого выражения без скобок.
        продолжение работы на семинаре'''

    start_list = string_expression.split()
    intermediate_list = []

    if start_list[0].isdigit():
        start_list.insert(0, '+')

    result = 0

    for i in range(0, len(start_list)-1, 2):
        if start_list[i] == '*':
            multyply = int(intermediate_list[-1]) * int(start_list[i+1])
            intermediate_list[-1] = multyply
        elif start_list[i] == '/':
            division = int(intermediate_list[-1]) / int(start_list[i+1])
            intermediate_list[-1] = division
        else:
            intermediate_list.append(start_list[i])
            intermediate_list.append(start_list[i+1])

    for i in range(0, len(intermediate_list)-1, 2):
        if intermediate_list[i] == '+':
            result += int(intermediate_list[i+1])
        elif start_list[i] == '-':
            result -= int(intermediate_list[i+1])
        else:
            continue
    print(string_expression + ' = ' + str(result))


simple_expression(SIMPLE_EXPRESSION)


# COMPLEX_EXXPRESSION = '22 + 3 - 2 * ( 2 * 5 + 2 ) * 4'
# COMPLEX_EXXPRESSION = '1 + 2 * ( 3 + 2 - 6 / ( 1 + 2 ) ) * 2 + 1'
# COMPLEX_EXXPRESSION = '1 + 2 * ( 3 + 4 / 2 - ( 1 + 2 ) ) * 2 + 1'
# COMPLEX_EXXPRESSION = '1 + 2 * ( 7 - 1 + 6 / 2 - ( 1 + 2 * 2 ) ) * 2 + 1'
# COMPLEX_EXXPRESSION = '( 2 + 5 ) * ( 7 - 5 )'
# COMPLEX_EXXPRESSION = '5 * 4 / ( 2 + 3 ) + 4 * 2'
COMPLEX_EXXPRESSION = '( 10 - 5 ) * ( 2 + 3 ) - 1 + ( 4 * ( 20 - 20 / ( 5 - 1 ) ) ) * ( 2 + 7 )'


def complex_expression(expression_string: str) -> None:
    '''парсер сложных выражений со скобками'''

    OPERATOR = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
                '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}

    digits_stack = []
    symbols_stack = []

    lexems = expression_string.split()

    for symbol in lexems:
        if symbol.isdigit():
            digits_stack.append(int(symbol))
        elif symbol in OPERATOR:
            if len(symbols_stack) == 0:
                symbols_stack.append(symbol)
                continue
            if symbols_stack[-1] == '(':
                symbols_stack.append(symbol)
                continue

            while symbols_stack:
                if OPERATOR.get(symbol)[0] < OPERATOR.get(symbols_stack[-1])[0]:
                    y, x = digits_stack.pop(), digits_stack.pop()
                    digits_stack.append(OPERATOR[symbols_stack[-1]][1](x, y))
                    del symbols_stack[-1]

                elif OPERATOR.get(symbol)[0] == OPERATOR.get(symbols_stack[-1])[0]:
                    y, x = digits_stack.pop(), digits_stack.pop()
                    digits_stack.append(OPERATOR[symbols_stack[-1]][1](x, y))
                    del symbols_stack[-1]

                symbols_stack.append(symbol)
                break

        elif symbol == ')':
            while symbols_stack[-1] != '(':
                y, x = digits_stack.pop(), digits_stack.pop()
                digits_stack.append(OPERATOR[symbols_stack[-1]][1](x, y))
                del symbols_stack[-1]
            if symbols_stack[-1] == '(':
                del symbols_stack[-1]
        else:
            symbols_stack.append(symbol)

    while len(symbols_stack) > 0:
        y, x = digits_stack.pop(), digits_stack.pop()
        digits_stack.append(OPERATOR[symbols_stack[-1]][1](x, y))
        del symbols_stack[-1]

    result = digits_stack.pop()

    print(expression_string + ' = ' + str(result))


complex_expression(COMPLEX_EXXPRESSION)