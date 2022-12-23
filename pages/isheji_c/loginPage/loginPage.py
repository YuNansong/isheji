# -*- coding: utf-8 -*-
from common.readLog import Log
from common.sendDingTalk import SendDingTalk
from pages.basePage import Action
from common.getYaml import userinfo
from element.isheji_c.login.loginElement import LoginElement
from element.isheji_c.home.homePageElement import HomePageElement


# ======================================================
# 爱设计登录页面功能
# https://www.isheji.com/
# ======================================================

class LoginPage(Action):
    log = Log(__name__)
    logger = log.getLog()

    def login(self, username, password):
        try:
            self.screenshot_new("01访问首页")
            self.logger.info("==========测试登录用例开始==========")
            self.sleep()
            self.click(HomePageElement.loginBtn_element)  # 点击首页的登录按钮
            self.sleep()
            self.click(LoginElement.login_phone_element)  # 切换手机密码登录弹窗
            self.sleep(2)
            self.click(LoginElement.phone_pwd_element)# 切换手机密码登录
            self.sleep(1)
            self.write(LoginElement.usname_element, username)  # 输入用户名
            self.write(LoginElement.psword_element, password)  # 输入密码
            self.click(LoginElement.login_button_element)  # 点击登录按钮
            self.sleep(5)
            mobile = self.saveCookie()
            self.sleep(3)
            #self.logger.info("手机号【%s】已登录完成" % mobile)
            self.logger.info("==========测试登录用例结束==========")
            self.screenshot_new("02登录后页面")
        except Exception as e:
            self.logger.error("登录失败了，请立即查看: %s" % repr(e))
            SendDingTalk().sendDingTalkMsg("用户登录失败了，请立即查看")
            raise e
        self.sleep(2)
        try:
            self.logger.info("==========开始关闭VIP弹框==========")
            self.click(HomePageElement.alert_element)  # 点击今日不再提醒选项
            self.sleep(2)
            try:
                self.logger.info("开始处理VIP弹框关闭(1)")
                self.click(HomePageElement.x_buttonA_element)
            except:
                try:
                    self.logger.info("开始处理VIP弹框关闭(2)")
                    self.click(HomePageElement.x_buttonB_element)
                except:
                    try:
                        self.logger.info("开始处理VIP弹框关闭(3)")
                        self.click(HomePageElement.x_buttonC_element)
                    except:
                        try:
                            self.logger.info("开始处理VIP弹框关闭(4)")
                            self.click(HomePageElement.x_buttonD_element)
                        except Exception as e:
                            self.logger.info("首页的VIP弹框无法关闭，开始刷新页面")
                            self.refresh()
                            self.refresh()
        except:
            self.logger.info("==========VIP弹框没有出现==========")
        self.logger.info("==========VIP弹框处理完成==========")
        return self

    def swith_ordinary_online(self):
        '''切换线上普通账号'''
        username = userinfo['userinfo']['online']['ordinary']['username']
        password = userinfo['userinfo']['online']['ordinary']['password']
        self.login(username, password)

    def swith_ordinary_test(self):
        '''切换测试普通账号'''
        username = userinfo['userinfo']['test']['ordinary']['username']
        password = userinfo['userinfo']['test']['ordinary']['password']
        self.login(username, password)

    def swith_longVip_online(self):
        '''切换线上终身会员'''
        username = userinfo['userinfo']['online']['longVip']['username']
        password = userinfo['userinfo']['online']['longVip']['password']
        self.login(username, password)

    def swith_longVip_test(self):
        '''切换测试终身会员'''
        username = userinfo['userinfo']['test']['longVip']['username']
        password = userinfo['userinfo']['test']['longVip']['password']
        self.login(username, password)
