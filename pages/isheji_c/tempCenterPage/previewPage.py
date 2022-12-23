from pages.isheji_c.tempCenterPage.workbenchPage import WorkBench
from common.readLog import Log
from common.sendDingTalk import SendDingTalk
from model.entModel.entTempModel import EntTempModel
from model.entModel.entIndexModel import EntIndexModel

# ======================================================
# 爱设计首页-->模板-->预览页面
# https://www.isheji.com/preview/96_54555
# ======================================================

class PerviewPage(EntTempModel,EntIndexModel):
    log = Log(__name__)
    logger = log.getLog()

    # 在首页点击模板的预览按钮进入到预览页面
    def test_review_temp(self):
        self.logger.info("在首页点击模板的预览按钮进入到预览页面")
        try:
            modo_xpath = ("xpath", "//div[@id='apptc']/div[2]/div[@class='swiper-boxs']/div[1]/div/div[1]/div[@class='jbalert-box']")
            self.mouse_hover(modo_xpath)
            # self.move_to_stay("//div[@id='apptc']/div[2]/div[@class='swiper-boxs']/div[1]/div/div[1]/div[@class='jbalert-box']")
            self.sleep(2)
            eay_look = ('xpath', "//div[@id='apptc']/div[2]/div[@class='swiper-boxs']/div[1]/div/div[1]/div[@class='jbalert-box']/div/a[1]/span")
            self.click(eay_look)
            self.sleep()
            self.window(-1)
            quickBtn = ('xpath', "//div[@class='quick_use_btn']")
            quickBtnName = self.getText(quickBtn)
            print(str(quickBtnName).strip(),"=-=-=-=-=-=-=-=-=>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            assert str(quickBtnName).strip() == "立即编辑"
        except Exception as e:
            self.logger.error("在首页点击模板的预览按钮进入到预览页面异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在首页点击模板的预览按钮进入到预览页面失败")
            raise e

    # 企业端进入模板中心
    def test_act_temp_center(self):
        self.click_manage()
        self.click_temp_center()

    # 企业端进入模版预览界面
    def qiye_reivew_temp(self):
        first_pct = ('xpath',"//div[@class='content-container']/div[1]/div[1]/div[1]")
        self.mouse_hover(first_pct)
        self.sleep(1)
        lovr_button = ('xpath', "//div[@class='content-container']/div[1]/div[1]//div[@class='alert-box']/div[1]")
        self.click(lovr_button)
        self.window(-1)

    # 在预览页面点击立即使用按钮
    def test_user_temp(self, driver):
        self.logger.info("验证在模板预览页面，点击立即使用进入工作台")
        try:
            try:
                # self.close_and_window()
                # self.window(-1)
                # self.back()#页面改动
                self.sleep(2)
                # 如果进模板预览页面失败，则直接跳转到指定页面测试其他用例
                quickBtn = ('xpath', "//div[@class='quick_use_btn']")
                self.click(quickBtn)  # 点击立即使用
                self.sleep(1)
                self.window(-1)
            except:
                self.appoint_url(self.transfer_url("/preview/103_244b74c0-0cc2-11ed-9314-b522c427d328"), self.transfer_url("/preview/5_27769"))
                quickBtn = ('xpath', "//div[@class='quick_use_btn']")
                self.click(quickBtn)  # 点击立即使用
                self.sleep(1)
                self.window(-1)
            self.sleep()
            try:
                self.jump_home()  # 在工作台提示上点击跳过
            except:
                self.logger.info("进入工作台后，跳过按钮没有出现")
            sucai_text = WorkBench(driver).work_material_text()
            sucai_text_ral = str(sucai_text).strip()
            self.close_and_window()
            assert sucai_text_ral == "素材"
        except Exception as e:
            self.logger.error("测试从模板预览页面点击立即使用进入工作台异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试从模板预览页面点击立即使用进入工作台失败")
            raise e

    # 在预览页面点击立即使用按钮
    def test_qiye_user_temp(self, driver):
        self.logger.info("验证在模板预览页面，点击立即使用进入工作台")
        try:
            try:
                # 如果进模板预览页面失败，则直接跳转到指定页面测试其他用例
                quickBtn = ('xpath', "//div[@class='top_btn']")
                self.click(quickBtn)  # 点击立即使用
            except:
                self.transfer_qiye_url(self.transfer_url("/templateCenterDetail?templateId=46306&type=96"))
                quickBtn = ('xpath', "//div[@class='top_btn']")
                self.click(quickBtn)  # 点击立即使用

            self.sleep(3)
            self.window(-1)
            try:
                self.jump_home()  # 在工作台提示上点击跳过
            except:
                self.logger.info("进入工作台后，跳过按钮没有出现")
            sucai_text = WorkBench(driver).work_material_text()
            sucai_text_ral = str(sucai_text).strip()
            self.sleep(1)
            self.save_temp(driver)
            assert sucai_text_ral == "素材"
            self.sleep(1)
            self.close_and_window()
        except Exception as e:
            self.logger.error("测试从模板预览页面点击立即使用进入工作台异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试从模板预览页面点击立即使用进入工作台失败")
            raise e

    # 在预览模板页面点击推荐模版
    def test_click_reveiw_temp(self, driver):
        self.logger.info("验证在模板预览页面，点击推荐的模版进入工作台")
        try:
            try:
                self.sleep()
                temp = ('xpath', "//div[@class='middle']/div[2]/div[1]/div[1]")
                self.ptclick(temp)  # 点击推荐列表的第一个模板
            except:
                self.appoint_url(self.transfer_url("/preview/103_244b74c0-0cc2-11ed-9314-b522c427d328"), self.transfer_url("/preview/5_27769"))
                temp = ('xpath', "//div[@class='middle']/div[2]/div[1]/div[1]")
                self.ptclick(temp)  # 点击推荐列表的第一个模板
            self.sleep(3)
            self.window(-1)
            try:
                self.jump_home()  # 在工作台提示上点击跳过
            except:
                self.logger.info("进入工作台后，跳过按钮没有出现")
            sucai_text = WorkBench(driver).work_material_text()
            sucai_text_ral = str(sucai_text).strip()
            self.preservation()
            self.sleep(1)
            self.closeWindow()
            assert sucai_text_ral == "素材"
        except Exception as e:
            self.logger.error("测试从模板预览页面点击推荐模板进入工作台异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试从模板预览页面点击推荐模板进入工作台失败")
            raise e
        finally:
            # self.closeWindow()
            self.close_and_home_page()

    # C端测试在模板预览页面点击关键词
    def fving_word_key(self):
        self.logger.info("验证在模板预览页面点击关键词")
        try:
            fving = ('xpath', "//div[@class=' top_main_right right']//div[@class='tag_wrapper']/div[2]")
            expect = self.getText(fving)
            self.logger.info("在模板预览页面要点击的关键词是:%s" % expect)
            self.ptclick(fving)
            self.window(-1)
            self.sleep(3)
            key = ('xpath', "//div[@class='keyword']//span")
            actual = self.getText(key)
            self.sleep(2)
            self.logger.info("在搜索结果页获取到的关键词为:%s" % actual)
            self.assert_text(expect, actual)
            self.sleep(2)
            self.closeWindow()
            self.window(-1)
        except Exception as e:
            self.logger.error("测试在模板预览页面点击关键词异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试在模板预览页面点击关键词失败")
            raise e

    # B端测试在企业模板预览页面点击关键词
    def qiey_fving_word_key(self):
        self.logger.info("验证在模板预览页面点击关键词")
        try:
            self.qiye_reivew_temp() # 进入预览页面
            fving = ('xpath', "//div[@class='right_footer']/div[1]")
            expect = self.getText(fving)
            self.logger.info("在模板预览页面要点击的关键词是:%s" % expect)
            self.ptclick(fving)
            self.sleep(2)
            key = ('xpath', "//div[@class='record_search']/span[1]")
            num_xpath = ('xpath', "//div[@class='record_search']/span[2]")
            actual = self.getText(key)
            num = self.getText(num_xpath)
            self.sleep(1)
            self.logger.info("在搜索结果页获取到的关键词为:%s" % actual)
            self.logger.info("在搜索结果页获取到的搜索结果为:%s 个" % num)
            self.assert_text('\"'+expect+'\"', actual)
            self.sleep(1)
            self.close_handle()
        except Exception as e:
            self.logger.error("测试在模板预览页面点击关键词异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试在模板预览页面点击关键词失败")
            raise e