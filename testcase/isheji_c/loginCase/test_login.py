from pages.isheji_c.loginPage.loginPage import LoginPage
from common.getYaml import url
from common.getYaml import userinfo
from common.readLog import Log
from pages.basePage import Action

class TestLogin:
    log = Log(__name__)
    logger = log.getLog()

    def test_login(self, driver):
        '''验证用户登录功能'''
        urlInfo = url['url']['testUrl']
        if urlInfo == "https://www.isheji.com":
            username = userinfo['userinfo']['online']['vipUser']['username']
            password = userinfo['userinfo']['online']['vipUser']['password']
        elif urlInfo == "https://misheji.wxbjq.top":
            username = userinfo['userinfo']['test']['vipUser']['username']
            password = userinfo['userinfo']['test']['vipUser']['password']
        else:
            self.logger.error("用户名或者密码错误，无法登录")
        LoginPage(driver).login(username, password)
        Action(driver).sleep()
        Action(driver).refresh()

    # def test_for_login(self, driver):
    #     try:
    #         Action(driver).sleep()
    #         x_button = ("xpath", "//div[@class='new-tanc']//img[@class='close']")
    #         Action.ptclick(x_button)
    #         self.logger.info("点击关闭新人福利弹窗")
    #     except Exception as e:
    #         self.logger.info("未出现新人福利弹窗", e)