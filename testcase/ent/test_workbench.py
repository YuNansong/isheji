from pages.isheji_c.tempCenterPage.workbenchPage import WorkBench
from pages.basePage import Action

class TestWorkbenchLeftButton():

    def test_selected(self, driver):
        '''验证在首页点击模版进入工作台功能'''
        WorkBench(driver).test_qiye_info_workbench()
        Action(driver).sleep()

    def test_template_info(self, driver):
        '''验证在工作台左侧模板--我的收藏列表功能'''
        WorkBench(driver).template_my_collection()
        Action(driver).sleep()

    def test_template_while(self, driver):
        '''验证在工作台推荐列表切换模版功能'''
        WorkBench(driver).test_template_while()
        Action(driver).sleep()

    def test_source_material(self, driver):
        '''验证在工作台点击左侧素材按钮功能'''
        WorkBench(driver).source_material_hot()
        Action(driver).sleep()

    def test_click_hot_material(self,driver):
        '''验证在工作台素材列表点击某个素材功能'''
        WorkBench(driver).test_click_hot_material()
        Action(driver).sleep()

    def test_click_material_class(self,driver):
        '''验证在工作台素材列表点击--查看全部功能'''
        WorkBench(driver).test_click_material_class()
        Action(driver).sleep()

    def test_words_written(self, driver):
        '''验证在工作台点击左侧文字按钮，并添加文字功能'''
        WorkBench(driver).words_written()
        Action(driver).sleep()

    def test_background(self, driver):
        '''验证在工作台点击左侧背景功能'''
        WorkBench(driver).test_click_background()
        Action(driver).sleep()

    def test_click_background_color(self,driver):
        '''验证在工作台左侧背景--背景图功能'''
        WorkBench(driver).test_click_background_color()
        Action(driver).sleep()

    def test_convenient_upload_pic(self, driver):
        '''验证在工作台左侧便捷模块【上传】图片'''
        WorkBench(driver).test_convenient_upload_pic()
        Action(driver).sleep()

    def test_convenient_detele_pic(self, driver):
        '''验证在工作台左侧便捷模块【删除】图片'''
        WorkBench(driver).test_convenient_detele_pic()
        Action(driver).sleep()

    def test_create_qrcode(self, driver):
        '''验证在工作台左侧便捷模块【生成二维码】'''
        WorkBench(driver).test_create_qrcode()
        Action(driver).sleep()

    def test_up_upload_pic(self, driver):
        '''验证在工作台上传模块【上传】图片'''
        WorkBench(driver).test_up_upload_pic()
        Action(driver).sleep()

    def test_delete_pic(self, driver):
        '''验证在工作台上传模块【删除】图片'''
        WorkBench(driver).test_up_delete_pic()
        Action(driver).sleep()

    def test_download_temp(self, driver):
        '''验证在工作台【保存模板并下载】功能'''
        WorkBench(driver).test_download_temp(driver)