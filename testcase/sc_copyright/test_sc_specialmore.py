"""
Author  : Milo
Time    : 2022/3/7 11:41
Desc    : 版权站专题页的测试用例
"""
from pages.sc_copyright.sc_specialmore import SpecialPage
import time


class TestHome:

    def test_act_special(self, driver):
        '''版权站-首页点击某个专题'''
        SpecialPage(driver).test_act_special(driver)
        time.sleep(2)

    def test_special_coll(self, driver):
        '''版权站-专题页收藏图片'''
        SpecialPage(driver).test_special_coll(driver)
        time.sleep(2)

    # def test_special_download(self,driver):
    #     '''版权站-专题页无下载额度图片'''
    #     SpecialPage(driver).test_special_download(driver)
    #     time.sleep(2)

    def test_special_search_smiler(self, driver):
        '''版权站-专题页查看相似图片'''
        SpecialPage(driver).test_special_search_smiler(driver)
