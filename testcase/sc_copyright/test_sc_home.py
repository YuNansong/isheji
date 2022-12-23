"""
Author  : Milo
Time    : 2022/3/2 11:41
Desc    : 版权站首页的测试用例
"""
import time
from pages.sc_copyright.sc_homePage import SCHomePage


class TestHome:

    def test_hot_tuijian(self, driver):
        '''版权站-首页点击热门推荐图片'''
        SCHomePage(driver).test_hot_tuijian()
        time.sleep(2)

    def test_video_material(self, driver):
        '''版权站-首页点击视频素材'''
        SCHomePage(driver).test_video_material()
        time.sleep(2)

    def test_pic_material(self, driver):
        '''版权站-首页点击图片素材'''
        SCHomePage(driver).test_pic_material()
        time.sleep(2)

    def test_temp_material(self, driver):
        '''版权站-首页点击平面模板'''
        SCHomePage(driver).test_temp_material()
        time.sleep(2)

    def test_hot_pic(self, driver):
        '''版权站-首页专题推荐点击分类'''
        SCHomePage(driver).test_hot_pic()
        time.sleep(2)

    def test_click_specialmore(self, driver):
        '''版权站-首页点击专题推荐查看更多'''
        SCHomePage(driver).test_click_specialmore()
        time.sleep(2)

    def test_coll_pic(self, driver):
        '''版权站-首页图片素材列表点击收藏图片'''
        SCHomePage(driver).test_coll_pic(driver)
        time.sleep(2)

    def test_coll_video(self, driver):
        '''版权站-首页视频素材列表点击收藏视频'''
        SCHomePage(driver).test_coll_video(driver)
        time.sleep(2)

    def test_coll_design(self, driver):
        '''版权站-首页设计素材列表点击收藏设计模板'''
        SCHomePage(driver).test_coll_design(driver)
        time.sleep(2)

    def test_similar_pic(self, driver):
        '''版权站-首页点击专题推荐查看相似图片'''
        SCHomePage(driver).test_similar_pic()
        time.sleep(2)

    def test_click_personal_vip(self, driver):
        '''版权站-首页点击个人VIP'''
        SCHomePage(driver).click_personal_vip()
        time.sleep(2)

    def test_click_ent_vip(self, driver):
        '''版权站-首页点击企业VIP'''
        SCHomePage(driver).click_ent_vip()
        time.sleep(2)

    def test_click_coll_folder(self, driver):
        '''版权站-首页点击收藏夹菜单'''
        SCHomePage(driver).test_click_coll_folder()
        time.sleep(2)

    def test_search(self, driver):
        '''版权站-首页搜索图片'''
        SCHomePage(driver).test_search("美食")
        time.sleep(2)
