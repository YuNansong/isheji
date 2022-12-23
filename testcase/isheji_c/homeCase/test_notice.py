from pages.isheji_c.homePage.notice import Notice
from pages.basePage import Action


class TestNotice:

    def test_small_bell(self, driver):
        '''验证进入消息通知功能'''
        Action(driver).transfer_url()
        Action(driver).sleep()
        Notice(driver).small_bell()
        Action(driver).sleep()
