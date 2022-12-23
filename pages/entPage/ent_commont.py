from common.readLog import Log
from model.entModel.entTempModel import EntTempModel
from common.path import psd
from common.sendDingTalk import SendDingTalk

class EntCommont(EntTempModel):
    # 我的设计，企业模版，企业素材列表有共同的方法
    log = Log(__name__)
    logger = log.getLog()
    # 新建文件夹
    def test_add_folder(self,msg):
        try:
            folder_num = self.get_folder_num()
            self.logger.info("新建文件夹前的个数：%d" %folder_num)
            self.add_folder()
            self.input_folder_name()
            self.sure_add_folder()
            folder_num_new = self.get_folder_num()
            self.logger.info("新建文件夹后的个数：%d" %folder_num_new)
            num = folder_num_new - folder_num
            assert num == 1
        except Exception as e:
            self.logger.error(msg+'%s' % repr(e))
            SendDingTalk().sendDingTalkMsg(msg)
            raise e

    # 公共方法
    # 判断当前页面文件夹是否大于0
    def get_folder_is_true(self,msg):
        folder_num = self.get_folder_num()
        if folder_num <= 0:
            self.test_add_folder(msg)
        folder_num = self.get_folder_num()
        if folder_num > 0:
            return folder_num
        else:
            return 0

    # 判断当前页面文件是否大于0
    def get_file_is_greater_zero(self,driver,msg):
        pic_num = self.get_pictemp_num() # 获取素材个数
        if pic_num < 0:
            self.test_upload_pictemp(driver,msg)
        pic_num = self.get_pictemp_num() # 获取素材个数
        if pic_num > 0:
            return pic_num
        else:
            return 0

    # 重命名文件夹
    def test_rename_folder(self,msg):
        try:
            new_folder = "新文件夹名称"
            if self.get_folder_is_true(msg) > 0:
                # 获取第一个文件夹
                self.select_first_folder()
                self.click_folder_more()     # 点击更多
                self.sleep(1)
                self.rename_folder_name()
                self.sleep(1)

                self.input_folder_name(new_folder)
                self.sure_add_folder()
                # 获取新模版名称
                name = self.get_first_folder_name()
                assert name == new_folder
        except Exception as e:
            self.logger.error(msg+'%s' % repr(e))
            SendDingTalk().sendDingTalkMsg(msg)
            raise e
    # 删除文件夹
    def test_delete_folder(self,msg):
        try:
            old_num = self.get_folder_num()
            if self.get_folder_is_true(msg) > 0:
                self.select_first_folder() # 获取第一个文件夹
                self.click_folder_more() # 点击更多
                self.sleep(1)
                self.delete_folder_name()
                self.sleep(1)
                self.sure_del_folder()
                new_num = self.get_folder_num()
                num = old_num - new_num
                assert num == 1
        except Exception as e:
            self.logger.error(msg+'%s' % repr(e))
            SendDingTalk().sendDingTalkMsg(msg)
            raise e

    # 点击上传模板
    def test_upload_pictemp(self,driver,msg):
        try:
            self.upload_temp()
            self.add_pic_file(psd)
            self.sleep(6)
            self.window(-1)
            try:
                self.jump_work()
            except:
                self.logger.info("跳过按钮没有出现")
            self.save_temp(driver) # 模板保存按钮
            temp_url = self.get_qiye_url()
            assert "designworkbench" in temp_url
            self.back()
        except Exception as e:
            self.logger.error(msg+'%s' % repr(e))
            SendDingTalk().sendDingTalkMsg(msg)
            raise e

    # 重命名模板
    def test_rename_pictemp(self,driver,msg):
        try:
            name = "企业模板新名称"
            if self.get_file_is_greater_zero(driver,msg) > 0:
                self.page_down(5000)
                page_num = self.get_page_num()
                if page_num > 1:
                    self.click_fanye()
                self.hover_temp()
                self.click_pic_temp_more()
                self.sleep(1)
                self.rename_temp()
                self.sleep(1)
                self.input_new_temp(name) # 请输入名称
                self.click_sure_rename_btn()
                temp_name = self.get_temp_name() # 获取模板名称
                assert str(temp_name).strip() == name
        except Exception as e:
            self.logger.error(msg+'%s' % repr(e))
            SendDingTalk().sendDingTalkMsg(msg)
            raise e
    # 移动模板
    def test_move_pictemp(self,driver,msg):
        try:
            if self.get_folder_is_true(msg) > 0 and self.get_file_is_greater_zero(driver,msg) > 0:
                page_num = self.get_page_num()
                if page_num > 1:
                    self.click_fanye()
                    self.sleep(2)
                pic_num = self.get_pictemp_num() # 翻页后重新获取图片个数
                self.sleep(1)
                self.hover_temp()
                self.click_pic_temp_more()
                self.sleep(1)
                self.move_temp() # 移动模板
                self.sleep(2)
                self.click_folder_tree() # 点击树结构
                self.select_folder() # 选择文件夹最后一个文件夹
                self.sure_move_btn() #点击确定按钮
                pic_num_new = self.get_pictemp_num()
                num = pic_num - pic_num_new
                assert num == 1
        except Exception as e:
            self.logger.error('企业--企业模板--移动模板失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业--企业模板--移动模板失败")
            raise e

    # 删除模板
    def test_delete_pictemp(self,driver,msg):
        try:
            pic_num = self.get_file_is_greater_zero(driver,msg)
            # 如果无模板
            if pic_num == 0:
                # 进入模板中心将模板设置为团队模板
                self.upload_temp()
                self.add_pic_file(psd)
                self.sleep(3)
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
                # 返回团队模板
                self.back_team_temp()
            if pic_num > 0:
                page_num = self.get_page_num()
                if page_num > 1:
                    self.click_fanye() # 翻页
                    self.sleep(2)

                pic_num = self.get_pictemp_num()
                self.page_down(5000)
                self.hover_temp()
                self.click_pic_temp_more()
                self.sleep(1)
                self.click_delete_btn()
                self.sleep(1)
                self.click_sure_delete_btn()
            pic_num_new = self.get_pictemp_num()
            num = pic_num - pic_num_new
            assert num == 1
        except Exception as e:
            self.logger.error(msg+'%s' % repr(e))
            SendDingTalk().sendDingTalkMsg(msg)
            raise e