from pages.suda.suda_requests import SudaApi


class TestSudaApi():

    def test_picture_find(self):
        '''验证图片搜索接口'''
        SudaApi().picture_find()

    def test_Visual_pictures_800px_resources(self):
        '''验证视觉图片800px资源接口'''
        SudaApi().Visual_pictures_800px_resources()

    def test_get_system_template_information(self):
        '''验证获取系统模板信息接口'''
        SudaApi().get_system_template_information()

    def test_get_user_design_information(self):
        '''验证获取用户设计信息（现有设计进入）接口'''
        SudaApi().get_user_design_information()

    def test_save_design_for_team_users(self):
        '''验证团队用户保存设计接口'''
        SudaApi().save_design_for_team_users()

    def test_team_user_download_design(self):
        '''验证团队用户下载设计接口'''
        SudaApi().team_user_download_design()

    def test_detect_image_generation(self):
        '''验证检测图片生成（下载轮循）接口'''
        SudaApi().detect_image_generation()
