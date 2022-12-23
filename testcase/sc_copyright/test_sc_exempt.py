"""
Author  : Milo
Time    : 2022/8/02 16:36
Desc    : 免抠元素模块执行用例
"""
import time
from pages.sc_copyright.sc_exempt import ScExempt

# 团队身份
class TestExempt:

    def test_into_exempt(self,driver):
        '''测试团队身份进入免抠元素列表'''
        ScExempt(driver).test_into_exempt()
        time.sleep(1)

    def test_exempt_coll(self,driver):
        '''测试团队身份进入免抠元素列表，收藏免抠元素'''
        ScExempt(driver).test_exempt_coll(driver)
        time.sleep(1)

    def test_open_exempt_detail(self,driver):
        '''测试团队身份进入免抠元素列表，打开免抠元素详情'''
        ScExempt(driver).test_open_exempt_detail()
        time.sleep(1)

    def test_exempt_download_source_file(self,driver):
        '''测试团队身份在免抠元素详情，下载源文件'''
        ScExempt(driver).test_exempt_detail_download_source_file(driver)
        time.sleep(1)

    def test_exempt_detail_coll(self,driver):
        '''测试团队身份在免抠元素详情，收藏免抠元素'''
        ScExempt(driver).test_exempt_detail_coll(driver)
        time.sleep(1)

    def test_exempt_click_keyword(self,driver):
        '''测试团队身份在免抠元素详情，点击推荐关键词'''
        ScExempt(driver).test_exempt_click_keyword()
        time.sleep(1)
