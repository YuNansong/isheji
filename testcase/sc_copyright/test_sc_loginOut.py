"""
Author  : Milo
Time    : 2022/3/7 11:41
Desc    : 版权站切换用户的测试用例
"""
from pages.sc_copyright.sc_loginPage import SCLoginPage
from common.getYaml import scuserinfo
class TestLoginOut:

    def test_loginOut(self,driver):
        '''验证用户退出登录，切换账号登录功能'''
        SCLoginPage(driver).test_loginOut(driver)
        username = scuserinfo['userinfo']['online']['ordinary']['username']
        password = scuserinfo['userinfo']['online']['ordinary']['password']
        SCLoginPage(driver).login(username, password)