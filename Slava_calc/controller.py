from oper import operations
import data
from view import input_data, view_data

def btm():
    num_data = (int(input_data('Первое число: ')), int(input_data('Второе число: ')))
    data.init_data(*num_data)
    znak = input_data('Укажите действие: ')
    match znak:
        case '+':
            res = operations.summ(*data.return_data())
        case '-':
            res = operations.dif(*data.return_data())
        case '*':
            res = operations.mult(*data.return_data())
        case '/':
            res = operations.div(*data.return_data())
        case _:
            res = 'NONE'

    view_data(text='Результат: ', data=res)