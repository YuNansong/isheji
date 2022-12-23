from common.path import vcg
from common.sendDingTalk import SendDingTalk
from common.readLog import Log
from model.entModel.entBrandModel import EntBrandModel

'''我的企业：品牌管理'''
class My_Brand(EntBrandModel):

    log = Log(__name__)
    logger = log.getLog()

    def m_environment(self):
        try:
            gaoji = ('xpath', "//button[@id='details-button']")
            self.click(gaoji)
            unsafe = ('xpath', "//a[@id='proceed-link']")
            self.click(unsafe)
        except Exception as e:
            self.sleep()
            self.logger.error('我的企业：没有出现：风险提示%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("我的企业：没有出现：风险提示")
            raise e

    def enterprise(self):
        '''进入我的企业'''
        enter = ('xpath', "//a[@id='toggle_team']")
        self.click(enter)
        self.window(-1)

    # 进入品牌管理
    def test_act_brand(self):
        try:
            self.click_manage() # 点击管理
            self.sleep(1)
            self.click_brand_manage() # 点击品牌管理
            # 断言
            self.sleep(3)
            text = self.get_brand_manage_text()
            assert "品牌管理" in text
        except Exception as e:
            self.logger.error('进入我的企业--品牌管理异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("进入我的企业--品牌管理失败")
            raise e

    # 品牌管理上传LOGO
    def test_brand_upload_logo(self):
        try:
            # 通过验证logo 个数进行判断是否上传成功
            logo_num = self.get_logo_num()
            self.input_logo(vcg)
            self.sleep(2)
            logo_num_new = self.get_logo_num()
            num = int(logo_num_new) - int(logo_num)
            assert num == 1
        except Exception as e:
            self.logger.error('失败：我的企业：品牌管理--上传logo失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：我的企业：品牌管理--上传logo失败")
            raise e

    # 品牌管理删除LOGO
    def test_brand_delete_logo(self):
        try:
            logo_num = self.get_logo_num()
            if logo_num < 1:
                self.input_logo(vcg)

            logo_num = self.get_logo_num()
            if logo_num >=1:
                self.last_logo() # 定位到最后一个logo上
                self.last_logo_more() # 点击logo 更多按钮
                self.sleep(1)
                self.last_logo_del() # 删除logo
                self.sleep(1)
                self.sure_del_logo() # 确定删除logo
                self.sleep(2)
                logo_num_new = self.get_logo_num()
                num = logo_num - logo_num_new
                assert num == 1
            else:
                SendDingTalk().sendDingTalkMsg("无法在品牌管理删除logo，logo个数为0")
        except Exception as e:
            self.logger.error('失败：我的企业：品牌管理--删除logo失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：我的企业：品牌管理--删除logo失败")
            raise e

    # 品牌管理重命名logo
    def test_brand_rename_logo(self):
        try:
            logo_num = self.get_logo_num()
            if logo_num < 1:
                self.input_logo(vcg)

            if logo_num >=1:
                # 获取名称
                self.last_logo() # 定位到最后一个logo上
                self.last_logo_more() # 点击logo 更多按钮
                self.sleep(1)
                self.last_logo_rename()
                self.sleep(2)
                self.clear_logo_name()
                self.sleep(1)
                self.input_logo_name("新logo") # 换个名称
                self.sure_rename_logo()
                name = self.get_last_logo_name()
                assert name == "新logo"
            else:
                SendDingTalk().sendDingTalkMsg("无法在品牌管理修改logo名称，logo个数为0")
        except Exception as e:
            self.logger.error('企业-品牌管理--重命名logo失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业-品牌管理--重命名logo失败")
            raise e
    # 品牌管理下载logo
    def test_brand_download_logo(self):
        try:
            logo_num = self.get_logo_num()
            if logo_num < 1:
                self.input_logo(vcg)
            if logo_num >=1:
                # 获取名称
                self.last_logo() # 定位到最后一个logo上
                self.last_logo_more() # 点击logo 更多按钮
                self.sleep(1)
                self.download_logo() # 下载logo
            else:
                SendDingTalk().sendDingTalkMsg("无法在品牌管理下载logo，logo个数为0")
        except Exception as e:
            self.logger.error('企业-品牌管理--下载logo失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业-品牌管理--下载logo失败")
            raise e

    # 增加品牌颜色
    def test_brand_add_coloer(self):
        try:
            color_num = self.get_color_num()
            self.click_add_color()
            self.sleep(1)
            self.input_colors()
            self.sleep(1)
            self.commit_color()
            color_num_new = self.get_color_num()
            num = color_num_new - color_num
            assert num == 1
        except Exception as e:
            self.logger.error('企业-品牌管理--添加品牌颜色异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业-品牌管理--添加品牌颜色失败")
            raise e

    # 获取品牌颜色名称
    def test_get_color_name(self):
        try:
            color_num = self.get_color_num()
            if color_num >= 1:
                name = self.get_color_name()
                self.logger.info("color name:%s"%name)
                assert  name != None
        except Exception as e:
            self.logger.error('企业-品牌管理--获取品牌颜色名称异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业-品牌管理--获取品牌颜色名称失败")
            raise e

    # 删除品牌颜色
    def test_delete_coloer(self):
        try:
            color_num = self.get_color_num()
            if color_num < 1:
                self.click_add_color()
                self.input_colors()
            color_num = self.get_color_num()
            self.logger.info("获取到颜色数:%d"%color_num)
            if color_num >= 1:
                self.click_color_more()  # 图片更多
                self.click_color_del_button() # 删除
                self.sleep(1)
                self.commit_del_color_button() # 弹框的确定按钮
                color_num_new = self.get_color_num()
                num = color_num - color_num_new
                assert num == 1
        except Exception as e:
            self.logger.error('企业-品牌管理--删除品牌颜色失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业-品牌管理--删除品牌颜色失败")
            raise e


    #增加字体
    def test_add_font(self):
        try:
            flag = True
            font_num = self.get_font_num()
            self.click_upload_font() # 点击添加字体按钮
            while flag == True:
                self.select_font() # 选择字体
                self.sure_font_btn()
                tips = self.get_error_tips()
                if str(tips).strip() == "上传失败，当前字体已存在" or str(tips).strip() == None:
                    flag = True
                else:
                    flag = False
                    break
            font_num_new = self.get_font_num()
            num = font_num_new - font_num
            assert num == 1
        except Exception as e:
            self.logger.error('失败：我的企业：品牌管理--增加字体%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：我的企业：品牌管理--增加字体")
            raise e
    # 增加重复字体
    def test_add_typeface_repeat(self):
        try:
            tips = ""
            flag = True
            while flag == True:
                self.click_upload_font()
                self.sleep(1)
                self.select_first_font()
                self.sleep(1)
                self.sure_font_btn()
                tips = self.get_error_tips()
                if str(tips).strip() == "上传失败，当前字体已存在":
                    flag = False
                    self.cancel_select_font_btn()
                    break
                else:
                    flag = True
            print("tips",tips)
            assert str(tips).strip() == "上传失败，当前字体已存在"
        except Exception as e:
            self.logger.error('失败：我的企业：品牌管理--增加重复字体%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：我的企业：品牌管理--增加重复字体")
            raise e
    # 修改字体
    def test_modiy_font(self):
        font_num = self.get_font_num()
        if font_num < 1:
            # 新选一个
            self.test_add_font()

        font_num = self.get_font_num()
        if font_num >= 1:
            flag = True
            font_name = self.get_font_name()
            self.click_font_more()
            self.click_modfiy_font_button()

            while flag == True:
                self.select_font() # 选择字体
                self.sure_font_btn()
                tips = self.get_error_tips()
                if str(tips).strip() == "上传失败，当前字体已存在" or str(tips).strip() == None:
                    flag = True
                else:
                    self.sure_modiy_font()
                    flag = False
                    break

            self.sleep(1)
            # 获取字体名称
            new_font_name = self.get_font_name()
            assert new_font_name != font_name
            self.logger.info("新获取到的字体名称：%s"%new_font_name)

    #删除字体
    def test_delete_font(self):
        try:
            font_num = self.get_font_num()
            if font_num < 4: # 字体 1，2 不允许删除
                # 新选一个
                self.test_add_font()

            font_num = self.get_font_num()
            if font_num >=1:
                self.click_font_more()
                self.click_del_font_button()
                self.sleep(1)
                self.click_sure_del_button()
                self.sleep(1)
                tips = self.get_success_tips()
                assert str(tips).strip() == "删除成功"
                font_num_new = self.get_font_num()
                num = font_num - font_num_new
                assert  num == 1
        except Exception as e:
            self.logger.error('失败：我的企业：品牌管理--删除字体%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：我的企业：品牌管理--删除字体")
            raise e