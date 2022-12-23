import pytest
from common.sendEmail import SendMail


if __name__ == '__main__':
    date_str = '爱设计执行用例结果'
    pytest.main([f'--report={date_str}.html',
                 '--title=爱设计UI自动化',
                 '--tester=左艺轩',
                 '--desc=如有未通过用例，可查看详细信息：查看详情',
                 '-s',
                 './testcase/suda/test_manual.py',
                 './testcase/suda/test_apicase.py'
                 ])
    mail = SendMail()
    mail.sendmail()