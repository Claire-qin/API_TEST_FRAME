import os
import xlrd

excel_path = os.path.join(os.path.dirname(__file__),'data/test_data.xlsx')
print(excel_path)

wb = xlrd.open_workbook(excel_path) # 创建工作簿对象
sheet = wb.sheet_by_name('Sheet1')
cell_value = sheet.cell_value(0,0)
# print(cell_value)
cell_value = sheet.cell_value(1,0)
# print(cell_value)
cell_value = sheet.cell_value(2,0) # 对于合并的左上角 首个单元格返回真实值，其他不显示
# print(cell_value)

# 处理方式：xlrd -->merged_cells
merged = sheet.merged_cells  #返回列表 [(1, 5, 0, 1),(...)]   合并单元格起始行、结束行、起始列、结束列
# 逻辑：凡是 merged_cells属性范围内的单元格，它的值都要等于 左上角
print(merged)
def get_merged_cell_value_01(row_index,col_index): #
    """只能完成合并单元格数据的获取"""
    cell_value = None
    for(rlow,rhiht,clow,chiht) in merged:
        if (row_index >= rlow and row_index < rhiht):
            if (col_index >= clow and col_index < chiht):
                cell_value = sheet.cell_value(rlow,clow)
    return cell_value
# print(get_merged_cell_value_01(3,0))

def get_merged_cell_value_02(row_index,col_index): #
    """获取普通单元格 和 合并单元格的数据"""
    cell_value = None
    for(rlow,rhiht,clow,chiht) in merged:
        if (row_index >= rlow and row_index < rhiht):
            if (col_index >= clow and col_index < chiht):
                cell_value = sheet.cell_value(rlow,clow)
                break; # 防止循环去判断出现值覆盖的情况
            else:
                cell_value = sheet.cell_value(row_index,col_index) # 列不相等
        else:
            cell_value = sheet.cell_value(row_index, col_index) # 行不相等
    return cell_value

print(get_merged_cell_value_02(4,0))



