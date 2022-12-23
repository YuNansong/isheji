from common.sendDingTalk import SendDingTalk
from model.entModel.entIndexModel import EntIndexModel
from model.entModel.entTempModel import EntTempModel
from pages.entPage.ent_commont import EntCommont
from common.readLog import Log


class MyDesign(EntIndexModel,EntTempModel):
    log = Log(__name__)
    logger = log.getLog()

    def test_act_my_design(self):
        self.click_manage()
        self.click_ent_mydesign()

    # 新建文件夹功能
    def test_add_folder(self, driver):
        msg = "企业-我的设计-新建文件夹失败"
        EntCommont(driver).test_add_folder(msg)

    # 测试双击打开文件夹
    def test_open_folder(self):
        try:
            # 双击文件夹 是否可以查看移动成功
            file_num = self.open_folder()
            # 断言：
            self.sleep(2)
            folder_num = self.get_folder_num()
            self.sleep(1)
            pictemp_num = self.get_pictemp_num()
            all_num = folder_num + pictemp_num
            # 点击全部
            allfolder_xpath = ('xpath',"//li[@class='second-title-li']/span[contains(text(),'全部')]")
            self.click(allfolder_xpath)
            assert file_num == all_num
        except Exception as e:
            self.logger.error('企业--我的设计-打开文件夹异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业--我的设计-打开文件夹失败")
            raise e

    # 重命名文件夹功能
    def test_rename_folder(self, driver):
        msg = "企业-我的设计-重命名文件夹失败"
        EntCommont(driver).test_rename_folder(msg)

    # 删除文件夹功能
    def test_delete_folder(self, driver):
        msg = "企业-我的设计-删除文件夹失败"
        EntCommont(driver).test_delete_folder(msg)

    # 上传模版
    def test_upload_temp(self,driver):
        msg = "企业-我的设计-上传模板失败"
        EntCommont(driver).test_upload_pictemp(driver,msg)

    # 重命名模板
    def test_rename_pictemp(self,driver):
        msg = "企业-我的设计-重命名模板失败"
        EntCommont(driver).test_rename_pictemp(driver,msg)

    # 移动模板
    def test_move_pictemp(self,driver):
        msg = "企业-我的设计-移动模板失败"
        EntCommont(driver).test_move_pictemp(driver,msg)

    # 删除模板
    def test_delete_pictemp(self,driver):
        msg = "企业-我的设计-删除模板失败"
        EntCommont(driver).test_delete_pictemp(driver,msg)



    #我的设计移动模版
    def test_mydesign_move(self,driver):
        msg = "企业-我的设计-移动文件夹失败"
        EntCommont(driver).test_move_pictemp(driver,msg)



    # 在我的设计页面点击模板
    def test_picture_template(self,driver):
        try:
            pic_num = self.get_pictemp_num()
            if pic_num > 0:
                self.logger.info("进入到我的设计页面，点击图片模板")
                self.click_last_temp() # 点击最后一个模板
                self.sleep(2)
                self.window(-1)
                temp_url = self.get_qiye_url()
                try:
                    self.jump_work()
                except:
                    self.logger.info("跳过按钮没有出现")
                self.save_temp(driver) # 模板保存按钮
                if "designworkbench" in temp_url:
                    # self.get_temp_title() # 在工作台获取模板title
                    temp_id = self.get_temp_id(driver) # 获取模板ID
                    self.logger.info("打开模板后获取到的模板ID：%d" %temp_id)
                    assert int(temp_id) > 0
                    self.close_handle()
        except Exception as e:
            self.logger.error('企业--我的设计-点击最后一个模板进入工作台异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业--我的设计-点击最后一个模板进入工作台失败")
            raise e

    # # 我的设计重命名模版
    # def test_mydesign_renmae(self,driver):
    #     self.logger.info("进入到企业--我的设计-重命名模版")
    #     try:
    #         name = "新模版名称"
    #         pic_num = self.get_pictemp_num()
    #         if pic_num <= 0:
    #             self.test_upload_temp(driver)
    #
    #         if pic_num > 0:
    #             self.hover_temp()
    #             self.click_pic_temp_more()
    #             self.sleep(1)
    #             self.rename_temp()
    #             self.sleep(1)
    #             self.input_new_temp(name) # 请输入名称
    #             self.click_sure_rename_btn()
    #             temp_name = self.get_temp_name() # 获取模板名称
    #             assert str(temp_name).strip() == name
    #     except Exception as e:
    #         self.logger.error('企业--我的设计-重命名模版异常%s' % repr(e))
    #         SendDingTalk().sendDingTalkMsg("企业--我的设计-重命名模版异常")
    #         raise e

