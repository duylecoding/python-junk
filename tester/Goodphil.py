import xlrd
import xlwt


def fix_data():
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Sheet 1", cell_overwrite_ok=True)

    sheet1.write(0, 0, 'Name')
    sheet1.write(0, 1, 'Name')
    sheet1.write(0, 2, 'Needs a ride')
    sheet1.write(0, 3, 'Destination')
    sheet1.write(0, 4, 'Can drive but would pref a ride')

    r_index = 1
    c_index = 2
    for x in range(1, row):
        for y in range(1, col):
            if y == 13:
                if data[x][y] == 'YES, I\'m carpooling with PhilSA' and data[x][y+1] == 'I don\'t have a vehicle --> someone take me please':
                    sheet1.write(r_index, 0, data[x][1])
                    sheet1.write(r_index, 1, data[x][2])
                    sheet1.write(r_index, 2, 'yes')
                    sheet1.write(r_index, 3, data[x][19])
                    sheet1.write(r_index, 5, data[x][6])
                    r_index = r_index + 1
                if data[x][y] == 'YES, I\'m carpooling with PhilSA' and data[x][y+1] == 'I have a vehicle --> I\'d rather be a passenger':
                    sheet1.write(r_index, 0, data[x][1])
                    sheet1.write(r_index, 1, data[x][2])
                    sheet1.write(r_index, 2, 'yes')
                    sheet1.write(r_index, 3, data[x][19])
                    sheet1.write(r_index, 4, 'True')
                    sheet1.write(r_index, 5, data[x][6])
                    r_index = r_index + 1
        c_index = 0
    book.save("goodphil_revised.xls")


def load_data():
    workbook = xlrd.open_workbook('goodphil.xlsx')
    worksheet = workbook.sheet_by_index(0)
    global row
    global col
    row = worksheet.nrows
    col = worksheet.ncols

    global data
    data = []

    for x in range(0, row):
        data.append([])
        for y in range(0, col):
            data[x].append(worksheet.cell(x, y).value)


if __name__ == '__main__':
    load_data()
    fix_data()
    #17 is- Yes, I would love to ride and/or provide rides for my PhilSA-onians
    # 13- YES, I'm carpooling with PhilSA
