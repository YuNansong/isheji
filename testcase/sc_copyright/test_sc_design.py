"""
Author  : Milo
Time    : 2022/8/02 16:36
Desc    : 设计模块执行用例
"""
import time
from pages.sc_copyright.sc_design import ScDesign

# 团队身份
class TestDesign:

    def test_into_design(self,driver):
        '''测试团队身份进入设计列表'''
        ScDesign(driver).test_into_design()
        time.sleep(1)

    def test_download_design_yangtu(self,driver):
        '''测试团队身份在设计列表，点击下载样图'''
        ScDesign(driver).download_design_yangtu()
        time.sleep(3)

    def test_design_coll(self,driver):
        '''测试团队身份进入设计列表，收藏设计'''
        ScDesign(driver).test_design_coll(driver)
        time.sleep(1)

    def test_open_design_detail(self,driver):
        '''测试团队身份进入设计列表，打开设计详情'''
        ScDesign(driver).test_open_design_detail()
        time.sleep(1)

    def test_design_detail_download_yangtu(self,driver):
        '''测试团队身份在设计详情点击下载样图'''
        ScDesign(driver).test_design_detail_download_yangtu()
        time.sleep(1)

    def test_design_download_source_file(self,driver):
        '''测试团队身份在设计详情，下载源文件'''
        ScDesign(driver).test_design_detail_download_source_file(driver)
        time.sleep(1)

    def test_design_detail_coll(self,driver):
        '''测试团队身份在设计详情，收藏设计'''
        ScDesign(driver).test_design_detail_coll(driver)
        time.sleep(1)

    def test_design_click_keyword(self,driver):
        '''测试团队身份在设计详情，点击推荐关键词'''
        ScDesign(driver).test_design_click_keyword()
        time.sleep(1)
