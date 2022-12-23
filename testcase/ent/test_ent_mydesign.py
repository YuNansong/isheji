from pages.entPage.ent_myDesign import MyDesign
from pages.basePage import Action
import time

# ============================
#    企业--我的设计页面用例
# ============================
class TestMyDesign:

    def test_my_design(self, driver):
        '''验证从首页进入我的设计页面'''
        MyDesign(driver).test_act_my_design()
        time.sleep(2)

    def test_add_folder(self,driver):
        '''验证我的设计--新增文件夹功能'''
        MyDesign(driver).test_add_folder(driver)
        time.sleep(2)

    def test_open_folder(self, driver):
        '''验证我的设计--打开文件夹功能'''
        MyDesign(driver).test_open_folder()
        time.sleep(2)

    def test_rename_folder(self, driver):
        '''验证我的设计--重命名文件夹功能'''
        MyDesign(driver).test_rename_folder(driver)
        Action(driver).sleep()

    def test_delete_folder(self, driver):
        '''验证我的设计--删除文件夹功能'''
        MyDesign(driver).test_delete_folder(driver)
        Action(driver).sleep()

    def test_mydesign_renmae(self, driver):
        '''验证我的设计--重命名图片模板功能'''
        MyDesign(driver).test_rename_pictemp(driver)
        time.sleep(2)

    def test_mydesign_move(self, driver):
        '''验证我的设计--移动图片模板功能'''
        MyDesign(driver).test_mydesign_move(driver)
        time.sleep(2)

    def test_picture_template(self, driver):
        '''验证我的设计--进入模板页面功能'''
        MyDesign(driver).test_picture_template(driver)
        time.sleep(2)

    def test_upload_temp(self,driver):
        '''验证我的设计--上传模板功能'''
        MyDesign(driver).test_upload_temp(driver)
        time.sleep(2)

    def test_delete_pictemp(self, driver):
        '''验证我的设计--删除图片模板功能'''
        MyDesign(driver).test_delete_pictemp(driver)
        time.sleep(2)
