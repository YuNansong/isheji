from pages.entPage.ent_myColl import EntMyColl
from pages.basePage import Action

# ============================
#    企业--我的设计页面用例
# ============================
class TestMyColl:

    def test_act_myColl(self, driver):
        '''验证企业-进入我的收藏页面'''
        EntMyColl(driver).test_act_myColl()
        Action(driver).sleep(2)

    def test_click_temp(self, driver):
        '''验证我的收藏--进入模板页面功能'''
        EntMyColl(driver).test_click_temp(driver)
        Action(driver).sleep()

    def test_click_cancle_coll(self,driver):
        '''验证我的收藏--取消收藏模板功能'''
        EntMyColl(driver).test_click_cancle_coll(driver)
        Action(driver).sleep()
