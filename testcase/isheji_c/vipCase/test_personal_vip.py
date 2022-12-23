from pages.basePage import Action
from pages.isheji_c.vipPage.personalVipPage import PersonalVip
import time
# ======================================================
# 爱设计个人VIP页面相关用例
# https://www.isheji.com/vip
# ======================================================
class TestPersonalVip:

    def test_jump_url(self, driver):
        '''访问个人VIP页面'''
        Action(driver).transfer_url("/vip")
        Action(driver).sleep()
        PersonalVip(driver).close_down_tip()

    def test_clickLifeLongBtn(self, driver):
        ''' 验证在个人VIP页面，点击"开通终身VIP按钮功能"'''
        PersonalVip(driver).test_clickLifeLongBtn()
        time.sleep(1)

    def test_openvip(self, driver):
        ''' 验证在个人VIP页面，点击"开通 终身，两年，年享VIP功能"'''
        PersonalVip(driver).test_openPerVip()
        time.sleep(1)

    def test_open_company(self, driver):
        '''验证在VIP页面打开商户VIP弹框功能'''
        PersonalVip(driver).test_open_company()
        time.sleep(1)
    def test_per_company(self, driver):
        '''验证在VIP页面由商户切换到个人VIP功能'''
        PersonalVip(driver).test_per_company()
        time.sleep(1)

    # # @pytest.mark.skip(reason="企业VIP隐藏1299，2999价格不执行")
    # # def test_openEntVip(self, driver):
    # #     ''' 验证在个人VIP页面，开通企业VIP功能'''
    # #     PersonalVip(driver).test_openEntVip() # 注意循环次数
    # #     Action(driver).sleep()
    # #
    # # @pytest.mark.skip(reason="企业VIP隐藏1299，2999价格不执行")
    # # def test_switchVipTab(self, driver):
    # #     ''' 验证在个人VIP页面，打开企业VIP，切换到个人VIP功能'''
    # #     PersonalVip(driver).test_switchVipTab() # 注意循环次数
    # #   Action(driver).sleep()

    def test_timeCountdown(self, driver):
        ''' 验证在个人VIP页面，获取倒计时功能'''
        PersonalVip(driver).test_timeCountdown()
        time.sleep(1)

    def test_upgradeNow(self, driver):
        ''' 验证在个人VIP页面，点击"立即升级"功能'''
        PersonalVip(driver).test_upgradeNow()
        time.sleep(1)

    def test_easierDesign(self,driver):
        ''' 验证在个人VIP页面，点击"开通VIP，更设计轻松"功能'''
        PersonalVip(driver).test_easierDesign()
        time.sleep(1)

    def test_business(self, driver):
        ''' 验证在个人VIP页面，点击"立即升级，放心商用"功能'''
        PersonalVip(driver).test_business()
        time.sleep(1)

    def test_buyNow(self, driver):
        ''' 验证在个人VIP页面，点击"立即购买，报销无忧"功能'''
        PersonalVip(driver).test_buyNow()
        time.sleep(1)