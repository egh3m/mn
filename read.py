import xlrd
import random


def r_column(column_number, file_address):
    loc = file_address
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    sheet.cell_value(0, 0)
    lis = list()
    for i in range(sheet.nrows):
        lis.append(sheet.cell_value(i, column_number))

    random_num = random.randint(0, len(lis)-1)
    return lis[random_num]






