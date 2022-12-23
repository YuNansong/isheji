from common.sendDingTalk import SendDingTalk
from pages.basePage import Action
from common.readLog import Log


class NoLoggedIn(Action):
    log = Log(__name__)
    logger = log.getLog()

    def my_design(self):
        """未登录状态点击我的设计"""
        try:
            design_button = ("xpath", "//li[@class='block-item mydesign']//span[@class='block-text']")
            self.click(design_button)
            userpdwlogin = ("xpath", "//li[@class='login-phone']//p")
            assert_login = self.getText(userpdwlogin)
            x_button = ("xpath", "//span[@class='iconfont icon-no close_button']")
            self.click(x_button)
            assert assert_login == "账号密码登录"
        except Exception as e:
            self.refresh()
            self.logger.error('失败：未登录状态点击我的设计出现登录弹窗%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：未登录状态点击我的设计出现登录弹窗")
            raise e

    def my_collection(self):
        """未登录状态点击我的收藏"""
        try:
            collection_button = ("xpath", "//li[@class='block-item mydesign']//span[@class='block-text']")
            self.click(collection_button)
            userpdwlogin = ("xpath", "//li[@class='login-phone']//p")
            assert_login = self.getText(userpdwlogin)
            x_button = ("xpath", "//span[@class='iconfont icon-no close_button']")
            self.click(x_button)
            assert assert_login == "账号密码登录"
        except Exception as e:
            self.refresh()
            self.logger.error('失败：未登录状态点击我的收藏出现登录弹窗%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：未登录状态点击我的收藏出现登录弹窗")
            raise e

    def new_user_gift(self):
        """未登录状态点击新人有礼"""
        try:
            gift_button = ("xpath", "//div[@class='img-icon right_icon1']")
            self.click(gift_button)
            userpdwlogin = ("xpath", "//li[@class='login-phone']//p")
            assert_login = self.getText(userpdwlogin)
            x_button = ("xpath", "//span[@class='iconfont icon-no close_button']")
            self.click(x_button)
            self.refresh()
            assert assert_login == "账号密码登录"
        except Exception as e:
            self.refresh()
            self.logger.error('失败：未登录状态点击新人有礼出现登录弹窗%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：未登录状态点击新人有礼出现登录弹窗")
            raise e

    def self_vip(self):
        """未登录状态点击右侧个人VIP"""
        try:
            self_vip_button = ("xpath", "//div[@class='img-icon right_icon2']")
            self.mouse_hover(self_vip_button)
            self_button = ('xpath', "//a[@class='gr-vip']//img[@class='btn-img']")
            self.click(self_button)
            userpdwlogin = ("xpath", "//li[@class='login-phone']//p")
            assert_login = self.getText(userpdwlogin)
            x_button = ("xpath", "//span[@class='iconfont icon-no close_button']")
            self.click(x_button)
            assert assert_login == "账号密码登录"
        except Exception as e:
            self.refresh()
            self.logger.error('失败：未登录状态点击右侧个人VIP出现登录弹窗%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：未登录状态点击右侧个人VIP出现登录弹窗")
            raise e

    def qiye_vip(self):
        """未登录状态点击右侧企业VIP"""
        try:
            self_vip_button = ("xpath", "//div[@class='img-icon right_icon2']")
            self.mouse_hover(self_vip_button)
            qiye_vip = ("xpath", "//a[@class='qy-vip']//img[@class='btn-img']")
            self.click(qiye_vip)
            userpdwlogin = ("xpath", "//li[@class='login-phone']//p")
            assert_login = self.getText(userpdwlogin)
            x_button = ("xpath", "//span[@class='iconfont icon-no close_button']")
            self.click(x_button)
            assert assert_login == "账号密码登录"
        except Exception as e:
            self.refresh()
            self.logger.error('失败：未登录状态点击右侧企业VIP出现登录弹窗%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：未登录状态点击右侧企业VIP出现登录弹窗")
            raise e

    def first_tempalte(self):
        """未登录状态点击模版"""
        try:
            tempalte_button = ("xpath", "//div[@class='vertical'][1]/div[@class='swiper-boxs']/div[1]/div/div[1]")
            self.click(tempalte_button)
            userpdwlogin = ("xpath", "//li[@class='login-phone']//p")
            assert_login = self.getText(userpdwlogin)
            x_button = ("xpath", "//span[@class='iconfont icon-no close_button']")
            self.click(x_button)
            assert assert_login == "账号密码登录"
        except Exception as e:
            self.refresh()
            self.logger.error('失败：未登录状态点击模版出现登录弹窗%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：未登录状态点击模版P出现登录弹窗")
            raise e
        finally:
            self.refresh()