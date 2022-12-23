from pages.isheji_c.tempCenterPage.templateCenter import PictureTemplate
from pages.basePage import Action


class TestTempCenter:
    # ============================
    #    模板中心用例  VIP用户执行
    # ============================

    def test_template_pic(self, driver):
        '''验证在首页点击模板中心菜单'''
        Action(driver).transfer_url()
        Action(driver).sleep()
        PictureTemplate(driver).test_click_tempCenterMenu()
        Action(driver).sleep()

    def test_switch_classification(self, driver):
        '''验证在模板中心按分类筛选功能'''
        PictureTemplate(driver).switch_classification()
        Action(driver).sleep()

    def test_switch_scene(self, driver):
        '''验证在模板中心按场景筛选功能'''
        PictureTemplate(driver).switch_scene()
        Action(driver).sleep()

    def test_switch_purpose(self, driver):
        '''验证在模板中心按用途筛选功能'''
        PictureTemplate(driver).switch_purpose()
        Action(driver).sleep()

    def test_switch_style(self, driver):
        '''验证在模板中心按风格筛选功能'''
        PictureTemplate(driver).switch_style()
        Action(driver).sleep()

    def test_template_center_picture(self, driver):#######收藏功能暂时有问题
        '''验证在模板中心收藏模版功能'''
        PictureTemplate(driver).template_center_picture()
        Action(driver).sleep()

    # ============================
    #    新媒体配图用例
    # ============================

    def test_new_media_graphics(self, driver):
        '''验证在首页左侧导航点击新媒体配图'''
        PictureTemplate(driver).new_media_graphics()
        Action(driver).sleep()

    def test_new_media_scenne(self, driver):
        '''验证在首页左侧导航点击新媒体配图后，切换到场景查询功能'''
        PictureTemplate(driver).new_media_scenne()
        Action(driver).sleep()

    def test_new_media_purpose(self, driver):
        '''验证在首页左侧导航点击新媒体配图后，切换到用途筛选功能'''
        PictureTemplate(driver).new_media_purpose()
        Action(driver).sleep()

    # ============================
    #    营销海报用例
    # ============================

    def test_marketing_poster(self, driver):
        '''验证在首页左侧导航点击营销海报菜单'''
        PictureTemplate(driver).marketing_poster()
        Action(driver).sleep()

    def test_marketing_poster_use(self, driver):
        '''验证在首页左侧导航点击营销海报后按用途筛选'''
        PictureTemplate(driver).new_media_scenne()
        Action(driver).sleep()

    def test_marketing_poster_long(self, driver):
        '''验证在首页左侧导航点击营销海报后按营销长图筛选'''
        PictureTemplate(driver).marketing_poster_long()
        Action(driver).sleep()

    def test_social_life(self, driver):
        '''验证在首页左侧导航点击社交生活菜单'''
        PictureTemplate(driver).social_life()
        Action(driver).sleep()

    def test_social_life_scene(self, driver):
        '''验证社交生活：手机壁纸功能'''
        PictureTemplate(driver).new_media_scenne()
        Action(driver).sleep()

    def test_social_life_use(self, driver):
        '''验证社交生活：互联网功能'''
        PictureTemplate(driver).new_media_purpose()
        Action(driver).sleep()
        PictureTemplate(driver).home_button()

    # ============================
    #    视频模板用例
    # ============================

    ''' 视频模板测试用例(已下架功能） '''

    # def test_click_videoTempMenu(self, driver):
    #     '''验证点击左侧导航视频模板菜单跳转页面是否正确'''
    #     PictureTemplate(driver).test_click_videoTemp()  # 模版中心-视频模版
    #     Action(driver).sleep()
    #
    # def test_template_video_user(self, driver):
    #     '''验证视频模版的用途'''
    #     PictureTemplate(driver).video_use()
    #     Action(driver).sleep()
    #
    # def test_template_video_styal(self, driver):
    #     '''验证视频模版的风格筛选'''
    #     PictureTemplate(driver).video_styal()
    #     Action(driver).sleep()
    #
    # def test_template_video_vlog(self, driver):
    #     '''验证收藏视频模版功能'''
    #     PictureTemplate(driver).video_vlog()
    #     Action(driver).sleep()
