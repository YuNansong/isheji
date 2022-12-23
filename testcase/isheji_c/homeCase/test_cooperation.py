from pages.isheji_c.homePage.cooperation import Cooperation
from pages.basePage import Action
from common.readLog import Log

# =====================
# 合作页面
# =====================
class TestCooperation:
    log = Log(__name__)
    logger = log.getLog()
    def test_get_coopUrl(self, driver):
        '''验证访问合作页面'''
        self.logger.info("开始执行合作页面用例/cooperation")
        Action(driver).transfer_url("/cooperation")
        Action(driver).sleep()

    def test_addServiceProvider(self, driver):
        '''验证在合作页面点击添加服务商信息'''
        Cooperation(driver).test_addServiceProvider()

    def test_open_per_vip(self, driver):
        '''验证在合作页面点击个人VIP下的立即开通按钮'''
        Cooperation(driver).test_open_per_vip(driver)
