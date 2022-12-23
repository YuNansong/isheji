from pages.basePage import Action
from pages.sc_copyright.sc_per_ent_vip import PerEntVIP

class TestVIP:

    def test_per_vip_price(self, driver):
        '''验证个人VIP价格是否正确'''
        PerEntVIP(driver).test_per_vip_price(1,4)
        Action(driver).sleep()

    def test_per_vip_price_table(self, driver):
        '''验证个人VIP页面表格打开弹窗价格是否正确'''
        PerEntVIP(driver).test_per_vip_price_table(2,5)
        Action(driver).sleep()

    def test_ent_vip(self, driver):
        '''验证企业VIP价格是否正确'''
        PerEntVIP(driver).test_ent_vip(1,3)
        Action(driver).sleep()

    def test_ent_vip_price_table(self, driver):
        '''验证企业VIP页面表格打开弹窗价格是否正确'''
        PerEntVIP(driver).test_ent_vip_price_table(2,4)
        Action(driver).sleep()

    def test_buy_package_sheet(self, driver):
        '''验证购买单张图片价格是否正确'''
        PerEntVIP(driver).test_buy_package_sheet()
        Action(driver).sleep()

    def test_buy_package_single(self, driver):
        '''验证购买单条视听价格是否正确'''
        PerEntVIP(driver).test_buy_package_single()
        Action(driver).sleep()