from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['№', 'product', "price", "quantity", "finalprice"]

for i in range(3):
    product = input('enter product name')
    price = int(input('enter product price'))
    quantity = int(input('enter product quantity'))
    table.add_row([i+1, product, f'{price}', f'{quantity}', f'{price * quantity}'])

print(table)
