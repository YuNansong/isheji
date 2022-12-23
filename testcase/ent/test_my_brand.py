from pages.basePage import Action
from pages.entPage.myBrand import My_Brand

# ============================
#    我的企业品牌管理
# ============================
class TestMyEnterprise:

    def test_act_brand(self, driver):
        '''验证企业-进入品牌管理功能'''
        My_Brand(driver).test_act_brand()
        Action(driver).sleep()

    def test_brand_upload_logo(self, driver):
        '''验证企业-品牌管理-上传LOGO功能'''
        My_Brand(driver).test_brand_upload_logo()
        Action(driver).sleep()

    def test_brand_delete_logo(self, driver):
        '''验证企业-品牌管理-删除LOGO功能'''
        My_Brand(driver).test_brand_delete_logo()
        Action(driver).sleep()
    def test_brand_rename_logo(self, driver):
        '''验证企业-品牌管理-重命名logo功能'''
        My_Brand(driver).test_brand_rename_logo()
        Action(driver).sleep()
    def test_brand_download_logo(self,driver):
        '''验证企业-品牌管理-下载logo功能'''
        My_Brand(driver).test_brand_download_logo()
        Action(driver).sleep()

    def test_brand_add_coloer(self, driver):
        '''验证企业-品牌管理-增加颜色功能'''
        My_Brand(driver).test_brand_add_coloer()
        Action(driver).sleep()

    def test_get_color_name(self, driver):
        '''验证企业-品牌管理-获取颜色名称功能'''
        My_Brand(driver).test_get_color_name()
        Action(driver).sleep()

    def test_delete_coloer(self, driver):
        '''验证企业-品牌管理-删除品牌颜色功能'''
        My_Brand(driver).test_delete_coloer()
        Action(driver).sleep()

    def test_add_font(self, driver):
        '''验证企业-品牌管理-增加字体功能'''
        My_Brand(driver).test_add_font()
        Action(driver).sleep()

    def test_add_typeface_repeat(self, driver):
        '''验证企业-品牌管理-增加重复字体功能'''
        My_Brand(driver).test_add_typeface_repeat()
        Action(driver).sleep()
    def test_modiy_font(self, driver):
        '''验证企业-品牌管理-修改字体功能'''
        My_Brand(driver).test_modiy_font()
        Action(driver).sleep()

    def test_delete_font(self, driver):
        '''验证企业-品牌管理-删除字体功能'''
        My_Brand(driver).test_delete_font()
        Action(driver).sleep()
