'''
Excel 파일 생성
'''

import openpyxl


def main():
    '''
    Excel 파일 생성
    '''

    workbook = openpyxl.Workbook()
    worksheet = workbook.create_sheet('sheet_name')

    worksheet['A1'] = 'Num'
    worksheet['B1'] = 'Name'

    worksheet['A2'] = 1
    worksheet['B2'] = 'John'
    worksheet['A3'] = 2
    worksheet['B3'] = 'James'

    workbook.save(r'excel/test.xlsx')


if __name__ == '__main__':
    main()
