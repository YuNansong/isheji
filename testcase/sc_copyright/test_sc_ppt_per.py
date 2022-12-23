import time
from pages.sc_copyright.sc_ppt import ScPPT

class TestPPTPer:

    def test_ppt_download_source_file_none(self,driver):
        '''测试个人身份在PPT 详情页点击下载源文件'''
        ScPPT(driver).test_ppt_detail_download_source_file_none()
        time.sleep(1)

    def test_ppt_detail_buy_vip(self,driver):
        '''测试个人身份在PPT 详情页点击购买单张套餐'''
        ScPPT(driver).test_ppt_detail_buy_vip()
        time.sleep(1)