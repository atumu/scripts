import xlrd


def read(target_code):
    workbook = xlrd.open_workbook("C:/T/08-01-Lookup精确匹配.xls")
    sheet = workbook.sheet_by_name("纵向查找")
    nrows = sheet.nrows

    companys = {}

    for index in range(1, nrows - 1):
        code = str(int(sheet.cell_value(0, index)))
        name = sheet.cell_value(1, index)
        companys[code] = name

    print(companys)

    print(companys['1009'])

    return companys[target_code] if target_code in companys.keys() else "N/A"


if __name__ == '__main__':
    target = input()
    print(read(target))
