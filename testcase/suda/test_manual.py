from pages.basePage import Action
from pages.suda.manual import Manual


class TestManual():

    def test_into_suda(self, driver):
        '''验证进入苏打项目和确切功能'''
        Manual(driver).into_suda()
        Action(driver).sleep()

    def test_change_token(self, driver):
        '''更新后需要手动更换token，自动获取后点击初始化'''
        Manual(driver).change_token()
        Action(driver).sleep()

    def test_modo_list(self, driver):
        '''验证模版搜索和点击功能'''
        Manual(driver).modo_list()
        Action(driver).sleep()
        Manual(driver).click_one_modo()

    def test_phono_picture(self, driver):
        '''验证图片搜索和点击功能'''
        Manual(driver).phono_picture()


    def test_source_material(self, driver):
        '''验证在工作台点击左侧素材功能'''
        Manual(driver).source_material()
        Action(driver).sleep()
        Manual(driver).material_other()

    def test_words(self, driver):
        '''验证在工作台点击左侧文字按钮，并添加文字功能'''
        Manual(driver).words_written()
        Action(driver).sleep()
    #
    def test_background(self, driver):
        '''验证在工作台点击左侧背景功能'''
        Manual(driver).background()
        Action(driver).sleep()


    # def test_realy_input(self, driver):
    #     '''验证上传模块功能'''
    #     Manual(driver).realy_input()
    #     Action(driver).sleep()


    def test_save_temp(self, driver):
        '''验证在工作台点击保存按钮功能'''
        Manual(driver).save_temp()
        Manual(driver).sleep()