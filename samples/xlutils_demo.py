import os,xlrd
from xlutils.copy import copy

excel_path = os.path.join(os.path.dirname(__file__),'data/test_data.xls')
wb = xlrd.open_workbook(excel_path,formatting_info=True) # 先转成2003版本文件。创建工作簿对象.formatting_info=True 防止格式丢失
# print(wb.sheet_names().index('Sheet1'))  # 通过表格名称获取sheet下标

new_workbook = copy(wb) # new_workbook 已经变成可写的对象 xlwt对象
sheet = new_workbook.get_sheet(wb.sheet_names().index('Sheet1')) # 不能用sheet_by_name('Sheet1')和.sheet_by_index方法
sheet.write(1,3,60)
new_workbook.save(excel_path)
