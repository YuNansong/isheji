"""
Author  : Milo
Time    : 2022/3/1 11:41
Desc    : 版权站登录的测试用例
"""
from pages.sc_copyright.sc_loginPage import SCLoginPage
from common.getYaml import scuserinfo

class TestLogin:

    def test_sc_login(self, driver):
        '''验证用户登录功能'''
        username = scuserinfo['userinfo']['online']['vipUser']['username']
        password = scuserinfo['userinfo']['online']['vipUser']['password']
        SCLoginPage(driver).login(username, password)
