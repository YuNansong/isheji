'''
    企业登录页面测试
'''
from pages.entPage.entLoginPage import QiyeLogin
from pages.basePage import Action
from common.readLog import Log

class TestEntHome:
    log = Log(__name__)
    logger = log.getLog()

    # #不测试首页开启
    # def test_act_qiye_home(self, driver):
    #     '''测试进入到企业介绍页面'''
    #     self.logger.info("开始访问爱设计ConTech页面")
    #     QiyeHomePage(driver).test_act_qiye_home()
    #     Action(driver).sleep(1)

    def test_login_username_error(self,driver):
        '''测试登录错误的用户名'''
        QiyeLogin(driver).test_login_username_error()
        Action(driver).sleep(1)

    def test_login_username_empty(self,driver):
        '''测试登录用户名为空的情况'''
        QiyeLogin(driver).test_login_username_empty()
        Action(driver).sleep(1)

    def test_ktkLogin_password_empty(self,driver):
        '''测试登录密码为空的情况'''
        QiyeLogin(driver).test_ktkLogin_password_empty()
        Action(driver).sleep(1)

    def test_ktkLogin_password_error(self,driver):
        '''测试登录手机号不存在的情况'''
        QiyeLogin(driver).test_ktkLogin_password_error()
        Action(driver).sleep(1)

    def test_ktkLogin_userandpass_error(self,driver):
        '''测试登录手机号正确，密码错误的情况'''
        QiyeLogin(driver).test_ktkLogin_userandpass_error()
        Action(driver).sleep(1)

    # 邮箱登录邮箱与密码都为空
    def test_login_email_all_empty(self,driver):
        '''验证邮箱登录邮箱与密码都为空'''
        QiyeLogin(driver).test_login_email_all_empty()
        Action(driver).sleep(1)

    # 邮箱登录邮箱为空
    def test_login_email_email_empty(self,driver):
        '''验证邮箱登录邮箱为空'''
        QiyeLogin(driver).test_login_email_email_empty()
        Action(driver).sleep(1)

    # 邮箱登录邮箱不符合规则
    def test_login_email_format_error(self,driver):
        '''验证邮箱登录邮箱不符合规则'''
        QiyeLogin(driver).test_login_email_format_error()
        Action(driver).sleep(1)

    # 邮箱登录密码为空
    def test_login_email_password_empty(self,driver):
        '''验证邮箱登录密码为空'''
        QiyeLogin(driver).test_login_email_password_empty()
        Action(driver).sleep(1)

    # 邮箱登录邮箱与密码错误
    def test_login_email_error(self,driver):
        '''验证邮箱登录邮箱与密码错误'''
        QiyeLogin(driver).test_login_email_error()
        Action(driver).sleep(1)

    # 邮箱-登录邮箱不存在
    def test_login_email_non_exist(self,driver):
        '''验证邮箱-登录邮箱不存在'''
        QiyeLogin(driver).test_login_email_non_exist()
        Action(driver).sleep(1)

    # 邮箱登录邮箱与密码正确
    def test_login_email_ok(self,driver):
        '''验证邮箱登录邮箱与密码正确'''
        QiyeLogin(driver).test_login_email_ok(driver)
        Action(driver).sleep(1)

    # 退出登录
    def test_login_out(self,driver):
        '''验证退出登录'''
        QiyeLogin(driver).test_login_out(driver)
        Action(driver).sleep(3)

    def test_qiye_login(self,driver):
        '''测试正确的用户名密码'''
        username = "13122222222"
        password = "111111"
        QiyeLogin(driver).ktkLogin_succ(driver,username,password)
        Action(driver).sleep(1)