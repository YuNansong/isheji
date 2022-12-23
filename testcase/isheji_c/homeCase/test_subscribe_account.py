from pages.isheji_c.homePage.subscribe_account import SubscribeAccount
from pages.basePage import Action
from common.readLog import Log


class TestSubscribeAccount:
    log = Log(__name__)
    logging = log.getLog()

    def test_info_first_picture(self, driver):
        '''验证进入公共号首图功能'''
        SubscribeAccount(driver).info_first_picture('公众号首图')
        Action(driver).sleep()

    def test_save_subscribe(self, driver):
        '''验证保存模版至公众号'''
        SubscribeAccount(driver).save_subscribe()
        Action(driver).sleep()

    def test_info_econdary_graph(self, driver):
        '''验证进入公众号次图'''
        SubscribeAccount(driver).info_first_picture('公众号次图')
        Action(driver).sleep()
        SubscribeAccount(driver).save_subscribe()
        Action(driver).sleep()

    def test_info_qr_code_previous(self, driver):
        '''验证进入横版二维码'''
        SubscribeAccount(driver).info_first_picture('横版二维码')
        Action(driver).sleep()

    def test_info_qr_code(self, driver):
        '''验证非公众号首图/次图模版保存至公众号'''
        SubscribeAccount(driver).info_qr_code()
        Action(driver).sleep()

