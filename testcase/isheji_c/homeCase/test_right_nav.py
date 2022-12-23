from pages.isheji_c.homePage.rightNavigation import Navigation
from pages.basePage import Action
from pages.isheji_c.homePage.homePage import HomePage


# =======================================
# 爱设计个人VIP页面
# https://misheji.wxbjq.top/vip
#
# 普通用户执行
# =======================================

class TestRightNav:

    def test_closeNewUserWelfare(self, driver):
        '''右侧导航栏--新人福利'''
        Action(driver).transfer_url()
        Action(driver).sleep()
        Navigation(driver).closeNewUserWelfare()
        Action(driver).sleep()

    def test_feedback(self, driver):
        '''验证意见反馈功能是否正常使用'''
        Navigation(driver).feedback()
        Action(driver).sleep()

    # 右侧导航栏--个人VIP
    def test_clickPersonalVip(self, driver):
        '''验证在右侧导航打开个人VIP页面是否正确'''
        Navigation(driver).clickPersonalVip()
        # HomePage(driver).info_retain()
        Action(driver).sleep()

    # 右侧导航栏--企业VIP#暂注
    def test_clickEnterprise(self, driver):
        '''验证打开企业VIP页面是否正确'''
        Navigation(driver).clickEnterprise()
        Action(driver).sleep()

    def test_clickPhone(self, driver):
        '''验证在右侧导航小程序和联系方式'''
        Navigation(driver).applet()
        Action(driver).sleep()

    def test_clickCommunicate(self, driver):
        '''验证在右侧导航点击沟通群弹窗是否正确'''
        Navigation(driver).clickCommunicate()
        Action(driver).sleep()

    # 点击关闭收藏网站
    # def test_clickCollection(self, driver):
    #     '''验证在右侧导航点击收藏有奖跳转页面是否正确'''
    #     url = Navigation(driver).clickCollection()
    #     assert str(url).find("f=d") > 0
    #     Action(driver).sleep()
    #
    # def test_clickCloseCollection(self, driver):
    #     '''验证在点击关闭收藏有奖弹框功能是否正确'''
    #     Navigation(driver).clickCloseCollection()
    #     Action(driver).sleep()

    def test_clickHelpCenter(self, driver):
        '''验证在右侧导航点击帮助中心跳转页面是否正确'''
        Navigation(driver).clickHelpCenter()
        Action(driver).sleep()
