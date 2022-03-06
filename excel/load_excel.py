'''
excel 파일 불러오기
'''

import openpyxl

file_path = 'excel/test.xlsx'
workbook = openpyxl.load_workbook(file_path)
worksheet = workbook['sheet_name']

worksheet['A4'] = 3
worksheet['B4'] = 'Jihogrammer'

workbook.save(file_path)
