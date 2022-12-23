from common.path import jepg
from common.readLog import Log
from common.sendDingTalk import SendDingTalk
from model.entModel.entIndexModel import EntIndexModel
from model.entModel.entMaterialModel import EntMaterialModel
from model.entModel.entTempModel import EntTempModel
from pages.entPage.ent_commont import EntCommont

class EnterpirseMaterial(EntIndexModel,EntMaterialModel,EntTempModel):
    '''我的企业：企业空间'''
    log = Log(__name__)
    logger = log.getLog()

    # 进入企业素材'''
    def test_ent_marterial(self):
        self.click_manage()
        self.click_ent_sucai()

    # 点击右侧导航--企业素材
    def test_right_menu_sucai(self):
        try:
           self.right_menu_sucai()
        except Exception as e:
            self.logger.error('企业-进入企业素材失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业-进入企业素材失败")
            raise e

    # 新建文件夹功能
    def test_add_folder(self, driver):
        msg = "企业-企业素材-添加文件夹失败"
        EntCommont(driver).test_add_folder(msg)

    # 重命名文件夹功能
    def test_rename_folder(self, driver):
        msg = "企业-企业素材-重命名文件夹失败"
        EntCommont(driver).test_rename_folder(msg)

    # 删除文件夹功能
    def test_delete_folder(self, driver):
        msg = "企业-企业素材-删除文件夹失败"
        EntCommont(driver).test_delete_folder(msg)

    # 上传素材'''
    def test_upload_sucai(self):
        msg = "企业素材--上传素材失败"
        try:
            self.upload_material() # 上传素材按钮
            self.add_pic_file(jepg) # 选择jpeg 文件
            self.sleep()
            self.sure_add_pic_file() # 确定上传
            self.sleep(2)
        except Exception as e:
            self.logger.error(msg+'%s' % repr(e))
            SendDingTalk().sendDingTalkMsg(msg)
            raise e

    # 判断当前页面文件是否大于0
    def get_file_is_true(self,msg):
        pic_num = self.get_pictemp_num() # 获取素材个数
        if pic_num < 0:
            self.test_upload_sucai()
        pic_num = self.get_pictemp_num() # 获取素材个数
        if pic_num > 0:
            return pic_num
        else:
            return  0

    # 重命名文件
    def test_rename_pic(self):
        msg = "企业-企业素材-重命名图片失败"
        name = "企业素材新名称"
        try:
            pic_num = self.get_pictemp_num() # 获取素材个数
            if pic_num < 0:
                self.test_upload_sucai()
            pic_num = self.get_pictemp_num() # 获取素材个数
            if pic_num > 0:
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
    # 企业-企业素材-移动图片
    def test_move_pic(self,driver):
        msg = "企业-企业素材-移动图片失败"
        try:
            folderIsTrue = EntCommont(driver).get_folder_is_true(msg)
            fileIsTrue = self.get_file_is_true(msg)
            if folderIsTrue > 0 and fileIsTrue > 0:
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
            self.logger.error(msg+'%s' % repr(e))
            SendDingTalk().sendDingTalkMsg(msg)
            raise e

    # 企业-企业素材-删除图片
    def test_delete_pic(self,driver):
        msg = "企业-企业模板-删除图片失败"
        try:
            folderIsTrue = EntCommont(driver).get_folder_is_true(msg)
            fileIsTrue = self.get_file_is_true(msg)
            if folderIsTrue > 0 and fileIsTrue > 0:
                page_num = self.get_page_num()
                if page_num > 1:
                    self.click_fanye()
                    self.sleep(2)
                pic_num = self.get_pictemp_num() # 翻页后重新获取图片个数
                self.sleep(1)
                self.hover_temp()
                self.click_pic_temp_more()
                self.sleep(1)
                flag = self.click_delete_btn()
                i = 1
                while flag == False and i < 3:
                    self.refresh()
                    if page_num > 1:
                        self.click_fanye()
                        self.sleep(2)
                    self.hover_temp(i)
                    self.click_pic_temp_more(i)
                    flag = self.click_delete_btn()
                    if flag == True:
                        break

                self.sleep(1)
                self.click_sure_delete_btn()
                pic_num_new = self.get_pictemp_num()
                num = pic_num - pic_num_new
                assert num == 1
        except Exception as e:
            self.logger.error(msg+'%s' % repr(e))
            SendDingTalk().sendDingTalkMsg(msg)
            raise e

    # 下载文件

