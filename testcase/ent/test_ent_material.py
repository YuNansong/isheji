from pages.entPage.ent_material import EnterpirseMaterial
from pages.basePage import Action
class TestEntMaterial:

    def test_ent_marterial(self, driver):
        '''验证进入企业--企业素材功能'''
        EnterpirseMaterial(driver).test_ent_marterial()
        Action(driver).sleep()

    def test_add_folder(self, driver):
        '''验证企业素材--新建文件夹功能'''
        EnterpirseMaterial(driver).test_add_folder(driver)
        Action(driver).sleep()

    def test_rename_folder(self, driver):
        '''验证企业素材--重命名文件夹功能'''
        EnterpirseMaterial(driver).test_rename_folder(driver)
        Action(driver).sleep()

    def test_delete_folder(self, driver):
        '''验证企业素材--删除文件夹功能'''
        EnterpirseMaterial(driver).test_delete_folder(driver)
        Action(driver).sleep()

    def test_upload_sucai(self, driver):
        '''验证企业素材--上传素材功能'''
        EnterpirseMaterial(driver).test_upload_sucai()
        Action(driver).sleep()

    def test_rename_pic(self, driver):
        '''验证企业素材--重命名图片功能'''
        EnterpirseMaterial(driver).test_rename_pic()
        Action(driver).sleep()

    def test_move_pic(self, driver):
        '''验证企业素材--移动图片功能'''
        EnterpirseMaterial(driver).test_move_pic(driver)
        Action(driver).sleep()

    def test_delete_pic(self, driver):
        '''验证企业素材--删除图片功能'''
        EnterpirseMaterial(driver).test_delete_pic(driver)
        Action(driver).sleep()