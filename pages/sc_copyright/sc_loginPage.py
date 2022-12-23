# -*- coding: utf-8 -*-
from common.readLog import Log
from common.sendDingTalk import SendDingTalk
from common.getYaml import userinfo
from element.sc_copyright.sc_login_element import SCLoginElement
from element.sc_copyright.sc_home_element import SCHomePageElement
from model.scModel.commModel import CommModel



# ======================================================
# 爱设计登录页面功能
# https://sc.isheji.com/
# ======================================================

class SCLoginPage(CommModel):
    log = Log(__name__)
    logger = log.getLog()

    def login(self, username, password):
        try:
            self.screenshot_new("01访问版权站首页")
            self.logger.info("==========测试登录用例开始==========")
            self.sleep()
            try:
                self.close_vip()
            except:
                self.logger.info("==========VIP弹框没有出现==========")
            self.click(SCHomePageElement.loginBtn_element)  # 点击首页的登录按钮
            self.sleep(1)
            self.click(SCLoginElement.tel_phone_element) # 手机号登录
            self.sleep(1)
            self.click(SCLoginElement.phone_element)  # 手机号密码登录
            self.write(SCLoginElement.usname_element, username)  # 输入用户名
            self.write(SCLoginElement.psword_element, password)  # 输入密码
            self.screenshot_new("02登录页面")
            self.click(SCLoginElement.login_button_element)  # 点击登录按钮
            self.sleep(5)
            self.saveCookie()
            self.logger.info("==========测试登录用例结束==========")
            self.screenshot_new("03登录完成后页面")
            self.sleep(2)
            try:
                self.close_vip()
            except:
                self.logger.info("==========VIP弹框没有出现==========")
        except Exception as e:
            self.logger.error("登录失败了，请立即查看: %s" % repr(e))
            SendDingTalk().sendDingTalkMsg("用户登录失败了，请立即查看")
            raise e
        self.sleep(2)

    def test_loginOut(self,driver):
        try:
            # 在首页点击个人头像
            self.click_img()
            self.click(SCHomePageElement.loginOut_element)
            self.sleep(2)
            text = self.getText(SCHomePageElement.loginBtn_element)
            assert text == "注册/登录"
        except Exception as e:
            self.logger.error("退出登录失败了，请立即查看: %s" % repr(e))
            SendDingTalk().sendDingTalkMsg("用户退出登录失败了，请立即查看")
            raise e
        self.sleep(2)

        

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
