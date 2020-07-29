import os
import xlrd

class ExcelUtils():
    def  __init__(self,file_path,sheet_name):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()  # 整个表格对象。构造里直接调方法

    def get_sheet(self):
        wb = xlrd.open_workbook(self.file_path)
        sheet = wb.sheet_by_name(self.sheet_name)
        return sheet

    def get_row_count(self):
        row_count = self.sheet.nrows
        return row_count

    def get_col_count(self):
        col_count = self.sheet.ncols
        return col_count

    def __get_cell_value(self,row_index, col_index):
        cell_value = self.sheet.cell_value(row_index, col_index)
        return cell_value

    def get_merged_info(self):
        merged_info = self.sheet.merged_cells
        return merged_info

    def get_merged_cell_value(self,row_index, col_index):  #
        """获取普通单元格 和 合并单元格的数据"""
        cell_value = None
        for (rlow, rhiht, clow, chiht) in self.get_merged_info():
            if (row_index >= rlow and row_index < rhiht):
                if (col_index >= clow and col_index < chiht):
                    cell_value = self.__get_cell_value(rlow, clow)
                    break;  # 防止循环去判断出现值覆盖的情况
                else:
                    cell_value = self.__get_cell_value(row_index, col_index)  # 列不相等
            else:
                cell_value = self.__get_cell_value(row_index, col_index)  # 行不相等
        return cell_value

    def get_sheet_data_by_dict(self):
        """
        """
        alldata_list = []
        fist_row = self.sheet.row_values(0)  # 获取首行数据
        for row in range(1, self.get_row_count()):
            row_dict = {}
            for col in range(0, self.get_col_count()):
                row_dict[fist_row[col]] = self.get_merged_cell_value(row, col)
            alldata_list.append(row_dict)
        return alldata_list

if __name__ ==  '__main__':
    excel_path = os.path.join(os.path.dirname(__file__), '..','samples/data/test_case.xlsx')  #  ..回到上一层
    excelutils = ExcelUtils(excel_path,'Sheet1')
    for row in excelutils.get_sheet_data_by_dict():
        print(row)
    # i = 0
    # for row in excelutils.get_sheet_data_by_dict():
    #     if row['测试用例编号'] == 'case01' and row['测试用例步骤'] == 'step_01':
    #         break
    #     else:
    #         i = i+1
    # print(i+1)
    #
    # testdatas = excelutils.get_sheet_data_by_dict()
    # for j in range(len(testdatas)):
    #     if testdatas[j]['测试用例编号'] == 'case01' and testdatas[j]['测试用例步骤'] == 'step_01':
    #         break
    # print(j+1)