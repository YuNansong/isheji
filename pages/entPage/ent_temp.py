from common.readLog import Log
from common.path import psd
from common.sendDingTalk import SendDingTalk
from model.entModel.entIndexModel import EntIndexModel
from model.entModel.entTempModel import EntTempModel
from model.entModel.entMyCollModel import EntMyCollModel
from pages.entPage.ent_commont import EntCommont

class EnterpirseTemp(EntIndexModel,EntTempModel):
    '''我的企业：企业空间'''
    log = Log(__name__)
    logger = log.getLog()

    # 进入企业模板
    def test_act_ent_temp(self):
        self.click_manage()
        self.click_ent_temp()

    # 点击右侧导航--企业模板
    def test_right_menu_temp(self):
        try:
           self.right_menu_temp()
        except Exception as e:
            self.logger.error('企业-进入企业模板失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业-进入企业模板失败")
            raise e

    # 新建文件夹功能
    def test_add_folder(self, driver):
        msg = "企业-企业模板-新建文件夹失败"
        EntCommont(driver).test_add_folder(msg)
    # 重命名文件夹功能
    def test_rename_folder(self, driver):
        msg = "企业-企业模板-重命名文件夹失败"
        EntCommont(driver).test_rename_folder(msg)

    # 删除文件夹功能
    def test_delete_folder(self, driver):
        msg = "企业-企业模板-删除文件夹失败"
        EntCommont(driver).test_delete_folder(msg)

    # 上传模板
    def test_upload_modo(self, driver):
        msg = "企业-企业模板-上传模板失败"
        EntCommont(driver).test_upload_pictemp(driver,msg)

    # 重命名模板
    def test_rename_pictemp(self, driver):
        msg = "企业-企业模板-重命名模板失败"
        EntCommont(driver).test_rename_pictemp(driver,msg)

    # 移动模板
    def test_move_pictemp(self,driver):
        msg = "企业-企业模板-移动模板失败"
        EntCommont(driver).test_move_pictemp(driver,msg)

    # 删除模板
    def test_delete_pictemp(self,driver):
        msg = "企业-企业模板-删除模板失败"
        self.test_right_menu_temp()
        EntCommont(driver).test_delete_pictemp(driver,msg)

    # 下载文件--企业模板
    def test_click_download_pictemp(self,driver):
        try:
            self.refresh()
            pic_num = self.get_pictemp_num() # 获取模板个数
            if pic_num < 0:
                self.test_upload_modo(driver) # 上传模板

            pic_num = self.get_pictemp_num() # 获取模板个数
            if pic_num > 0:
                self.hover_temp()
                self.click_pic_temp_more()
                self.click_download_temp()
        except Exception as e:
            self.logger.error('企业--企业模板--下载模板失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业--企业模板--下载模板失败")
            raise e

    # 访问我的收藏
    def act_mycoll(self,driver):
        self.click_manage()
        self.click_ent_myColl()
        mycoll_pictemp_num = EntMyCollModel(driver).get_pictemp_num()
        return mycoll_pictemp_num

    # 收藏文件
    def test_click_coll_pictemp(self,driver):
        try:
            # 进入到我收藏页面，查看是否新增
            mycoll_pictemp_num = self.act_mycoll(driver)
            self.sleep(2)
            self.click_manage()
            self.click_ent_temp()
            pic_num = self.get_pictemp_num() # 获取模板个数
            if pic_num < 0:
                self.test_upload_modo(driver) # 上传模板
            if pic_num > 0:
                self.hover_temp()
                self.click_pic_temp_more()
                self.click_coll_temp()
                # 进入到我收藏页面，查看是否新增
                mycoll_pictemp_num_new = self.act_mycoll(driver)
                num = mycoll_pictemp_num_new - mycoll_pictemp_num
                assert num == 1
        except Exception as e:
            self.logger.error('企业--企业模板--收藏模板失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业--企业模板--收藏模板失败")
            raise e

    def set_team_modo(self,driver):
        '''设置团队模版'''
        try:
            self.upload_temp()
            self.add_pic_file(psd)
            self.sleep(3)
            temp_url = self.get_qiye_url()
            try:
                self.jump_work()
            except:
                self.logger.info("跳过按钮没有出现")

            self.save_temp(driver) # 模板保存按钮
            self.set_ent_team_temp() # 设置为团队模板
            self.save_new_temp() # 保存新模板
            try:
                self.sure_save_btn() # 确定保存
            except:
                self.logger.info("确认保存模版弹框没有出现")
            self.sleep(1)
            tips = self.get_save_succ_tips()
            assert tips == "保存成功"
            # 返回团队模板
            self.back_team_temp()
        except Exception as e:
            self.logger.error('模板--设置为团队模板异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("模板--设置为团队模板失败")
            raise e