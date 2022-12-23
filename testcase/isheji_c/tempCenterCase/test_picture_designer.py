import time
from common.readLog import Log
from pages.basePage import Action
from pages.isheji_c.tempCenterPage.picture_designer import PictureDesigner


class TestPictyreDesigner:
    log = Log(__name__)
    logger = log.getLog()

    def test_picture_designer(self, driver):
        '''验证设计师进入图片创作'''
        self.logger.info("进入到首页，开始测试我的创作")
        Action(driver).transfer_url()
        Action(driver).sleep()
        PictureDesigner(driver).picture_designer()
        Action(driver).sleep()

    def test_new_design(self, driver):
        '''验证新建设计，进入工作台'''
        PictureDesigner(driver).new_design()
        time.sleep(1)

    # def test_submit_to_rxamine(self, driver):
    #     '''验证提交审核写资料功能'''
    #     PictureDesigner(driver).submit_to_rxamine()
    #     time.sleep(1)
    #
    # def test_back_my_design(self, driver):
    #     '''验证返回我的图片创作'''
    #     PictureDesigner(driver).back_my_design()
    #     time.sleep(1)
    #
    # def test_make_drafts(self, driver):
    #     '''验证制造草稿功能'''
    #     PictureDesigner(driver).make_drafts()
    #     time.sleep(1)
    #
    # def test_cuntiue_design(self, driver):
    #     '''验证继续设计功能'''
    #     PictureDesigner(driver).cuntiue_design()
    #     time.sleep(1)
    #
    # def test_submit_for_review(self, driver):
    #     '''验证提交审核功能'''
    #     PictureDesigner(driver).submit_for_review()
    #     time.sleep(1)

    # def test_delete_design(self, driver):
    #     '''验证删除设计功能'''
    #     PictureDesigner(driver).delete_design()
    #     time.sleep(1)
