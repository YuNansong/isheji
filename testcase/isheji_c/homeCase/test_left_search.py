from pages.basePage import Action
from pages.isheji_c.homePage.leftTopSearch import LeftSearch


# ======================================================
# 爱设计版权素材库首页
# https://www.isheji.com
# ======================================================

class TestLeftSearch:
    '''普通人'''

    def test_get_url(self, driver):
        '''验证进入首页'''
        Action(driver).transfer_url()

    def test_get_search_tips(self, driver):
        '''验证首页左上角搜索中的提示是否正确'''
        LeftSearch(driver).test_get_search_tips()

    # 左上角搜索模版
    def test_left_search(self, driver):
        '''验证首页左上角搜索功能'''
        key = "七夕"
        LeftSearch(driver).left_search(key)  # 左上角搜索

    # 搜索结果页面，进入模板详情
    def test_clickTempOfSearchResultView(self, driver):
        '''验证在搜索模板结果页点击模板进入工作台'''
        LeftSearch(driver).clickTempOfSearchResultView(driver)
        Action(driver).sleep()
