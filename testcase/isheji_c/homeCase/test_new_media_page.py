from pages.isheji_c.homePage.new_media_page import NewMediaPage
from pages.basePage import Action


class TestNewMediaPage:

    def test_info_new_media_page(self, driver):
        '''验证进入新媒体落地页功能'''
        NewMediaPage(driver).info_new_media_page()
        Action(driver).sleep()

    def test_make_one_picture(self, driver):
        '''验证开始做图功能'''
        NewMediaPage(driver).make_one_picture()
        Action(driver).sleep()

    def test_info_work_page(self, driver):
        '''验证模版进入工作台功能'''
        NewMediaPage(driver).info_work_page()
        Action(driver).sleep()

    def testmake_two_picture(self, driver):
        '''验证中部开始作图按钮'''
        NewMediaPage(driver).make_two_picture()
        Action(driver).sleep()

    def test_info_scene(self, driver):
        '''验证进入落地页场景'''
        NewMediaPage(driver).info_scene()
        Action(driver).sleep()

    def test_other_make_picture(self, driver):
        '''验证其他开始作图按钮功能'''
        NewMediaPage(driver).other_make_picture()
        Action(driver).sleep()

