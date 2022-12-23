from pages.isheji_c.tempCenterPage.tempSpecial import TempSpecial
from common.readLog import Log
from pages.basePage import Action

# ======================================================
# 爱设计首页-->模板-->专题页面
# https://www.isheji.com/template_column_10_8
# ======================================================

class TestTempSpecial:
    log = Log(__name__)
    logger = log.getLog()
    def test_click_hotTemp(self, driver):
        '''在首页点击模板专题'''
        self.logger.info("进入到首页，测试模板专题页面")
        Action(driver).transfer_url()
        Action(driver).sleep()
        TempSpecial(driver).test_click_hotTemp()
        Action(driver).sleep()

    def test_hot_temp_view(self, driver):
        '''在模板专题列表点击模板进入工作台'''
        TempSpecial(driver).test_hot_temp_view(driver)
        Action(driver).sleep()

    def test_hot_temp_coll(self, driver):
        '''在模板专题列表点击收藏模板'''
        TempSpecial(driver).test_hot_temp_coll()
        Action(driver).sleep()

    def test_hot_temp_see(self, driver):
        '''在模板专题列表点击预览模板'''
        TempSpecial(driver).test_hot_temp_see()
        Action(driver).sleep()
