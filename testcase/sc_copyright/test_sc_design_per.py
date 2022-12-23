import time
from pages.sc_copyright.sc_design import ScDesign

class TestDesignPer:
    def test_design_download_yangtu_none(self,driver):
        '''测试个人身份在设计详情页下载样图'''
        ScDesign(driver).test_design_detail_download_yangtu_none()
        time.sleep(1)

    def test_design_download_source_file_none(self,driver):
        '''测试个人身份在设计详情页点击下载源文件'''
        ScDesign(driver).test_design_detail_download_source_file_none()
        time.sleep(1)

    def test_design_detail_buy_vip(self,driver):
        '''测试个人身份在设计详情页点击购买单张套餐'''
        ScDesign(driver).test_design_detail_buy_vip()
        time.sleep(1)