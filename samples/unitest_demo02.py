import paramunittest
import unittest

# 1)元组类型 可以
# @paramunittest.parametrized(
#     (8,5),
#     (10,20)
# )

# 2)列表类型可以
# @paramunittest.parametrized(
#     [8,5],
#     [10,20]
# )

# 3)字典类型
# @paramunittest.parametrized(
#     {'numa':8,'numb':5},
#     {'numa':10,'numb':20}
# )
# 4)函数或者数据对象 传入进去
testdata = [{'numa':8,'numb':5},{'numa':10,'numb':20},{'numa':100,'numb':66}]
def get_data():
    return [{'numa':8,'numb':5},{'numa':10,'numb':20},{'numa':100,'numb':66}]
@paramunittest.parametrized(
    # *testdata
    * get_data()
)
class UTestDemo(paramunittest.ParametrizedTestCase):
    def setParameters(self, numa,numb): # *args, **kwargs 元组 字典
        self.numa = numa
        self.numb = numb
    def test_number(self):
        print('numa=%d,numb=%d'%(self.numa,self.numb))
        self.assertGreater(self.numa,self.numb)

if __name__ == '__main__':
    unittest.main()