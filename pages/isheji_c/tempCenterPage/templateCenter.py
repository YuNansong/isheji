from common.sendDingTalk import SendDingTalk
from common.readLog import Log
from model.entModel.entIndexModel import EntIndexModel


class PictureTemplate(EntIndexModel):
    log = Log(__name__)
    logger = log.getLog()

    # 进入到模板中心
    def picture(self):
        '''模版中心-图片模版。'''
        pctr = ('xpath', "//li[@class='block-item template-tp']//span[@class='block-text']")
        self.click(pctr)

    # 获取模板中心第一个分类
    def new_picture(self):
        new_picture = ('xpath', "//div[@class='search-item-content classifys']//span[2]//a[1]")
        text = self.getText(new_picture)
        return text

    # 企业端进入模板中心
    def test_act_temp_center(self):
        self.click_manage()
        self.sleep(1)
        self.click_temp_center()

    def test_click_tempCenterMenu(self):
        try:
            # self.home_button()
            self.sleep()
            self.picture()
            self.sleep()
            text = self.new_picture()
            assert text == "新媒体配图"
        except Exception as e:
            self.logger.error('失败:进入模版中心-断言：新媒体配图%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:进入模版中心-断言：新媒体配图")
            raise e

    def switch_classification(self):
        '''分类：新媒体配图、营销海报、社交生活、视频模版'''
        try:
            class_one = ('xpath', "//div[@class='search-item-content classifys']//span[2]")  # 新媒体配图
            class_two = ('xpath', "//div[@class='search-item-content classifys']//span[3]")  # 营销海报
            class_three = ('xpath', "//div[@class='search-item-content classifys']//span[4]")  # 社交生活
            class_four = ('xpath', "//div[@class='search-item-content classifys']//span[5]")  # 电商设计
            self.click(class_two)
            self.sleep()
            self.click(class_three)
            self.sleep()
            self.click(class_four)
            self.sleep()
            self.click(class_one)
            self.sleep()
        except Exception as e:
            self.logger.error('失败:分类：新媒体配图、营销海报、社交生活、视频模版%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:分类：新媒体配图、营销海报、社交生活、视频模版")
            raise e

    def switch_scene(self):
        '''进入到场景分类'''
        try:
            scene = ('xpath', "//span[@typeid='5']")  # 公众号首图
            self.click(scene)
            self.sleep()
        except Exception as e:
            self.logger.error('失败:模版中心进入到场景分类%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:模版中心进入到场景分类")
            raise e

    def qiye_switch_scene(self):
        '''进入到场景分类'''
        try:
            scene = ('xpath', "//span[contains(text(),'场景')]/parent::div/div/span[2]")  # 公众号首图
            self.click(scene)
            self.sleep()
        except Exception as e:
            self.logger.error('失败:模版中心进入到场景分类%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:模版中心进入到场景分类")
            raise e

    def switch_purpose(self):
        '''进入到用途分类'''
        try:
            yongt = ('xpath', "//span[@typeid='45']")  # 热点节日
            self.click(yongt)
            self.sleep()
        except Exception as e:
            self.logger.error('失败:模版中心进入到用途分类%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:模版中心进入到用途分类")
            raise e

    def qiye_switch_purpose(self):
        '''进入到企业端用途分类'''
        try:
            yongt = ('xpath', "//span[contains(text(),'用途')]/parent::div/div/span[2]")  # 热点节日
            self.click(yongt)
            self.sleep()
        except Exception as e:
            self.logger.error('失败:模版中心进入到用途分类%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:模版中心进入到用途分类")
            raise e

    def switch_style(self):
        '''进入到综合排序，点击风格-->扁平简约分类'''
        fengg = ('xpath', "//i[@class='iconfont icon-moreandmore-copy']")  # 风格筛选
        self.click(fengg)
        self.sleep()
        first_styal = ('xpath', "//li[2]//span[1]//a[1]")  # 扁平简约
        self.click(first_styal)
        self.sleep()

    def qiey_switch_style(self):
        '''进入到综合排序'''
        fengg = ('xpath', "//div[contains(text(),'综合排序')]/parent::div/div[2]")  # 最新上传
        self.click(fengg)
        self.sleep()
        first_styal = ('xpath', "//div[contains(text(),'综合排序')]/parent::div/div[3]")  # 最多使用
        self.click(first_styal)
        self.sleep()

    def template_center_picture(self):
        '''收藏模版，鼠标悬停加收藏'''
        first_pct = ("xpath", "//div[@id='waterfall']/div[1]")
        # first_pct = "//div[@id='waterfall']/div[1]"
        # self.move_to_stay(first_pct)
        self.mouse_hover(first_pct)
        self.sleep(2)
        lovr_button = ('xpath', "//div[@id='waterfall']/div[1]//div[@class='item-collect']/span")
        attr = self.getElementAttr(lovr_button, 'class')
        if attr == "iconfont icon-collected icon-uncollection":  # 未收藏
            self.ptclick(lovr_button)
        elif attr == "iconfont icon-collected icon-collection":  # 已收藏
            self.ptclick(lovr_button)
            self.ptclick(lovr_button)
        else:
            self.logger.info("模板收藏按钮没有获取到")
        self.sleep()
        self.home_button()

    def qiye_template_center_picture(self):
        '''收藏模版，鼠标悬停加收藏'''
        first_pct = "//div[@class='content-container']/div[1]/div[1]/div[1]"
        self.move_to_stay(first_pct)
        self.sleep(2)
        lovr_button = ('xpath', "//div[@class='content-container']/div[1]/div[1]//div[@class='alert-box']/div[2]")
        attr = self.getElementAttr(lovr_button, 'class')
        if attr == "collect iconfont icon-collected icon-uncollection":  # 未收藏
            self.ptclick(lovr_button)
        elif attr == "collect iconfont icon-collected icon-collection":  # 已收藏
            self.ptclick(lovr_button)
            self.ptclick(lovr_button)
        else:
            self.logger.info("模板收藏按钮没有获取到")
        self.sleep()

    # ======================== 视频模板==================
    # =================================================

    def click_videoTemp(self):
        '''视频模版'''
        # self.home_button()
        vdiu = ('xpath', "//li[@class='block-item video-template']")
        self.click(vdiu)
        self.sleep()

    # 在模板中心获取视频模板名称
    # https://www.isheji.com/video_0_0_1?source=template&classify=4&entry=0&search_all=0
    def getVideoTempView(self):
        video_assert = ('xpath', "//div[@class='search-module']/section/div[1]/div[2]/span[7]/a")
        text = self.getText(video_assert)
        return text

    # 测试点击左侧导航视频模板菜单
    def test_click_videoTemp(self):
        try:
            self.home_button()
            self.click_videoTemp()
            # 获取断言
            text = self.getVideoTempView()
            self.assert_text("视频模板", str(text).strip())
        except Exception as e:
            self.logger.error('失败:点击左侧导航视频模板菜单%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:点击左侧导航视频模板菜单")
            raise e

    def video_use(self):
        '''用途'''
        yongt = ('xpath', "//span[@typeid='11']")
        self.click(yongt)
        self.sleep()

    def video_styal(self):
        '''风格'''
        styal = ('xpath', "//i[@class='iconfont icon-moreandmore-copy']")
        self.click(styal)
        fengg = ('xpath', "//span[@typeid='12']")
        self.click(fengg)
        self.sleep()

    def video_vlog(self):
        '''模版'''
        first_pct = "//div[@class='item_link']/img[@class='lazy-load']"
        self.move_to_stay(first_pct)
        lovr_button = ('xpath', "//div[@class='continer']//div[1]//div[1]//div[2]")
        self.click(lovr_button)
        self.sleep()

    def new_media_online(self):
        '''新媒体配图：线上'''
        new_media = ('xpath', "//ul[@class='default']//ul[3]/li[@class='block-item template-new-media']")
        self.click(new_media)

    def new_media_test(self):
        '''新媒体配图：测试'''
        new_media = ('xpath', "//li[@class='block-item template-new-media']//span[@class='block-text']")
        self.click(new_media)

    def new_media_graphics(self):
        '''新媒体配图'''
        self.appoint_url(self.new_media_online, self.new_media_test)
        self.sleep()
        text = ('xpath', "//div[@class='search-item-content industrylist']//span[4]//a[1]")
        actual = self.getText(text)
        expect = '互联网'
        self.assert_in_abnormal(expect, actual)
        self.sleep()

    def new_media_scenne(self):
        '''社交生活----手机壁纸'''
        secondary_graph = ('xpath', "//div[@class='search-item-content typelist']//span[3]//a[1]")
        self.click(secondary_graph)
        self.sleep()

    def new_media_purpose(self):
        '''社交生活---互联网科技'''
        purpose = ('xpath', "//div[@class='search-item-content industrylist']//span[4]//a[1]")
        self.click(purpose)
        self.sleep()

    # def home_page(self):
    #     self.home_button()

    def marketing_poster(self):
        '''点击首页左侧导航--营销海报'''
        poster = ('xpath', "//li[@class='block-item template-marketing']//span[@class='block-text']")
        self.click(poster)
        self.sleep()
        long_picture = ('xpath', "//div[@class='search-item-content typelist']//span[3]//a[1]")
        actual = self.getText(long_picture)
        expect = '营销长图'
        self.assert_text(expect, actual)
        self.sleep()

    def marketing_poster_long(self):
        '''点击营销长图'''
        long_picture = ('xpath', "//div[@class='search-item-content typelist']//span[4]//a[1]")
        self.click(long_picture)

    def social_life(self):
        '''点击社交生活'''
        life = ('xpath', "//li[@class='block-item template-social']//span[@class='block-text']")
        self.click(life)
        secondary_graph = ('xpath', "//div[@class='search-item-content typelist']//span[3]//a[1]")
        actual = self.getText(secondary_graph)
        expect = '手机壁纸'
        self.assert_text(expect, actual)
        self.sleep()
