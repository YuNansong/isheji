from pages.entPage.ent_temp import EnterpirseTemp
from pages.basePage import Action

class TestEnterpirseTemp:

    def test_design(self, driver):
        '''验证进入企业模版功能'''
        EnterpirseTemp(driver).test_act_ent_temp()
        Action(driver).sleep()

    def test_right_temp_menu(self,driver):
        '''验证点击右侧导航--企业模板'''
        EnterpirseTemp(driver).test_right_menu_temp()
        Action(driver).sleep()

    def test_add_folder(self, driver):
        '''验证新建文件夹功能'''
        EnterpirseTemp(driver).test_add_folder(driver)
        Action(driver).sleep()

    def test_rename_folder(self, driver):
        '''验证企业模板--重命名文件夹功能'''
        EnterpirseTemp(driver).test_rename_folder(driver)
        Action(driver).sleep()

    def test_delete_folder(self, driver):
        '''验证企业模板--删除文件夹功能'''
        EnterpirseTemp(driver).test_delete_folder(driver)
        Action(driver).sleep()

    def test_upload_modo(self, driver):
        '''验证企业模板--上传模版功能'''
        EnterpirseTemp(driver).test_upload_modo(driver)
        Action(driver).sleep()

    def test_set_team_modo(self, driver):
        '''验证设置团队模版功能'''
        EnterpirseTemp(driver).set_team_modo(driver)
        Action(driver).sleep()

    def test_rename_pictemp(self, driver):
        '''验证企业模板--重命名模板功能'''
        EnterpirseTemp(driver).test_rename_pictemp(driver)
        Action(driver).sleep()

    def test_move_pictemp(self, driver):
        '''验证企业模板--移动模板功能'''
        EnterpirseTemp(driver).test_move_pictemp(driver)
        Action(driver).sleep()

    def test_click_coll_pic_temp(self, driver):
        '''验证企业模板--收藏模板功能'''
        EnterpirseTemp(driver).test_click_coll_pictemp(driver)
        Action(driver).sleep()

    def test_click_delete_pic_temp(self, driver):
        '''验证企业模板--删除模板功能'''
        EnterpirseTemp(driver).test_delete_pictemp(driver)
        Action(driver).sleep()
