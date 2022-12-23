from common.sendDingTalk import SendDingTalk
from pages.basePage import Action
from common.readLog import Log
from common.getYaml import url


# =======================================
# 爱设计首页右侧导航页面
# https://misheji.wxbjq.top
# =======================================

class Navigation(Action):
    log = Log(__name__)
    logger = log.getLog()

    # 右侧导航新人福利
    def clickNewUserWelfare(self):
        '''新人有礼'''
        new_prople = ('xpath', "//div[@class='img-icon right_icon1']")
        self.click(new_prople)

    def closeNewUserWelfare(self):
        '''关闭右侧导航弹出的新人福利'''
        try:
            self.logger.info("开始测试关闭新人福利用例")
            self.clickNewUserWelfare()
            self.sleep()
            npx = ('xpath', "//img[@stats-mark='关闭新人有礼弹窗']")
            self.sleep()
            self.click(npx)
        except Exception as e:
            self.logger.error('失败：关闭右侧导航弹出的新人福利%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：关闭右侧导航弹出的新人福利")
            raise e

    # 点击个人VIP
    def clickPersonalVip(self):
        '''验证首页右侧导航：个人VIP'''
        try:
            self.logger.info("开始测试首页右侧导航：个人VIP用例")
            # self.move_to_stay("//div[@class='img-icon right_icon2']")
            vip_move = ("xpath", "//div[@class='img-icon right_icon2']")
            self.mouse_hover(vip_move)
            self.sleep(3)
            self_vip = ('xpath', "//a[@class='gr-vip']//img[@class='btn-img']")
            self.click(self_vip)
            self.sleep()
            # # 获取到页面元素断言
            number = ('xpath', "//ul[@class='payContent-card']/li[1]/div/section[2]/span")
            actual = self.getText(number)
            self.sleep(2)
            x_button = ('xpath', "//span[contains(@class,'iconfont icon-no close_button')]")
            self.click(x_button)  # 关闭支付弹框
            self.retention_window()
            assert float(actual) > 0
        except Exception as e:
            self.logger.error('失败：验证首页右侧导航：个人VIP%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：验证首页右侧导航：个人VIP")
            raise e

    def m_environment(self):
        try:
            gaoji = ('xpath', "//button[@id='details-button']")
            self.click(gaoji)
            unsafe = ('xpath', "//a[@id='proceed-link']")
            self.click(unsafe)
        except Exception as e:
            self.sleep()
            self.logger.error('我的企业：没有出现：风险提示%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("我的企业：没有出现：风险提示")
            raise e

    def clickEnterprise(self):
        '''验证首页右侧导航：点击企业VIP，进入到企业vip页面'''
        try:
            self.logger.info("开始测试点击企业VIP，进入到企业vip页面用例")
            # self.move_to_stay("//div[@class='img-icon right_icon2']")
            vip_move = ("xpath", "//div[@class='img-icon right_icon2']")
            self.mouse_hover(vip_move)
            enterprise = ('xpath', "//a[@class='qy-vip']//img[@class='btn-img']")
            self.click(enterprise)
            self.sleep()
            self.window(-1)
            url = self.get_current_url()
            assert url == "https://qiye.isheji.com/"
            self.close_handle()
        except Exception as e:
            self.logger.error('失败：首页右侧导航：点击企业VIP，进入到企业vip页面%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：首页右侧导航：点击企业VIP，进入到企业vip页面")
            raise e

    # 点击首页Logo
    def clickLogo(self):
        '''验证测试完成回到首页'''
        try:
            home_logo = ('xpath', "//img[@class='logo']")
            self.click(home_logo)
        except:
            home_logo = ('xpath', "//div[@class='header-logo']")
            self.click(home_logo)
        self.sleep()

    def applet(self):
        '''小程序'''
        try:
            # self.move_to_stay("//div[@class='fons-icons icons1']")
            applet_move = ("xpath", "//div[@class='fons-icons icons1']")
            self.mouse_hover(applet_move)
        except Exception as e:
            self.logger.error('失败：首页右侧导航：点击小程序%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：首页右侧导航：点击小程序")
            raise e


    # 点击手机端
    def clickPhone(self):
        '''联系方式'''
        try:
            self.move_to_stay("//div[@class='fons-icons icons2']")
        except Exception as e:
            self.logger.error('失败：首页右侧导航：联系方式%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：首页右侧导航：联系方式")
            raise e
        # try:
        #     self.logger.info("开始测试点击手机端按钮用例")
        #     self.home_button()
        #     phone = ('xpath', "//span[contains(text(),'手机端')]")
        #     self.click(phone)
        #     self.sleep(2)
        #     saoyisao = ('xpath', "//li[@class='icons1h']/div/p")
        #     text = self.getText(saoyisao)
        #     self.logger.info("手机扫一扫：%s" % text)
        #     assert str(text).strip() == "微信扫一扫使用"
        # except Exception as e:
        #     self.logger.error('失败：首页右侧导航：点击手机端%s' % repr(e))
        #     SendDingTalk().sendDingTalkMsg("失败：首页右侧导航：点击手机端")
        #     raise e

    # 验证点击沟通群
    def clickCommunicate(self):
        self.logger.info("开始测试点击沟通群用例")
        talk = ('xpath', "//div[@class='fons-icons icons2']")
        self.click(talk)

    # 点击收藏
    def clickCollection(self):
        self.logger.info("开始测试点击收藏用例")
        collection = ('xpath', "//div[@class='fons-icons icons4']")
        self.click(collection)
        url = self.getUrl()
        return url

    # 点击关闭收藏提示弹框
    def clickCloseCollection(self):
        self.logger.info("开始测试关闭收藏弹框用例")
        url = self.clickCollection()
        if str(url).find("f=d") > 0:
            collection_close = ('xpath', "//div[@class='shouc']/div[@class='new-tanc']/img[@class='close']")
            self.ptclick(collection_close)
        else:
            self.logger.info("收藏页面的URL错误:%s" % url)

    # 点击帮助中心
    def clickHelpCenter(self):
        try:
            self.logger.info("开始测试点击帮助中心用例")
            help_button = ('xpath', "//li[@class='icons6h ']")
            self.click(help_button)
            self.sleep()
            self.window(-1)
            tips_element = ('xpath', "//div[@class='modular']/div[1]/div[1]/span")
            tips = self.getText(tips_element)
            self.sleep(2)
            self.logger.info("在帮助中心获取到的信息%s" % tips)
            assert str(tips).strip() == "新手使用教程"
            self.logger.info("在帮助中心开始关闭浏览器")
            self.close_handle()
        except Exception as e:
            self.logger.error('失败：首页右侧导航：点击帮助中心%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：首页右侧导航：点击帮助中心")
            raise e

    def feedback(self):
        '''验证意见反馈功能是否正常使用'''
        try:
            feed_button = ('xpath', "//div[@class='img-icon right_icon0']")
            self.click(feed_button)
            self.window(-1)
            self.sleep(2)
            get_url = self.get_current_url()
            assert 'https://support.qq.com/product' in get_url
            self.close_handle()
        except Exception as e:
            self.logger.error('失败：进入意见反馈%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：进入意见反馈")
            raise e
