import time
from pages.isheji_c.tempCenterPage.templateCenter import PictureTemplate


class TestTempCenter:
    # ============================
    #    模板中心用例  VIP用户执行
    # ============================

    def test_act_temp_center(self, driver):
        '''验证在首页点击模板中心菜单'''
        PictureTemplate(driver).test_act_temp_center()
        time.sleep(2)

    def test_switch_classification(self, driver):
        '''验证在模板中心按分类筛选功能'''
        PictureTemplate(driver).qiye_switch_scene()
        time.sleep(2)

    def test_switch_scene(self, driver):
        '''验证在模板中心按场景筛选功能'''
        PictureTemplate(driver).qiye_switch_purpose()
        time.sleep(2)

    def test_switch_purpose(self, driver):
        '''验证在模板中心按用途筛选功能'''
        PictureTemplate(driver).qiey_switch_style()
        time.sleep(2)

    def test_template_center_picture(self, driver):
        '''验证在模板中心收藏模版功能'''
        PictureTemplate(driver).qiye_template_center_picture()
        time.sleep(2)