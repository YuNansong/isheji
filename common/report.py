from common.path import getTestReport
from bs4 import BeautifulSoup

class Report():

    def __init__(self):
        file = getTestReport() # 读取报告文件
        self.soup = BeautifulSoup(open(file, 'r', encoding='utf-8'), features="lxml")

    def getReportSummaryData(self):
        total_list = []
        success_list = []
        skip_list = []
        fail_list = []
        list = []

        # 总用例数
        for attr in self.soup.find_all('span', class_='text-dark'):
            total_list.append(attr.text)
        total = total_list[-1]
        # print("总用例数:",total)
        # 成功用例数
        for attr in self.soup.find_all('span', class_='text-success'):
            success_list.append(attr.text)
        success = success_list[-1]
        # print("成功用例数:",success)

        # 跳过用例数
        for attr in self.soup.find_all('span', class_='text-secondary'):
            skip_list.append(attr.text)
        skip = skip_list[0]
        # print("跳过用例数:",skip)
        # 执行失败数
        for attr in self.soup.find_all('span', class_='text-warning'):
            fail_list.append(attr.text)
        fail = fail_list[-1]
        # print("失败用例数:",fail)
        list.append(total)
        list.append(success)
        list.append(skip)
        list.append(fail)
        return list

    # 获取失败用例条数
    def getFailCaseList(self):
        fail_case = []
        warning_num = len(self.soup.select('.text-warning'))
        if warning_num > 0:
            for warning in self.soup.find_all('td', class_='text-warning'):
                exec_time = warning.find_previous()
                # print('执行时间:' + exec_time.text)
                desc = exec_time.find_previous()
                fail_case.append(desc.text)
                #print('失败用例描述:' + desc.text)
                # func = desc.find_previous()
                # print('方法:' + func.text)
                # module = func.find_previous()
                # print('用例模块:' + module.text)
                # print('执行状态:' + warning.text)
        else:
            print("暂无")
        return fail_case

# if __name__ == "__main__":
#     a = Report().getReportSummaryData()
#     b = Report().getFailCaseList()
