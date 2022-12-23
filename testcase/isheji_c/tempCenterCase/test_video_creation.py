from pages.basePage import Action
from pages.isheji_c.tempCenterPage.video_creation import VideoCreation


class TestVideoCreation:
    '''设计师：我的视频创作'''

    def test_video_into(self, driver):
        '''验证从首页进入我的视频创作列表功能'''
        Action(driver).transfer_url()
        Action(driver).sleep()
        VideoCreation(driver).into_my_video_create()
        Action(driver).sleep(2)

    def test_upload_video_temp(self,driver):
        '''验证进入设计师视频模板--新增视频功能'''
        VideoCreation(driver).test_upload_video_temp()
        Action(driver).sleep(2)

    def test_edit_video_temp(self, driver):
        '''验证在我的视频创作列表编辑模版功能'''
        VideoCreation(driver).test_edit_video_temp()
        Action(driver).sleep()

    def test_all_list(self,driver):
        '''验证进入设计师视频模板--全部列表功能'''
        VideoCreation(driver).all_list()
        Action(driver).sleep(2)

    def test_draft_list(self,driver):
        '''验证进入设计师视频模板--草稿列表功能'''
        VideoCreation(driver).test_draft_list()
        Action(driver).sleep(2)

    def test_approve_list(self,driver):
        '''验证进入设计师视频模板--审核中列表功能'''
        VideoCreation(driver).approve_list()
        Action(driver).sleep(2)

    def test_approve_succ_list(self,driver):
        '''验证进入设计师视频模板--审核通过列表功能'''
        VideoCreation(driver).approve_succ_list()
        Action(driver).sleep(2)

    def test_delete_video_temp(self, driver):
        '''验证在我的视频创作列表删除模版功能'''
        VideoCreation(driver).test_delete_video_temp()
        Action(driver).sleep()