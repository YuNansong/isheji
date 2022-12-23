from pages.sc_copyright.sc_personalcenter import PersonalCenter
from pages.basePage import Action

class TestPersonConter:

    # ==================团队==========================
    def test_change_identity(self, driver):
        '''验证切换团队身份'''
        PersonalCenter(driver).test_change_team()
        Action(driver).sleep()

    def test_batch_authorization(self,driver):
        '''在下载记录页面验证批量授权功能'''
        PersonalCenter(driver).batch_authorization()
        Action(driver).sleep()

    def test_into_enterprise_material(self, driver):
        '''验证进入企业素材删除文件夹'''
        PersonalCenter(driver).del_ent_material_folder()
        Action(driver).sleep()

    def test_member_management(self, driver):
        '''验证成员管理操作功能'''
        PersonalCenter(driver).member_management()
        Action(driver).sleep()