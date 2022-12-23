from pages.isheji_c.tempCenterPage.previewPage import PerviewPage
from pages.basePage import Action

from common.readLog import Log


# ======================================================
# 爱设计首页-->模板-->预览页面
# https://qiye.isheji.com
# ======================================================

class TestPreviewPage:
    log = Log(__name__)
    logger = log.getLog()


    def test_act_temp_center(self,driver):
        '''验证进入模板中心功能'''
        PerviewPage(driver).test_act_temp_center()
        Action(driver).sleep(2)
    def test_review_temp(self, driver):
        '''验证点击模板的预览按钮功能'''
        self.logger.info("进入到首页，开始测试模板预览页面")
        PerviewPage(driver).qiye_reivew_temp()
        Action(driver).sleep()

    def test_user_temp(self, driver):
        '''验证在模板预览页面，点击立即使用进入工作台'''
        PerviewPage(driver).test_qiye_user_temp(driver)
        Action(driver).sleep()

    def test_click_reveiw_temp(self, driver):
        '''验证在模板预览页面，点击推荐的模版进入工作台'''
        PerviewPage(driver).test_click_reveiw_temp(driver)
        Action(driver).sleep()

    def test_fving_word_key(self, driver):
        '''验证在模板预览页面，点击关键词进入搜索功能'''
        PerviewPage(driver).qiey_fving_word_key()
        Action(driver).sleep()
