from pages.basePage import Action
from pages.entPage.ent_newDesign import NewDesign

class TestNewDesign:

    def test_act_newDesign(self, driver):
        '''验证企业-进入新建设计页面功能'''
        NewDesign(driver).act_new_design()
        Action(driver).sleep()

    def test_create_custome_temp(self, driver):
        '''验证企业-点击新建自定义尺寸功能'''
        NewDesign(driver).test_create_custome_temp()
        Action(driver).sleep()

    def test_click_temp(self, driver):
        '''验证企业-点击各种类别的模板功能'''
        NewDesign(driver).test_click_temp()
        Action(driver).sleep()