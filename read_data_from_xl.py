import openpyxl


def read_data():
    data = []
    workbook = openpyxl.load_workbook('test_data.xlsx')
    worksheet = workbook['testdata']
    for each_row in range(2,worksheet.max_row+1):
        email_address = worksheet.cell(each_row,1).value
        password = worksheet.cell(each_row,2).value
        user_data = (email_address,password)
        data.append(user_data)

    workbook.close()
    return data



