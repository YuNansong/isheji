from pages.isheji_c.homePage.poster_home import PosterHome
from pages.basePage import Action


class TestPosterHome:

    def test_info_poster_home_page(self, driver):
        '''验证进入海报家落地页功能'''
        PosterHome(driver).info_poster_home_page()
        Action(driver).sleep()

    # def test_design_button_info(self, driver):
    #     '''验证开始作图进入新建设计'''
    #     PosterHome(driver).design_button_info()
    #     Action(driver).sleep()

    # def test_info_poster(self, driver):#待配置
    #     '''验证进入海报'''
    #     PosterHome(driver).info_poster()
    #     Action(driver).sleep()

    def test_input_boxfind(self, driver):
        PosterHome(driver).input_boxfind()
        Action(driver).sleep()