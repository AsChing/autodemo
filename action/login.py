
import unittest
import ddt
from autodemo.config.public_data import *
from utils import sendrequest, readexcel, writeexcel, encrypt, mysql
import configparser as cparser


token = None

@ddt.ddt
class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)

    def setUp(self):
        print('this is the setUp')

    # @ddt.data([1, 2, 3])
    # def test_1(self, value):
    #     print(value)
    #
    # '''
    #   断言成功返回结果为none，不会返回true，不会报错
    # '''
    # @ddt.data([3, 2, 1], [5, 3, 2], [10, 4, 6])
    # @ddt.unpack
    # def test_minus(self, a, b, expected):
    #     actual = int(a) - int(b)
    #     expected = int(expected)
    #     print(self.assertEqual(actual, expected))

    # @ddt.data([2, 3], [4, 5])
    # def test_compare(self, a, b):
    #     self.assertEqual(a, b)

    testdata = readexcel.ReadExcel(FILE_PATH, u"Sheet1").read_data()
    @ddt.data(*testdata)
    def test_login(self, data):
        cf = cparser.ConfigParser()
        cf.read("../config/config.ini", encoding='UTF-8')
        ip = cf.get("ip", "auction_ip")
        # for d in data:
        rowNum = int(data["casenum"].split("_")[1])+1
        if data["body"] != "":
            body = eval(data["body"])
            body["password"] = encrypt.encrpt(AUCTION_PUBLIC_KEY, body["password"])
            data["body"] = str(body)
        if data["params"] != "":
            global token
            if token is None:
                raise Exception('token is none cannot get')
            else:
                params = eval(data["params"])
                params["token"] = globals()["token"]
                data["params"] = str(params)
        res = sendrequest.HttpClient().request(ip, data)
        if res["code"] == 200:
            result = "PASS"
            if data["module"] == "登录":
                globals()["token"] = res["data"]["token"]
            elif data["module"] == "查询":
                db = mysql.MySQL()
                sql = data["sql"]
                pre = db.select(sql)
                print(type(pre[0]))
                print(type(pre))
        else:
            result = "FAIL"
        writeexcel.WriteExcel(REPORT_FILE_PATH).write_data(rowNum, result, str(res))

    def tearDown(self):
        print('this is tearDown')


'''
    verbosity是一个选项,表示测试结果的信息复杂度，有0、1、2 三个值
    0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共10个 失败2 成功8
    1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
    2 (详细模式):测试结果会显示每个测试用例的所有相关的信息
'''
if __name__ == '__main__':
    unittest.main()
