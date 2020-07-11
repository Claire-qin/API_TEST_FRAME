# 1、根据在github上的实例excel文件，利用xlrd模块读取第2列的所有数据
# import os
# import xlrd
#
# excel_path = os.path.join(os.path.dirname(__file__),'data/test_data.xlsx')
# wb = xlrd.open_workbook(excel_path)
# sheet = wb.sheet_by_name('Sheet1')
# print(sheet.col_values(1))

# 2、根据在github上的实例excel文件，编写一个方法，方法参数为单元格的坐标（x,y），如果给的坐标是合并的单元格，输出此单元格是合并的，否则，输出普通单元格
# import os
# import xlrd
#
# excel_path = os.path.join(os.path.dirname(__file__),'data/test_data.xlsx')
# wb = xlrd.open_workbook(excel_path)
# sheet = wb.sheet_by_name('Sheet1')
#
# merged = sheet.merged_cells
# def is_merged_cell(row_index,col_index): # 是否是合并单元格
#     cell_value = None
#     for (row_min,row_max,col_min,col_max) in merged:
#         if (row_index >= row_min and row_index < row_max) :
#             if (col_index >= col_min and col_index < col_max):
#                 cell_value = sheet.cell_value(row_min, col_min)
#                 return True  # 找到就跳出
#     return False # 没有找到，全部遍历再跳出
#
# print(is_merged_cell(9,0))
# 3、把完成情况这一列数据改为60、90、100、40，用xlrd模块取出来之后，进行降序排序输出
import os
import xlrd

excel_path = os.path.join(os.path.dirname(__file__),'data/test_data.xlsx')
wb = xlrd.open_workbook(excel_path)
sheet = wb.sheet_by_name('Sheet1')
values = sheet.col_values(3)[1:5]
cell_values = list(map(int,values))
cell_values.sort(reverse = True)
print(cell_values)



