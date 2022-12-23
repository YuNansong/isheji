"""
Author  : Milo
Time    : 2022/3/7 11:41
Desc    : 版权站测试图片--个人身份
account : 135
"""
import time
from pages.sc_copyright.sc_picture import SCPicture

class TestPicPer:

    def test_picList_down_yangtu(self,driver):
        '''版权站-个人在图片列表下载样图-无下载额度提示'''
        SCPicture(driver).picList_down_yangtu()
        time.sleep(2)

    def test_personal_detail_down_yangtu(self,driver):
        '''版权站-个人在图片详情页-下载样图无额度提示'''
        SCPicture(driver).personal_detail_down_yangtu()
        time.sleep(2)