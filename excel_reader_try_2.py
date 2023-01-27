import openpyxl

book = openpyxl.open('C:/Users/Dmitry/Desktop/Цикл_1.xlsx', read_only = True)

sheet = book.active

print(sheet[1][0].value)

for row in range(1, sheet.max_row + 1):
    point_name = sheet[row][0].value
    date_time = sheet[row][1].value
    X_coordinate = sheet[row][2].value
    Y_coordinate = sheet[row][3].value
    Z_coordinate = sheet[row][4].value
    print(row, point_name, date_time, X_coordinate, Y_coordinate, Z_coordinate)

