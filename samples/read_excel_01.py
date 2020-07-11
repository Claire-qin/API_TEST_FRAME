import os
import xlrd
from common.excel_untils import ExcelUtils

excel_path = os.path.join(os.path.dirname(__file__), '..', 'samples/data/test_data.xlsx')  # ..回到上一层
excelutils = ExcelUtils(excel_path, 'Sheet1')
# print(excelutils.get_merged_cell_value(8, 0))

sheet_list =[]
for row in range(1,excelutils.get_row_count()):
    row_dict={}
    row_dict['事件']=excelutils.get_merged_cell_value(row,0)
    row_dict['步骤序号']=excelutils.get_merged_cell_value(row,1)
    row_dict['步骤操作']=excelutils.get_merged_cell_value(row,2)
    row_dict['完成情况']=excelutils.get_merged_cell_value(row,3)
    sheet_list.append(row_dict)

# for row in sheet_list:
#     print(row)

alldata_list = []
fist_row = excelutils.sheet.row_values(0)
for row in range(1,excelutils.get_row_count()):
    row_dict = {}
    for col in range(0,excelutils.get_col_count()):
        row_dict[fist_row[col]] = excelutils.get_merged_cell_value(row,col)
    alldata_list.append(row_dict)
for row in alldata_list:
    print(row)