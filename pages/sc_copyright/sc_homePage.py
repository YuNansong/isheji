from common.sendDingTalk import SendDingTalk
from common.getYaml import url
from common.readLog import Log
from element.sc_copyright.sc_home_element import SCHomePageElement
from model.scModel.homeModel import HomeModel
from model.scModel.vipModel import VIPModel
from model.scModel.picModel import PicModel
from model.scModel.favoritesModel import FavoritesModel
from model.scModel.videoDetailModel import VideoDetailModel
from model.scModel.commModel import CommModel


class SCHomePage(HomeModel, VIPModel, PicModel, FavoritesModel, VideoDetailModel, CommModel):
    log = Log(__name__)
    logger = log.getLog()

    # 热门推荐，第一个图集
    def test_hot_tuijian(self):
        try:
            self.mouse_hover(SCHomePageElement.first_pic)
            text_num = self.getText(SCHomePageElement.first_pic_num_xpath)
            num = int(text_num[1:-3])  # 获取图集上的数字
            self.click(SCHomePageElement.first_pic)
            self.window(-1)
            pic_list = self.getElements(SCHomePageElement.pic_list_xpath)
            pic_num = len(pic_list)
            assert num >= pic_num
            self.close_handle()
        except Exception as e:
            self.logger.error("版权站-首页点击热门推荐的图片异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-首页点击热门推荐的图片失败")
            raise e

    # 获取视频名称
    def test_video_material(self):
        try:
            self.click(SCHomePageElement.first_video_xpath)
            self.sleep(2)
            self.window(-1)
            video_name = self.get_video_name()
            video_id = self.get_video_id()
            self.logger.info("获取到的视频名称为%s" % video_name)
            self.logger.info("获取到的视频名称为%s" % video_id)
            self.close_handle()
            assert video_name != ""
            assert video_id != ""
        except Exception as e:
            self.logger.error("版权站-首页点击视频名称异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-首页点击视频名称失败")
            raise e

    # 图片素材
    def test_pic_material(self):
        try:
            self.click(SCHomePageElement.first_img_xpath)
            self.sleep(2)
            self.window(-1)
            # 获取视频名称
            img_name = self.getText(SCHomePageElement.img_name_xpath)
            img_id = self.getText(SCHomePageElement.img_id_xpath)
            self.logger.info("获取到的图片素材为：%s" % img_name)
            self.logger.info("获取到的图片素材为：%s" % img_id)
            self.close_handle()  # 关闭窗口
            assert img_name != ""
            assert img_id != ""
        except Exception as e:
            self.logger.error("版权站-首页点击图片素材异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-首页点击图片素材失败")
            raise e

    # 平面模板
    def test_temp_material(self):
        try:
            self.click(SCHomePageElement.first_temp_xpath)
            self.window(-1)
            self.sleep(2)
            temp_name = self.getText(SCHomePageElement.temp_name_xpath)
            temp_id = self.getText(SCHomePageElement.temp_id_xpath)
            self.logger.info("获取到的平面模板ID:%s 名称为：%s" % (temp_id, temp_name))
            self.close_handle()  # 关闭窗口
            assert temp_name != ""
            assert temp_id != ""
        except Exception as e:
            self.logger.error("版权站-首页点击平面模板异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-首页点击平面模板失败")
            raise e

    # 点击PPT模板
    def test_ppt_material(self):
        try:
            self.click(SCHomePageElement.first_ppt_xpath)
            self.window(-1)
            self.sleep(2)
            ppt_name = self.getText(SCHomePageElement.ppt_name_xpath)
            ppt_id = self.getText(SCHomePageElement.ppt_id_xpath)
            self.logger.info("获取到的PPT模板ID:%s 名称为：%s" % (ppt_id, ppt_name))
            self.close_handle()  # 关闭窗口
            assert ppt_name != ""
            assert ppt_id != ""
        except Exception as e:
            self.logger.error("版权站-首页点击PPT模板异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-首页点击PPT模板失败")
            raise e

    # 点击免抠元素
    def test_exempt_material(self):
        try:
            self.click(SCHomePageElement.first_exempt_xpath)
            self.window(-1)
            self.sleep(2)
            exempt_name = self.getText(SCHomePageElement.exempt_name_xpath)
            exempt_id = self.getText(SCHomePageElement.exempt_id_xpath)
            self.logger.info("获取到的PPT模板ID:%s 名称为：%s" % (exempt_id, exempt_name))
            self.close_handle()  # 关闭窗口
            assert exempt_name != ""
            assert exempt_id != ""
        except Exception as e:
            self.logger.error("版权站-首页点击免抠元素异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-首页点击免抠元素失败")
            raise e

    # 在专题推荐模块-获取分类
    def test_hot_pic(self):
        try:
            clas_num = len(self.getElements(SCHomePageElement.hot_pic_class_element))
            for i in range(1, int(clas_num)):
                pic_class_name_xpath = ('xpath', "//div[@class='temp-zt']/div/div/div[" + str(i) + "]//p")
                title = self.getText(pic_class_name_xpath)
                self.logger.info("版权站-首页点击专题推荐分类获取到分类名称%s" % title)
                pic_class_element = ('xpath', "//div[@class='temp-zt']/div/div/div[" + str(i) + "]")
                self.click(pic_class_element)
                if i == 3:
                    break
        except Exception as e:
            self.logger.error("版权站-首页点击热门图集异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-首页点击热门图集失败")
            raise e

    # 专题推荐点击查看更多
    def test_click_specialmore(self):
        try:
            urlInfo = url['url']['testUrl']
            self.sleep(1)
            self.click(SCHomePageElement.zt_more_btn_element)
            self.sleep(2)
            self.window(-1)
            domain = self.getUrl()
            self.logger.info("专题点击查看更多获取到URL:%s" % domain)
            self.close_handle()
            assert urlInfo + "/specialmore" in domain
        except Exception as e:
            self.logger.error("版权站-首页专题推荐点击查看更多异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-首页专题推荐点击查看更多失败")
            raise e

    # 专题推荐--下载样图--(无额度)
    def test_download_pic_none(self):
        try:
            self.logger.info("================1==============")
            self.window(-1)
            self.mouse_hover_pic()
            self.click(SCHomePageElement.down_load_yangtu_xpath)
            self.sleep(1)
            # 样图下载提示
            title = self.apply_title()
            assert title == "下载成功"
        except Exception as e:
            self.logger.error("版权站-首页专题推荐点击下载样图(无额度)异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-首页专题推荐点击下载样图(无额度)失败")
            raise e

    # =========================
    # 首页收藏
    # ==========================

    # 判断是否已收藏
    def is_coll_pic(self, element):
        try:
            self.getElementAttr(element, "alt")  # alt 属性存在则代表未收藏
            alt = True  # 未收藏
        except:
            alt = False  # 已收藏
        return alt

    # 收藏PPT 模板
    def test_home_coll_ppt(self, driver):
        try:
            for i in range(1, 2):
                ppt_element = ('xpath', "//div[@id='ppt']/div[2]/ul/li[" + str(i) + "]/div")
                ppt_coll_alt = ('xpath', "//div[@id='ppt']/div[2]/ul/li[" + str(i) + "]/div/div//img[@alt='']")  # 获取属性
                ppt_coll_btn = ('xpath', "//div[@id='ppt']/div[2]/ul/li[" + str(i) + "]/div/div//img")
                self.mouse_hover(ppt_element)
                self.sleep(2)
                alt = self.is_coll_pic(ppt_coll_alt)
                if alt == False:  # 已收藏
                    self.click(ppt_coll_btn)
                self.sleep(2)
                alt = self.is_coll_pic(ppt_coll_alt)
                tips = self.coll_material(alt, ppt_coll_alt, driver)
                self.logger.info("获取到的收藏成功提示：%s" % tips)
                assert "素材已成功" in tips
                self.sleep(2)
        except Exception as e:
            self.logger.error("版权站-首页收藏PPT模板异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-首页收藏PPT模板失败")
            raise e

    # 收藏免抠元素
    def test_home_coll_exempt(self, driver):
        try:
            for i in range(1, 2):
                ppt_element = ('xpath', "//div[@id='exempt']/div[2]/ul/li[" + str(i) + "]/div")
                ppt_coll_alt = (
                    'xpath', "//div[@id='exempt']/div[2]/ul/li[" + str(i) + "]/div/div//img[@alt='']")  # 获取属性
                ppt_coll_btn = ('xpath', "//div[@id='exempt']/div[2]/ul/li[" + str(i) + "]/div/div//img")
                self.mouse_hover(ppt_element)
                self.sleep(2)
                alt = self.is_coll_pic(ppt_coll_alt)
                if alt == False:  # 已收藏
                    self.click(ppt_coll_btn)
                self.sleep(2)
                alt = self.is_coll_pic(ppt_coll_alt)
                tips = self.coll_material(alt, ppt_coll_alt, driver)
                self.logger.info("获取到的收藏成功提示：%s" % tips)
                assert "素材已成功" in tips
                self.sleep(2)
        except Exception as e:
            self.logger.error("版权站-首页收藏免抠元素异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-首页收藏免抠元素失败")
            raise e

    # 图片素材列表--收藏图片
    def test_coll_pic(self, driver):
        try:
            for i in range(1, 2):
                pic_element = ('xpath', "//div[@id='img']/div[2]/ul/li[" + str(i) + "]/div")
                pic_coll_alt = ('xpath', "//div[@id='img']/div[2]/ul/li[" + str(i) + "]/div/div//img[@alt='']")  # 获取属性
                pic_coll_btn = ('xpath', "//div[@id='img']/div[2]/ul/li[" + str(i) + "]/div/div//img")
                self.mouse_hover(pic_element)
                self.sleep(2)
                alt = self.is_coll_pic(pic_coll_alt)
                if alt == False:  # 已收藏
                    self.click(pic_coll_btn)
                self.sleep(2)
                alt = self.is_coll_pic(pic_coll_alt)
                tips = self.coll_material(alt, pic_coll_btn, driver)
                self.logger.info("获取到的收藏成功提示：%s" % tips)
                assert "素材已成功" in tips
                self.sleep(2)
        except Exception as e:
            self.logger.error("版权站-首页收藏图片异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-首页收藏图片失败")
            raise e

    # 测试收藏视频
    def test_coll_video(self, driver):
        try:
            for i in range(1, 3):
                video_element = ('xpath', "//div[@id='video']/div[2]/ul/li[" + str(i) + "]/div")
                video_coll_alt = (
                    'xpath', "//div[@id='video']/div[2]/ul/li[" + str(i) + "]/div/div//img[@alt='']")  # 获取属性
                video_coll_btn = ('xpath', "//div[@id='video']/div[2]/ul/li[" + str(i) + "]/div/div//img")
                self.mouse_hover(video_element)
                self.sleep(2)
                alt = self.is_coll_pic(video_coll_alt)
                if alt == False:  # 已收藏
                    self.click(video_coll_btn)
                self.sleep(2)
                alt = self.is_coll_pic(video_coll_alt)
                tips = self.coll_material(alt, video_coll_btn, driver)
                self.logger.info("获取到的收藏成功提示：%s" % tips)
                assert "素材已成功" in tips
                self.sleep(2)
        except Exception as e:
            self.logger.error("版权站-首页收藏视频异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-首页收藏视频失败")
            raise e

    # 测试收藏设计
    def test_coll_design(self, driver):
        try:
            for i in range(1, 3):
                video_element = ('xpath', "//div[@id='plane']/div[2]/ul/li[" + str(i) + "]/div")
                video_coll_alt = (
                    'xpath', "//div[@id='plane']/div[2]/ul/li[" + str(i) + "]/div/div//img[@alt='']")  # 获取属性
                video_coll_btn = ('xpath', "//div[@id='plane']/div[2]/ul/li[" + str(i) + "]/div/div//img")
                self.mouse_hover(video_element)
                self.sleep(2)
                alt = self.is_coll_pic(video_coll_alt)
                if alt == False:  # 已收藏
                    self.click(video_coll_btn)
                self.sleep(2)
                alt = self.is_coll_pic(video_coll_alt)
                tips = self.coll_material(alt, video_coll_btn, driver)
                self.logger.info("获取到的收藏成功提示：%s" % tips)
                assert "素材已成功" in tips
                self.sleep(2)
        except Exception as e:
            self.logger.error("版权站-首页收藏视频异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-首页收藏视频失败")
            raise e

    # 相似图片
    def test_similar_pic(self):
        try:
            self.page_down(100)
            self.sleep(3)
            self.mouse_hover_pic()  # 悬浮图片
            self.click(SCHomePageElement.similar_pic_btn)
            self.sleep(2)
            self.window(-1)
            domain = self.getUrl()
            assert "search" in domain
            self.close_handle()
        except Exception as e:
            self.logger.error("版权站-首页点击相似图片异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-首页点击相似图片失败")
            raise e

    # 搜索[图片，视频，音乐，设计，免抠元素，PPT]
    def test_search(self, name):
        try:
            self.page_down(100)
            for i in range(1, 6):
                type_btn_xpath = ('xpath', "//div[@class='type']")
                self.mouse_hover(type_btn_xpath)
                self.sleep(1)
                switch_type_xpath = ('xpath', "//div[@class='type']/ul/li[" + str(i) + "]")
                self.click(switch_type_xpath)
                self.write(SCHomePageElement.search_input_element, name)  # 输入搜索关键词
                self.click(SCHomePageElement.search_btn_element)  # 点击搜索框
                self.sleep(3)
                url = self.getUrl()
                type_xpath = (
                    'xpath', "//div[@class='search-title']/span")
                if "keyword=" in url:
                    num = 0
                    num = int(self.getText(type_xpath))
                    self.logger.info("版权站-首页搜索到素材数量%s" % num)
                    # if i == 1 or i == 3 or i == 4 or i == 5:
                    #     # 搜索结果页 进行判断是否选中tab
                    #     # 图片 视频,免抠元素
                    #     # num = len(self.getElements(pic_type_xpath))
                    #     num = int(self.getText(type_xpath))
                    #     self.logger.info("版权站-首页搜索到素材数量%s" % num)
                    # if i == 2:
                    #     # 搜索结果页 进行判断是否选中tab
                    #     # design_type_xpath = (
                    #     #     'xpath', "//div[@class='search-title']/span")  # type =2 设计
                    #     # num = len(self.(design_type_xpath))
                    #     num = int(self.getText(type_xpath))
                    #     self.logger.info("版权站-首页搜索到设计数量%s" % num)
                    # if i == 6:
                    #     # 搜索结果页 进行判断是否选中tab
                    #     # music_type_xpath = ('xpath', "//div[@class='search-title']/span")  # 音乐
                    #     num = len(self.getElements(type_xpath))
                    #     self.logger.info("版权站-首页搜索到音乐数量%s" % num)
                    assert num > 0
                    self.home_button()
        except Exception as e:
            self.home_button()
            self.logger.error("版权站-首页搜索素材异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-首页搜索素材失败")
            raise e

    # 点击个人VIP
    def click_personal_vip(self):
        try:
            self.click_per_vip_menu()
            shuoming_text = self.get_vip_assert_content()
            self.close_handle()
            assert shuoming_text == "商用授权详细说明"
        except Exception as e:
            self.logger.error("版权站-首页点击个人VIP菜单异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-首页点击个人VIP菜单失败")
            raise e

    # 点击企业VIP
    def click_ent_vip(self):
        try:
            self.click_ent_vip_menu()
            shuoming_text = self.get_vip_assert_content()  # 断言
            self.close_handle()
            assert shuoming_text == "商用授权详细说明"
        except Exception as e:
            self.logger.error("版权站-首页点击企业VIP菜单异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-首页点击企业VIP菜单失败")
            raise e

    # 点击收藏夹
    def test_click_coll_folder(self):
        try:
            self.click_coll_folder()
            coll_folder_name_xpath = ('xpath', "//div[@class='collect content']/div/p")
            coll_folder_name = self.getText(coll_folder_name_xpath)
            assert coll_folder_name == "收藏夹"
            self.close_handle()
        except Exception as e:
            self.close_handle()
            self.logger.error("版权站-首页点击收藏夹菜单异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-首页点击收藏夹菜单失败")
            raise e
