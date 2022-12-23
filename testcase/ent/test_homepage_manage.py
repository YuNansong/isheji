from pages.entPage.homeManage import HomepageManagement
import time
# ============================
#    我的企业用例 首页管理
# ============================
class TestHomepageManagement:

    def test_enterprise(self, driver):
        '''进入企业-首页管理'''
        HomepageManagement(driver).test_act_ent_homemange()
        time.sleep(2)

    def test_open_button(self, driver):
        '''验证开启关闭功能'''
        HomepageManagement(driver).test_open_button()
        time.sleep(2)

    def test_page_manege(self, driver):
        '''验证首页基础配置功能'''
        HomepageManagement(driver).test_page_manege()
        time.sleep(2)
    def test_aborted_input(self, driver):
        '''验证企业配置文字导航功能'''
        HomepageManagement(driver).test_aborted_input()
        time.sleep(2)

    def test_classification(self, driver):
        '''验证我的企业-首页管理分类功能'''
        HomepageManagement(driver).test_classification()

    def test_send_home(self, driver):
        '''验证企业-首页管理-发布功能分类功能'''
        HomepageManagement(driver).test_send_home()