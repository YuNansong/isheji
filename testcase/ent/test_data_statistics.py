from pages.entPage.data_statistice import DataStatistice
from pages.basePage import Action


class TestDataStatistice:

    def test_act_dataStat(self, driver):
        '''验证进入企业--数据统计'''
        DataStatistice(driver).test_act_dataStat()
        Action(driver).sleep()

    def test_one_more_button(self, driver):
        '''验证版权用量更多、导出、关闭、导出功能'''
        DataStatistice(driver).copyright_pictures_usage()
        Action(driver).sleep()

    def test_use_export_button(self, driver):
        '''验证版权用量导出功能'''
        DataStatistice(driver).use_export_button()
        Action(driver).sleep()

    def test_top_more_button(self, driver):
        '''验证导出更多功能'''
        DataStatistice(driver).top_more_button()
        Action(driver).sleep()
        Action(driver).close_and_home_page()
