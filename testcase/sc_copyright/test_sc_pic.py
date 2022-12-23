"""
Author  : zhouqixi
Time    : 2022/3/3 11:41
Desc:对搜索结果的自动化操作
"""
from pages.sc_copyright.sc_picture import SCPicture

# 团队身份
class TestPicSearch:

    def test_search_text(self, driver):
        '''首页输入关键字查询图片，并可以滚动显示图片'''
        SCPicture(driver).SearchPage()
        SCPicture(driver).rollPage()

    def test_search_newKeywords(self, driver):
        '''图片搜索结果页输入新的关键字查询图片'''
        SCPicture(driver).SearchByText()
        SCPicture(driver).rollPage()

    def test_search_select(self, driver):
        '''图片搜索结果页下进行筛选操作'''
        SCPicture(driver).selectSearch()

    def test_operate_collect(self, driver):
        '''图片搜索结果页下进行收藏操作，操作收藏和取消收藏'''
        SCPicture(driver).collectPic()

    def test_picList_down_yangtu(self, driver):
        '''团队图片搜索结果页下进行样图下载操作'''
        SCPicture(driver).picList_down_yangtu()

    def test_enter_detail(self, driver):
        '''图片搜索结果页下进入详情页'''
        SCPicture(driver).picDetail()

    def test_picDetail_down_yangtu(self, driver):
        '''团队在图片详情页，点击下载样图按钮'''
        SCPicture(driver).team_pic_detail_down_yangtu()

    def test_pic_detail_down_yuantu(self, driver):
        '''团队在图片详情页，点击下载原图按钮'''
        SCPicture(driver).team_pic_detail_down_yuantu(driver)

    def test_key_word_into(self, driver):
        '''团队在图片详情页，点击推荐关键词'''
        SCPicture(driver).key_word_into()