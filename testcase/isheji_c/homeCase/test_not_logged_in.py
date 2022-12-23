from pages.isheji_c.homePage.not_logged_in import NoLoggedIn
from pages.basePage import Action


class TestNoLoggedIn:

    def test_my_design(self, driver):
        """验证未登录状态点击我的设计"""
        NoLoggedIn(driver).my_design()
        Action(driver).sleep()

    def test_my_collection(self, driver):
        """验证未登录状态点击我的收藏"""
        NoLoggedIn(driver).my_collection()
        Action(driver).sleep()

    def test_new_user_gift(self, driver):
        """验证未登录状态点击新人有礼"""
        NoLoggedIn(driver).new_user_gift()
        Action(driver).sleep()

    def test_self_vip(self, driver):
        """验证未登录状态点击右侧个人VIP"""
        NoLoggedIn(driver).self_vip()
        Action(driver).sleep()

    def test_qiye_vip(self, driver):
        """验证未登录状态点击右侧企业VIP"""
        NoLoggedIn(driver).qiye_vip()
        Action(driver).sleep()

    def test_first_tempalte(self, driver):
        """验证未登录状态点击模版"""
        NoLoggedIn(driver).first_tempalte()
        Action(driver).sleep()