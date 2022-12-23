from pages.basePage import Action
from pages.isheji_c.homePage.user_core import UserCore


class TestUserCore:

    def test_user_head_portrait(self, driver):
        '''验证个人中心点击账号设置功能'''
        # Action(driver).transfer_url()
        # Action(driver).sleep()
        UserCore(driver).user_head_portrait()
        Action(driver).sleep()

    def test_nickname(self, driver):
        '''验证个人中心查看账户信息功能'''
        UserCore(driver).nickname()
        Action(driver).sleep()

    def test_user_security(self, driver):
        '''验证个人中心进入账户安全列表功能'''
        UserCore(driver).user_security()
        Action(driver).sleep()

    def test_my_order(self, driver):
        '''验证个人中心进入我的订单列表'''
        UserCore(driver).my_order()
        Action(driver).sleep()

    def test_apply_invoice(self, driver):
        '''验证申请发表功能'''
        UserCore(driver).apply_invoice()
        Action(driver).sleep()
