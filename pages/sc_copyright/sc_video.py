import time
from common.readLog import Log
from common.sendDingTalk import SendDingTalk
from model.scModel.videoModel import VideoModel
from model.scModel.favoritesModel import FavoritesModel
from model.scModel.vipModel import VIPModel
from model.scModel.commModel import CommModel

#===========================
#   视频模块
#   2022-08-02 Milo
#==========================
class ScVideo(VideoModel,FavoritesModel,VIPModel,CommModel):
    log = Log(__name__)
    logger = log.getLog()

    # 0. 在首页进入视频模块
    def test_into_video(self):
        try:
            self.click_video_menu()
            num = self.video_search_result()
            self.logger.info(f'进入视频模块，搜索到{num}个视频模板')
            assert num > 0
        except Exception as e:
            self.logger.error("版权站-在首页进入视频模块异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在首页进入视频模块失败")
            raise e

    # 1. 在视频模板列表收藏模板
    def test_video_coll(self,driver):
        try:
            for i in range(3, 5):
                pic_element = ('xpath', "//div[@id='coryright-video-list']/div["+str(i)+"]")
                pic_coll_alt = ('xpath', "//div[@id='coryright-video-list']/div["+str(i)+"]//div[@class='image-item-shadowbox']//img[@alt='']") # 获取属性
                pic_coll_btn = ('xpath', "//div[@id='coryright-video-list']/div["+str(i)+"]//div[@class='image-item-shadowbox']//img")
                self.mouse_hover(pic_element)
                self.sleep(2)
                alt = self.video_is_coll(pic_coll_alt)
                if alt == False:  # 已收藏
                    self.click(pic_coll_btn)
                self.sleep(2)
                alt = self.video_is_coll(pic_coll_alt)
                tips = self.coll_material(alt,pic_coll_btn,driver)
                self.logger.info("获取到的收藏成功提示：%s" % tips)
                assert "素材已成功" in tips
                self.sleep(2)
        except Exception as e:
            self.logger.error("版权站-在视频模版列表收藏模板异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在视频模版列表收藏模板失败")
            raise e

    # 2. 打开详情
    def test_open_video_detail(self):
        try:
            self.video_click_first()
            self.sleep(1)
            self.window(-1)
            video_name = self.video_detail_get_name()
            assert video_name !=""
        except Exception as e:
            self.logger.error("版权站-视频模版详情页获取模板名称异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-视频模版详情页获取模板名称失败")
            raise e

    # 3. 在视频详情页点击下载源文件
    def test_video_detail_download_source_file(self,driver):
        try:
            res_tips = ""
            tips_text = ['下载成功', '您的团队已下载过该视频，为您免费重复下载']
            tips_list = self.video_get_tips_list()
            flag = False
            cont = 0
            self.video_detail_download_source_file()
            # 选择文件夹
            try:
                folder_num = self.get_list_folder()
                if folder_num == 0:
                    self.write_folder_name()
                    self.click_coll_sure_btn()  # 为了保存
                if folder_num >=1:
                    self.select_coll_folder(driver)
                    self.sleep(5)
                    for i in tips_list:
                        res = self.getElements(i)
                        if len(res) == 0:
                            cont += 1
                            continue
                        if len(res) != 0:
                            res_tips = self.getText(i)
            except:
                while flag == False and cont < 5:
                    self.video_detail_download_source_file()
                    self.sleep(3)
                    for i in tips_list:
                        res = self.getElements(i)
                        if len(res) == 0:
                            cont += 1
                            continue
                        if len(res) != 0:
                            res_tips = self.getText(i)
                            flag = True
        except Exception as e:
            self.logger.error("版权站-在视频详情页点击下载源文件异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在视频详情页点击下载源文件失败")
            raise e
    # 4. 在视频详情页点击收藏按钮
    def test_video_detail_coll(self,driver):
        try:
            video_coll_btn_xpath = ('xpath',"//div[@class='right']//div[@class='top']/span/img[@alt='']")
            alt = self.video_is_coll(video_coll_btn_xpath)
            coll_btn = ('xpath', "//div[@class='top']/span[1]") # 收藏按钮
            attr = self.getElementAttr(coll_btn,'class')
            if attr == "collection yse":
                self.click(coll_btn) # 取消收藏
            self.sleep(1)
            attr = self.getElementAttr(coll_btn,'class')
            if attr == "collection no":
                tips = self.coll_material(alt,video_coll_btn_xpath,driver)
                assert "素材已成功" in tips
        except Exception as e:
            self.logger.error("版权站-视频详情页点击收藏异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-视频详情页点击收藏失败")
            raise e

    # 5.在视频详情页无源文件下载权限,弹出VIP页面
    def test_video_detail_download_source_file_none(self):
        try:
            self.click_video_menu()
            self.video_click_first()
            self.sleep(2)
            self.window(-1)
            self.video_detail_download_source_file()
            price = self.get_alert_price()
            time.sleep(1)
            self.alert_close_btn()
            assert float(price) > 0
        except Exception as e:
            self.logger.error("版权站-在视频详情页点击下载源文件【无权限】异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在视频详情页点击下载源文件【无权限】失败")
            raise e

    # 6.点击推荐的关键词
    def test_video_click_keyword(self):
        try:
            keyname = self.click_keyword()
            self.window(-1)
            key = self.get_input_key()
            assert keyname == key
            self.close_handle()
        except Exception as e:
            self.close_handle()
            self.logger.error("版权站-在视频详情页点击关键词异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在视频详情页点击关键词失败")
            raise e

    # 7. 个人身份 在视频详情页，点击“单张购买”
    def test_video_detail_buy_vip(self):
        try:
            self.click_leaflet_meal()
            self.sleep(1)
            self.window(-1)
            vip_url = self.getUrl()
            assert "solavip" in vip_url
            self.close_handle()
        except Exception as e:
            self.close_handle()
            self.logger.error("版权站-在视频详情页，点击【单张购买】异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在视频详情页，点击【单张购买】失败")
            raise e