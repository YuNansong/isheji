import time
from pages.sc_copyright.sc_music import ScMusic

class TestMusicPer:
    def test_download_music_no_interests(self,driver):
        '''测试个人身份在音乐详情下载音乐'''
        ScMusic(driver).download_music_no_interests(driver)
        time.sleep(1)

    def test_music_detail_buy_vip(self,driver):
        '''测试个人身份在音乐详情点击购买单张套餐'''
        ScMusic(driver).test_music_detail_buy_vip()
        time.sleep(1)