"""
Author  : Milo
Time    : 2022/8/11 16:36
Desc    : PPT模块执行用例
"""
import time
from pages.sc_copyright.sc_ppt import ScPPT

# 团队身份
class TestPPT:

    def test_into_ppt(self,driver):
        '''测试团队身份进入PPT列表'''
        ScPPT(driver).test_into_ppt()
        time.sleep(1)

    def test_ppt_coll(self,driver):
        '''测试团队身份进入PPT列表，收藏PPT'''
        ScPPT(driver).test_ppt_coll(driver)
        time.sleep(1)

    def test_open_ppt_detail(self,driver):
        '''测试团队身份进入PPT列表，打开PPT详情'''
        ScPPT(driver).test_open_ppt_detail()
        time.sleep(1)

    def test_ppt_download_source_file(self,driver):
        '''测试团队身份在PPT详情，下载源文件'''
        ScPPT(driver).test_ppt_detail_download_source_file(driver)
        time.sleep(1)

    def test_ppt_detail_coll(self,driver):
        '''测试团队身份在PPT详情，收藏PPT'''
        ScPPT(driver).test_ppt_detail_coll(driver)
        time.sleep(1)

    def test_ppt_click_keyword(self,driver):
        '''测试团队身份在PPT详情，点击推荐关键词'''
        ScPPT(driver).test_ppt_click_keyword()
        time.sleep(1)
