import time
from common.readLog import Log
from common.sendDingTalk import SendDingTalk
from model.scModel.exemptModel import ExemptModel
from model.scModel.favoritesModel import FavoritesModel
from model.scModel.vipModel import VIPModel
from model.scModel.commModel import CommModel


# ===========================
#   免抠元素模块
#   2022-08-10 Milo
# ==========================
class ScExempt(ExemptModel, FavoritesModel, VIPModel, CommModel):
    log = Log(__name__)
    logger = log.getLog()

    # 0. 在首页进入免抠元素模块
    def test_into_exempt(self):
        try:
            self.click_exempt_menu()
            num = self.exempt_search_result()
            self.logger.info(f'进入免抠元素模块，搜索到{num}个免抠元素模板')
            assert num > 0
        except Exception as e:
            self.logger.error("版权站-在首页进入免抠元素模块异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在首页进入免抠元素模块失败")
            raise e

    # 1. 在免抠元素模板列表收藏模板
    def test_exempt_coll(self, driver):
        try:
            for i in range(3, 5):
                pic_element = ('xpath', "//div[@id='coryright-exempt-list']/div[" + str(i) + "]")
                pic_coll_alt = ('xpath', "//div[@id='coryright-exempt-list']/div[" + str(
                    i) + "]//div[@class='image-item-shadowbox']//img[@alt='']")  # 获取属性
                pic_coll_btn = ('xpath', "//div[@id='coryright-exempt-list']/div[" + str(
                    i) + "]//div[@class='image-item-shadowbox']//img")
                self.mouse_hover(pic_element)
                self.sleep(2)
                alt = self.exempt_is_coll(pic_coll_alt)
                if alt == False:  # 已收藏
                    self.click(pic_coll_btn)
                self.sleep(2)
                alt = self.exempt_is_coll(pic_coll_alt)
                tips = self.coll_material(alt, pic_coll_btn, driver)
                self.logger.info("获取到的收藏成功提示：%s" % tips)
                assert "素材已成功" in tips
                self.sleep(2)
        except Exception as e:
            self.logger.error("版权站-在免抠元素模版列表收藏模板异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在免抠元素模版列表收藏模板失败")
            raise e

    # 2. 打开免抠元素详情
    def test_open_exempt_detail(self):
        try:
            self.exempt_click_first()
            self.sleep(1)
            self.window(-1)
            exempt_name = self.exempt_detail_get_name()
            assert exempt_name != ""
        except Exception as e:
            self.logger.error("版权站-免抠元素模版详情页获取模板名称异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-免抠元素模版详情页获取模板名称失败")
            raise e

    # 3. 在免抠元素详情页点击下载源文件
    def test_exempt_detail_download_source_file(self, driver):
        try:
            res_tips = ""
            tips_text = ['下载成功', '您的团队已下载过该免抠元素，为您免费重复下载']
            tips_list = self.exempt_get_tips_list()
            flag = False
            cont = 0
            self.exempt_detail_download_source_file()
            # 选择文件夹
            try:
                folder_num = self.get_list_folder()
                if folder_num == 0:
                    self.write_folder_name()
                    self.click_coll_sure_btn()  # 为了保存
                if folder_num >= 1:
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
                    self.exempt_detail_download_source_file()
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
            self.logger.error("版权站-在免抠元素详情页点击下载源文件异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在免抠元素详情页点击下载源文件失败")
            raise e

    # 4. 在免抠元素详情页点击收藏按钮
    def test_exempt_detail_coll(self, driver):
        try:
            exempt_coll_btn_xpath = ('xpath', "//div[@class='img-detail']//span/img[@alt='']")
            alt = self.exempt_is_coll(exempt_coll_btn_xpath)
            coll_btn = ('xpath', "//section[@class='collbtn']//span")  # 收藏按钮
            attr = self.getElementAttr(coll_btn, 'class')
            if attr == "collection yse":
                self.click(coll_btn)  # 取消收藏
            self.sleep(1)
            attr = self.getElementAttr(coll_btn, 'class')
            if attr == "collection":
                tips = self.coll_material(alt, exempt_coll_btn_xpath, driver)
                assert "素材已成功" in tips
        except Exception as e:
            self.logger.error("版权站-免抠元素详情页点击收藏异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-免抠元素详情页点击收藏失败")
            raise e

    # 5.在免抠元素详情页无源文件下载权限,弹出VIP页面
    def test_exempt_detail_download_source_file_none(self):
        try:
            self.click_exempt_menu()
            self.exempt_click_first()
            self.sleep(2)
            self.window(-1)
            self.exempt_detail_download_source_file()
            price = self.get_alert_price()
            time.sleep(1)
            self.alert_close_btn()
            assert float(price) > 0
        except Exception as e:
            self.logger.error("版权站-在免抠元素详情页点击下载源文件【无权限】异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在免抠元素详情页点击下载源文件【无权限】失败")
            raise e

    # 6.点击推荐的关键词
    def test_exempt_click_keyword(self):
        try:
            keyname = self.other_click_keyword()
            self.window(-1)
            key = self.get_input_key()
            assert keyname == key
        except Exception as e:
            self.logger.error("版权站-在免抠元素详情页点击关键词异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在免抠元素详情页点击关键词失败")
            raise e

    # 7. 个人身份 在免抠元素详情页，点击“单张购买”
    def test_exempt_detail_buy_vip(self):
        try:
            self.click_leaflet_meal()
            self.sleep(1)
            self.window(-1)
            vip_url = self.getUrl()
            assert "solavip" in vip_url
            self.close_handle()
        except Exception as e:
            self.close_handle()
            self.logger.error("版权站-在免抠元素详情页，点击【单张购买】异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在免抠元素详情页，点击【单张购买】失败")
            raise e

    # 8.在免抠元素详情页无样图下载权限
    def test_exempt_detail_download_yangtu_none(self):
        try:
            self.click_exempt_menu()
            self.exempt_click_first()
            self.sleep(2)
            self.window(-1)
            self.exempt_detail_download_yangtu()
            title = self.design_detail_get_apply()
            time.sleep(1)
            # self.design_detail_close_apply()
            assert title == "下载成功"
        except Exception as e:
            self.logger.error("版权站-在免抠元素详情页点击下载样图【无权限】异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在免抠元素详情页点击下载样图【无权限】失败")
            raise e
