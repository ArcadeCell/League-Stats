from prettyTables import Table

new_table = Table()

new_table.add_column('header1', ['data1', 'data2'])
new_table.add_row(['data3', 12.4325])
new_table.add_row(['data4', 111.22])
new_table.add_row(['data5'])
new_table.add_row(['data6', .4])
new_table.add_row(['data7', 321111])
# new_table.add_row()
# new_table.add_column()
new_table.missing_value = 'missing_value__'
new_table.style_name = 'pretty_columns'
new_table.show_empty_columns = False
new_table.show_empty_rows = False
new_table.show_index = True
# new_table.show_headers = False

print(new_table)
# print(new_table.internal_rows)
print(new_table.style_name)
print(new_table.possible_styles)


# new_table.add_column('Name', ['Jade', 'John'])
# new_table.add_column('Age', [20, 30])
# new_table.add_column('Test\nResults', [9.651, 3, 245.7])
# new_table.add_row(['Piotr\nBaltimore', 27, 3.5])
# new_table.add_row(['Sam', 21])
# new_table.show_index = True
# new_table.style_name = 'pretty_columns'
# new_table.missing_value = '?'
# print(new_table)
# new_table.show_index = False
# new_table.show_headers = False
# print(new_table)
# print('row:', new_table.row_count)
# print('columns:', new_table.column_count)
# new_table.show_index = True
# print(new_table)
# print('internal_row_count:', new_table.internal_row_count)
# print('internal_column_count:', new_table.internal_column_count)
# new_table.show_empty_columns = False
# new_table.show_empty_rows = False
# new_table.show_headers = False
# new_table.missing_value = '?'
# new_table.show_index = True
# new_table.index_start = 1
# new_table.index_step = 5
# new_table.style_name = 'thin_borderline'


# new_table.add_column('i', ['Juan', 'Pedro', 'Maria', 'John', 'Elsie', 'Ramiro'])
# new_table.add_column('Age', [20, 30, 40, 50, 60, 70]),
# new_table.add_column('Registered', [True, False, True, False])
# new_table.add_column('Salary', [1651000, 2321000, 3000651, 40006581, 5651000, 665416000])
# new_table.add_column('City', ['Buenos Aires', 'Santiago', 'Buenos Aires', 'Santiago', 'Buenos Aires', 'Santiago'])
# new_table.add_column('Address', ['Calle falsa 123', 'Calle falsa 123', 'Calle falsa 123', 'Calle falsa 123', 'Calle falsa 123', 'Calle falsa 123'])
# new_table.add_column('Large Number', [100000000, 200000000, 300000000, 400000000, 500000000, 600000000])
# new_table.add_column('Large Odd Number', [1000000001, 2000000002, 3000000003, 4000000004, 5000000005, 6000000006])


# new_table.headers = ['Name', 'Age', 'Registered']
# new_table.add_row(['Juan', 20, True])
# new_table.add_row(['Pedro', 30, False])
# new_table.add_row(['Maria', 40, True])
# new_table.add_row(['John', 50, False])
# new_table.add_row(['Elsie', 60])
# new_table.add_row(['Ramiro', 70])

# new_table.add_column('Topic', ['Matter State', 'Check'])
# new_table.add_column('Borium', [1, True])
# new_table.add_column('Helium', [2, True])
# new_table.add_column('Corium', [7, False])
# new_table.add_column('Uranium', [-1, True])
# new_table.add_row(['Bus', 25, 115, 30, 31])
# new_table.add_row(['Set', 400, 2, 0, 100])
# new_table.add_row()
# new_table.add_row()
# new_table.add_row()
# new_table.add_row(['Critic Mass', False, False, False, False])
# new_table.add_row(['Critic Heat', False, False, True, True])
# new_table.add_row(['Critic Pressure', False, False, False, True])
# new_table.add_row(['Urgent Cleaning', False, False, True, False])
# new_table.add_row(['Cuadrant vals', 10, 1, 11, 12])
# new_table.add_row()
# new_table.add_row()
# new_table.add_row(['Inherent mass', 425345, -2, 453213453, 242224532])
# new_table.add_row(['Calamity count', 0, 0, 999, 0])
# new_table.add_row()
# new_table.add_row(['Calamity count', 0, 0, 999, 0])
# new_table.add_column()
# new_table.add_column()
# new_table.add_column()

# str(new_table)
# print(new_table)
# list(map(lambda x: print(len(x)), str(new_table).splitlines()))
# print('columns: ', new_table.column_count)
# print('rows: ', new_table.row_count)
# print('internal count of columns: ', new_table.internal_column_count)
# print('internal count of rows: ', new_table.internal_row_count)
# print('empty column indexes: ', new_table.empty_columns_i)
# print('empty row indexes: ', new_table.empty_rows_i)
# print('internal_headers: ', new_table.internal_headers)
# print('columns: ', new_table.columns)
# print('rows: ', new_table.rows)

