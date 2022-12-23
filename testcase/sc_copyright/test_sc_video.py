"""
Author  : Milo
Time    : 2022/8/02 16:36
Desc    : 视频模块执行用例
"""
import time
from pages.sc_copyright.sc_video import ScVideo

# 团队身份
class TestVideo:

    def test_into_video(self,driver):
        '''测试团队身份进入视频列表'''
        ScVideo(driver).test_into_video()
        time.sleep(1)

    def test_video_coll(self,driver):
        '''测试团队身份进入视频列表，收藏视频'''
        ScVideo(driver).test_video_coll(driver)
        time.sleep(1)

    def test_open_video_detail(self,driver):
        '''测试团队身份进入视频列表，打开视频详情'''
        ScVideo(driver).test_open_video_detail()
        time.sleep(1)

    def test_video_download_source_file(self,driver):
        '''测试团队身份在视频详情，下载源文件'''
        ScVideo(driver).test_video_detail_download_source_file(driver)
        time.sleep(1)

    def test_video_detail_coll(self,driver):
        '''测试团队身份在视频详情，收藏视频'''
        ScVideo(driver).test_video_detail_coll(driver)
        time.sleep(1)

    def test_video_click_keyword(self,driver):
        '''测试团队身份在视频详情，点击推荐关键词'''
        ScVideo(driver).test_video_click_keyword()
        time.sleep(2)
