import time
from pages.sc_copyright.sc_video import ScVideo

class TestVideoPer:
    def test_download_video_no_interests(self,driver):
        '''测试个人身份在视频详情下载视频'''
        ScVideo(driver).test_video_detail_download_source_file_none()
        time.sleep(1)

    def test_video_detail_buy_vip(self,driver):
        '''测试个人身份在视频详情点击购买单张套餐'''
        ScVideo(driver).test_video_detail_buy_vip()
        time.sleep(1)