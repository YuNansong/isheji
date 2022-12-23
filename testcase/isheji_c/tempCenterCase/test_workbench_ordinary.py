from pages.isheji_c.tempCenterPage.workbenchPage import WorkBench
from pages.isheji_c.loginPage.exit_load import Exit_Load
from pages.isheji_c.loginPage.loginPage import LoginPage
from pages.basePage import Action
from common.readLog import Log


class TestSwithUserIntoWorkbench:
    log = Log(__name__)
    logger = log.getLog()

    def test_swith_user(self, driver):
        '''验证切换用户功能'''
        # 退出后再登录其他用户
        self.logger.info("访问爱设计首页")
        Action(driver).transfer_url()
        Action(driver).sleep()
        # 退出登录
        self.logger.info("退出现在的账号")
        Exit_Load(driver).exit_action()
        Action(driver).sleep(1)

        Action(driver).appoint_url(LoginPage(driver).swith_ordinary_online, LoginPage(driver).swith_ordinary_test)
        Action(driver).sleep()

    def test_selected(self, driver):
        '''验证在首页点击精选模版进入工作台功能'''
        self.logger.info("在首页点击精选模板，并进入到工作台")
        WorkBench(driver).test_act_workbench()
        Action(driver).sleep()

    def test_assert_risk_watermark_button(self, driver):
        '''验证普通用户进入工作台页面水印提示'''
        self.logger.info("普通用户进入工作台页面点击水印按钮")
        WorkBench(driver).test_watermark_button_value()
        Action(driver).sleep()

    def test_assert_risk_watermark_button_pay(self, driver):
        '''验证普通用户在工作台点击水印按钮是否打开VIP弹窗'''
        WorkBench(driver).test_click_watermark()
        Action(driver).sleep()
        WorkBench(driver).info_retain()
        Action(driver).sleep()

    def test_risk_button(self, driver):
        '''验证普通用户进入工作台页面风险提示是否存在'''
        self.logger.info("普通用户进入工作台页面点击风险提示")
        WorkBench(driver).test_get_risk_button_value()
        Action(driver).sleep()

    def test_risk_button_into(self, driver):
        '''验证普通用户进入工作台页面点击风险提示是否打开VIP弹窗'''
        WorkBench(driver).test_click_riskButton()
        Action(driver).sleep()
        WorkBench(driver).close_retain()
        Action(driver).sleep()

    def test_upvip_buootn(self, driver):
        '''验证升级VIP按钮'''
        self.logger.info("普通用户进入工作台页面点击升级VIP按钮")
        WorkBench(driver).test_get_upvip_button_value()
        Action(driver).sleep()

    def test_upvip_button_into(self, driver):
        '''验证升级VIP支付页面价格'''
        WorkBench(driver).test_click_upvip_button()
        Action(driver).sleep()

    def test_download_upvip_into(self, driver):
        '''验证在工作台非会员用户下载VIP模板'''
        WorkBench(driver).test_download_upvip_temp()
        Action(driver).sleep()
