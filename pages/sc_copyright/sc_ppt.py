import time
from common.readLog import Log
from common.sendDingTalk import SendDingTalk
from model.scModel.pptModel import PPTModel
from model.scModel.favoritesModel import FavoritesModel
from model.scModel.vipModel import VIPModel
from model.scModel.commModel import CommModel

#===========================
#   PPT模块
#   2022-08-10 Milo
#==========================
class ScPPT(PPTModel,FavoritesModel,VIPModel,CommModel):
    log = Log(__name__)
    logger = log.getLog()

    # 0. 在首页进入PPT模块
    def test_into_ppt(self):
        try:
            self.click_ppt_menu()
            num = self.ppt_search_result()
            self.logger.info(f'进入PPT模块，搜索到{num}个PPT模板')
            assert num > 0
        except Exception as e:
            self.logger.error("版权站-在首页进入PPT模块异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在首页进入PPT模块失败")
            raise e

    # 1. 在PPT模板列表收藏模板
    def test_ppt_coll(self,driver):
        try:
            for i in range(3, 5):
                pic_element = ('xpath', "//div[@class='search-item']/div["+str(i)+"]")
                pic_coll_alt = ('xpath', "//div[@class='search-item']/div["+str(i)+"]//div[@class='image-item-shadowbox']//img[@alt='']") # 获取属性
                pic_coll_btn = ('xpath', "//div[@class='search-item']/div["+str(i)+"]//div[@class='image-item-shadowbox']//img")
                self.mouse_hover(pic_element)
                self.sleep(2)
                alt = self.ppt_is_coll(pic_coll_alt)
                if alt == False:  # 已收藏
                    self.click(pic_coll_btn)
                self.sleep(2)
                alt = self.ppt_is_coll(pic_coll_alt)
                tips = self.coll_material(alt,pic_coll_btn,driver)
                self.logger.info("获取到的收藏成功提示：%s" % tips)
                assert "素材已成功" in tips
                self.sleep(2)
        except Exception as e:
            self.logger.error("版权站-在PPT模版列表收藏模板异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在PPT模版列表收藏模板失败")
            raise e

    # 2. 打开PPT详情
    def test_open_ppt_detail(self):
        try:
            self.ppt_click_first()
            self.sleep(1)
            self.window(-1)
            ppt_name = self.ppt_detail_get_name()
            assert ppt_name !=""
        except Exception as e:
            self.logger.error("版权站-PPT模版详情页获取模板名称异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-PPT模版详情页获取模板名称失败")
            raise e

    # 3. 在PPT详情页点击下载源文件
    def test_ppt_detail_download_source_file(self,driver):
        try:
            res_tips = ""
            tips_text = ['下载成功', '您的团队已下载过该PPT，为您免费重复下载']
            tips_list = self.ppt_get_tips_list()
            flag = False
            cont = 0
            self.ppt_detail_download_source_file()
            # 选择文件夹
            try:
                folder_num = self.get_list_folder()
                if folder_num == 0:
                    self.write_folder_name()
                    self.click_coll_sure_btn()  # 为了保存
                if folder_num >=1:
                    self.select_coll_folder(driver)
                    self.sleep(3)
                    for i in tips_list:
                        res = self.getElements(i)
                        if len(res) == 0:
                            cont += 1
                            continue
                        if len(res) != 0:
                            res_tips = self.getText(i)
            except:
                while flag == False and cont < 5:
                    self.ppt_detail_download_source_file()
                    self.sleep(3)
                    for i in tips_list:
                        res = self.getElements(i)
                        if len(res) == 0:
                            cont += 1
                            continue
                        if len(res) != 0:
                            res_tips = self.getText(i)
                            flag = True
            assert res_tips in tips_text
        except Exception as e:
            self.logger.error("版权站-在PPT详情页点击下载源文件异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在PPT详情页点击下载源文件失败")
            raise e
    # 4. 在PPT详情页点击收藏按钮
    def test_ppt_detail_coll(self,driver):
        try:
            ppt_coll_btn_xpath = ('xpath',"//div[@class='img-detail']//span/img[@alt='']")
            alt = self.ppt_is_coll(ppt_coll_btn_xpath)
            coll_btn = ('xpath', "//section[@class='collbtn']//span") # 收藏按钮
            attr = self.getElementAttr(coll_btn,'class')
            if attr == "collection yse":
                self.click(coll_btn) # 取消收藏
            self.sleep(1)
            attr = self.getElementAttr(coll_btn,'class')
            if attr == "collection":
                tips = self.coll_material(alt,ppt_coll_btn_xpath,driver)
                assert "素材已成功" in tips
        except Exception as e:
            self.logger.error("版权站-PPT详情页点击收藏异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-PPT详情页点击收藏失败")
            raise e

    # 5.在PPT详情页无源文件下载权限,弹出VIP页面
    def test_ppt_detail_download_source_file_none(self):
        try:
            self.click_ppt_menu()
            self.ppt_click_first()
            self.sleep(2)
            self.window(-1)
            self.ppt_detail_download_source_file()
            price = self.get_alert_price()
            time.sleep(1)
            self.alert_close_btn()
            assert float(price) > 0
        except Exception as e:
            self.logger.error("版权站-在PPT详情页点击下载源文件【无权限】异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在PPT详情页点击下载源文件【无权限】失败")
            raise e

    # 6.点击推荐的关键词
    def test_ppt_click_keyword(self):
        try:
            keyname = self.other_click_keyword()
            self.window(-1)
            key = self.get_input_key()
            assert keyname == key
        except Exception as e:
            self.logger.error("版权站-在PPT详情页点击关键词异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在PPT详情页点击关键词失败")
            raise e

    # 7. 个人身份 在PPT详情页，点击“单张购买”
    def test_ppt_detail_buy_vip(self):
        try:
            self.click_leaflet_meal()
            self.sleep(1)
            self.window(-1)
            vip_url = self.getUrl()
            assert "solavip" in vip_url
            self.close_handle()
        except Exception as e:
            self.close_handle()
            self.logger.error("版权站-在PPT详情页，点击【单张购买】异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在PPT详情页，点击【单张购买】失败")
            raise e