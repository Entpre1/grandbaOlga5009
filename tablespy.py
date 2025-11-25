from prettytable import PrettyTable

print_func = print
length = len
to_int = int
user_input = input

table = PrettyTable()
table.field_names = ['№', 'product', "price", "quantity", "finalprice"]

for i in range(3):
    product = user_input('enter product name')
    price = to_int(user_input('enter product price'))
    quantity = to_int(user_input('enter product quantity'))
    table.add_row([i+1, product, f'{price}', f'{quantity}', f'{price * quantity}'])

print_func(table)
