import action
import view
import initiation
def button_click() -> int:
    val_a = view.get_value()
    my_sign = view.sign()
    val_b = view.get_value()
    initiation.init(val_a, val_b)
    match my_sign:
        case '+':   
            result = action.summ(val_a, val_b)
        case '-':   
            result = action.diff(val_a, val_b)   
        case '*':   
            result = action.mult(val_a, val_b)
        case '/':   
            result = action.div(val_a, val_b)
        case _:
            result = 'None'
    view.view_data(result)

