from pages.isheji_c.homePage.myDesign import MyDesign
from pages.basePage import Action

# ============================
#    我的设计页面用例  VIP用户执行
# ============================
class TestMyDesign:

    def test_my_design(self, driver):
        '''验证从首页进入我的设计页面'''
        Action(driver).transfer_url()
        Action(driver).sleep()
        MyDesign(driver).test_clickMyDesign()
        Action(driver).sleep()

    def test_del_more_folder(self, driver):
        """验证删除文件夹和创建新文件夹"""
        MyDesign(driver).del_more_folder()

    def test_Create_copy(self, driver):
        """验证创建副本"""
        MyDesign(driver).get_first_modo_name()

    def test_assert_out_in_name(self,driver):
        """验证将模板移入文件夹"""
        MyDesign(driver).assert_out_in_name()

    # def test_my_design_picture(self, driver):
    #     '''验证我的设计--点击图片模版按钮功能'''
    #     MyDesign(driver).picture_template()
    #     Action(driver).sleep()

    # def test_my_design_video(self, driver):
    #     '''验证我的设计--点击视频模版点击功能'''
    #     MyDesign(driver).video_template()
    #     Action(driver).sleep()

    # def test_my_design_picture_see(self, driver):
    #     '''验证点击模板进入工作台功能'''
    #     MyDesign(driver).picture_template_see()
    #     Action(driver).sleep()
    #
    # def test_delete_my_design(self, driver):
    #     '''验证我的设计删除模版功能'''
    #     MyDesign(driver).test_delete_my_design()
    #     Action(driver).sleep()
    #
    # def test_my_collection(self, driver):
    #     '''验证点击我的收藏菜单跳转页面是否正确'''
    #     MyDesign(driver).test_my_collection()  # 我的收藏
    #     Action(driver).sleep()
    #
    # def test_collection_picture_template(self, driver):
    #     '''验证我的收藏点击图片模版菜单功能'''
    #     MyDesign(driver).collection_picture_template()
    #     Action(driver).sleep()
    #
    # def test_my_cancel_collection(self, driver):
    #     '''验证我的收藏--图片模版取消收藏'''
    #     MyDesign(driver).cancel_collection_action()
    #     Action(driver).sleep()
