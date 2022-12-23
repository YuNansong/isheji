'''
 企业登录页面
'''
from common.readLog import Log
from common.sendDingTalk import SendDingTalk
from element.ent.entIndexElement import EntIndexElement
from model.entModel.entLoginModel import EntLoginModel

class QiyeLogin(EntLoginModel):
    log = Log(__name__)
    logger = log.getLog()

    # 手机号错误
    def test_login_username_error(self):
        try:
            try:
                self.click_loginBtn() # 点击登录注册按钮
            except:
                self.logger.info("登录按钮没有出现")
            self.input_userName("2423423") # 输入手机号
            self.input_password("111111") # 输入密码
            self.sureLogin()
            errorUsername = self.error_userName()
            assert str(errorUsername).strip() == "请输入正确的手机号"
        except Exception as e:
            self.logger.info("企业首页登录出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试企业首页登录手机号错误的情况失败")
            raise e

    # 手机号空的
    def test_login_username_empty(self):
        try:
            self.refresh() # 切换到密码登录
            self.input_userName("") # 输入手机号
            self.input_password("111111") # 输入密码
            self.sureLogin()
            errorUsername = self.error_userName()
            assert str(errorUsername).strip() == "请输入手机号"
        except Exception as e:
            self.logger.info("企业首页登录出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试企业首页登录手机号空的情况失败")
            raise e

    # 密码为空
    def test_ktkLogin_password_empty(self):
        try:
            self.refresh() # 切换到密码登录
            self.input_userName("13522221111") # 输入手机号
            self.input_password("") # 输入密码
            self.sureLogin()
            errorPassword = self.error_password()
            assert str(errorPassword).strip() == "请输入密码"
        except Exception as e:
            self.logger.info("企业首页登录出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试企业首页登录密码为空的情况失败")
            raise e

    # 手机号不存在
    def test_ktkLogin_password_error(self):
        try:
            self.refresh() # 切换到密码登录
            self.input_userName("16619783411") # 输入手机号
            self.input_password("111111") # 输入密码
            self.sureLogin()
            tips = self.get_tips_error()
            assert tips == "手机号不存在"
        except Exception as e:
            self.logger.info("企业首页登录出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试企业首页登录手机号不存在的情况失败")
            raise e

    # 密码错误
    def test_ktkLogin_userandpass_error(self):
        try:
            self.refresh() # 切换到密码登录
            self.input_userName("16619783425") # 输入手机号
            self.input_password("123456") # 输入密码
            self.sureLogin()
            tips = self.get_tips_error()
            assert tips == "密码错误"
        except Exception as e:
            self.logger.info("测试企业首页登录【密码错误】出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试企业首页登录密码错误的情况失败")
            raise e

    # 正确的手机号密码
    def ktkLogin_succ(self,driver,username,password):
        try:
            try:
                self.click_loginBtn()
            except:
                self.logger.info("首页的登录按钮没有出现")
            self.sleep(3)
            self.input_userName(username) # 输入手机号
            self.input_password(password) # 输入密码
            self.sureLogin()
            self.sleep(3)
            self.saveCookie() # 保存token
            assert str(self.getText(EntIndexElement.qiye_vip_xpath)) == "企业VIP"
        except Exception as e:
            self.logger.info("企业首页登录出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试企业首页登录正确的用户名密码的情况失败")
            raise e

    # 退出登录
    def test_login_out(self,driver):
        try:
            self.click(EntIndexElement.head_img_xpath)
            self.sleep(2)
            self.click(EntIndexElement.logout_xpath)
        except Exception as e:
            self.logger.info("企业首页退出登录%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试业首页退出登录失败")
            raise e

    # ======================
    # 测试邮箱登录
    # ======================

    # 邮箱登录邮箱与密码都为空
    def test_login_email_all_empty(self):
        try:
            self.refresh()
            self.click_email_tab()
            self.input_email("")
            self.input_password("")
            self.sureLogin()
            # 断言：
            email_tips = self.error_email()
            password_tips = self.error_password()
            assert email_tips == "请输入邮箱"
            assert password_tips == "请输入密码"
        except Exception as e:
            self.logger.info("企业首页登录出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试企业首页登录正确的用户名密码的情况失败")
            raise e

    # 邮箱登录邮箱为空
    def test_login_email_email_empty(self):
        try:
            self.refresh()
            self.click_email_tab()
            self.input_email("")
            self.input_password("111222")
            self.sureLogin()
            # 断言：
            tips = self.error_email()
            assert tips == "请输入邮箱"
        except Exception as e:
            self.logger.info("企业首页邮箱登录邮箱为空出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试企业首页登录邮箱登录邮箱为空失败")
            raise e

    # 邮箱登录邮箱不符合规则
    def test_login_email_format_error(self):
        try:
            self.refresh()
            self.click_email_tab()
            self.input_email("24242@")
            self.input_password("111222")
            self.sureLogin()
            # 断言：
            tips = self.error_email()
            assert tips == "请输入正确的邮箱"
        except Exception as e:
            self.logger.info("企业首页邮箱登录邮箱不符合规则出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试企业首页邮箱登录邮箱不符合规则失败")
            raise e

    # 邮箱登录密码为空
    def test_login_email_password_empty(self):
        try:
            self.refresh()
            self.click_email_tab()
            self.input_email("4234234@qq.com")
            self.input_password("")
            self.sureLogin()
            # 断言：
            tips = self.error_password()
            assert tips == "请输入密码"
        except Exception as e:
            self.logger.info("企业首页邮箱登录密码为空出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试企业首页邮箱登录密码为空失败")
            raise e

    # 邮箱登录邮箱与密码错误
    def test_login_email_error(self):
        try:
            self.refresh()
            self.click_email_tab()
            self.input_email("13111532764@qq.com") # 邮箱必须存在
            self.input_password("1212423")
            self.sureLogin()
            # 断言：
            tips = self.get_tips_error()
            assert tips == "密码错误"
        except Exception as e:
            self.logger.info("企业首页邮箱登录邮箱与密码错误出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试企业首页邮箱登录邮箱与密码错误失败")
            raise e

        # 邮箱-登录邮箱不存在
    def test_login_email_non_exist(self):
        try:
            self.refresh()
            self.click_email_tab()
            self.input_email("3232311@qq.com") # 邮箱必须存在
            self.input_password("1212423")
            self.sureLogin()
            # 断言：
            tips = self.get_tips_error()
            assert str(tips).strip() == "邮箱不存在"
        except Exception as e:
            self.logger.info("企业首页邮箱-登录邮箱不存在出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试企业首页邮箱-登录邮箱不存在失败")
            raise e

    # 邮箱登录邮箱与密码正确
    def test_login_email_ok(self,driver):
        try:
            self.refresh()
            self.click_email_tab()
            self.sleep(1)
            self.input_email("zhaomiao@microdreams.com")
            self.sleep(2)
            self.input_password("111111")
            self.sureLogin()
            # self.sleep(2)
            # QiyeHomePage(driver).click_gaoji()
            # 断言：
            self.sleep(3)
            assert str(self.getText(EntIndexElement.qiye_vip_xpath)) == "企业VIP"
            url = self.get_qiye_url()
            SendDingTalk().sendDingTalkMsg(f'当前企业地址{url}')
        except Exception as e:
            self.logger.info("企业首页邮箱登录邮箱与密码正确出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试企业首页邮箱登录邮箱与密码正确失败")
            raise e