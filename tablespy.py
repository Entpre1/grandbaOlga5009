from prettytable import PrettyTable as МилаяТаблица
печатать = print
лен = len
инт = int
вводотпользователя = input
чек = МилаяТаблица()
чек.field_names = ['№', 'product', "price", "quantity", "finalprice"]

for i in range(3):
    продукт = вводотпользователя('enter product name')
    цена = инт(вводотпользователя('enter product price'))
    количество = инт(вводотпользователя('enter product quantity'))
    чек.add_row([i+1, продукт, f'{цена}', f'{количество}', f'{цена*количество}'])
    

печатать(чек)
