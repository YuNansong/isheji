from common.sendDingTalk import SendDingTalk
from model.entModel.entIndexModel import EntIndexModel
from common.readLog import Log
import time


class MyDesign(EntIndexModel):
    log = Log(__name__)
    logger = log.getLog()

    def test_act_my_design(self):
        self.click_manage()
        self.click_ent_mydesign()

    def my_design(self):
        '''我的设计'''
        mysj = ('xpath', "//li[@class='block-item mydesign']")
        self.click(mysj)
        self.sleep()

    def my_design_text(self):
        '''断言：是否进入我的设计'''
        design_ass = ('xpath', "//div[@id='tab-list']")
        text = self.getText(design_ass)
        return text

    def test_clickMyDesign(self):
        self.logger.info("进入到我的设计页面")
        self.my_design()
        text = self.my_design_text()
        assert text == "图片设计"

    # 在我的设计页面点击图片模板
    def picture_template(self):
        try:
            self.logger.info("进入到我的设计页面，点击图片模板")
            picture_template = ('xpath', "//span[@formid='1']")
            self.click(picture_template)
            self.sleep(2)
            shoutuElement = ('xpath', "//div[@class='search-item type-list']/div[2]/span[2]")
            text = self.getText(shoutuElement)
            assert text == "公众号首图"
        except Exception as e:
            self.logger.error('在我的设计页面点击图片模板--未找到元素，或未进入页面%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("在我的设计页面点击图片模板--未找到元素，或未进入页面")
            raise e

    def video_template(self):
        self.logger.info("进入到我的设计页面，点击视频模板")
        video_template = ('xpath', "//span[@formid='2']")
        self.click(video_template)
        self.sleep(2)
        try:
            jiaoyuElement = ('xpath', "//div[@class='search-item videotype-list']/div[2]/span[2]")
            text = self.getText(jiaoyuElement)
            assert text == "教育培训"
        except Exception as e:
            self.logger('我的设计：在我的设计页面点击视频模板--未找到元素，或未进入页面%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("我的设计：在我的设计页面点击视频模板--未找到元素，或未进入页面")
            raise e

    def picture_template_see(self):
        '''点击模版进入工作台'''
        self.logger.info("进入到我的设计页面在图片模板下点击某个模板")
        modo_1 = ('xpath', "//ul[@class='clearFix designdatas designList']/li[1]/div[1]")
        self.click(modo_1)  # 点击第一个模板进入工作台
        self.sleep(3)
        self.window(-1)
        try:
            self.jump_work()
        except:
            self.logger.info("工作台跳过按钮没有出现")
        try:
            self.preservation()  # 点击保存按钮
            self.sleep(1)
            self.close_handle()
        except Exception as e:
            self.logger.error('我的设计：在我的设计页面点击图片模板进入工作台--保存按钮点击失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("我的设计：在我的设计页面点击图片模板进入工作台--保存按钮点击失败")
            raise e

    def test_delete_my_design(self):
        '''我的设计删除模版'''
        self.logger.info("进入到我的设计页面在图片模板下删除某个模板")
        try:
            first_design_xpath = ('xpath', "//div[@class='mydeisgn-datalist']/ul[1]/li[1]/div[1]")
            self.mouse_hover(first_design_xpath)
            self.sleep(1)
            delete_button = ('xpath', "//main[@id='app']//li[1]//div[1]//div[1]//span[1]")
            self.click(delete_button)
            self.sleep(1)
            en_ido = ('xpath', "//div[@class='el-message-box__btns']/button[2]")
            self.click(en_ido)
            self.sleep(1)
            self.logger.info('我的设计删除模版完成')
            self.home_button()
            self.sleep()
        except Exception as e:
            self.logger.error('我的设计删除模版异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("我的设计删除模版异常")
            raise e

    def test_my_collection(self):
        '''我的收藏'''
        self.logger.info("进入到我的收藏页面")
        col = ('xpath', "//span[contains(text(),'我的收藏')]")
        self.click(col)
        self.sleep()
        try:
            element_path = ('xpath', "//h3[@class='create-item-title']")
            actual = self.getText(element_path)
            self.assert_text("我的收藏", actual)
        except Exception as e:
            self.logger.error('未进入我的收藏%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("未进入我的收藏")
            raise e

    def collection_picture_template(self):
        '''图片模版'''
        self.logger.info("进入到我的收藏页面点击图片模板")
        picture_template = ('xpath', "//span[@formid='1']")
        self.click(picture_template)
        self.sleep()

    def cancel_collection_action(self):
        '''取消收藏'''
        try:
            self.logger.info("进入到我的收藏页面点击图片模板--取消某个模板")
            piceche = ("xpath", "//div[@class='mydeisgn-datalist']/ul[1]/li[1]/div[1]")
            self.mouse_hover(piceche)
            # piceche = "//div[@class='mydeisgn-datalist']/ul[1]/li[1]/div[1]"
            # self.move_to_stay(piceche)
            self.sleep(2)
            love_button = ('xpath', "//ul[@class='clearFix designdatas']/li[1]/div[1]/div[2]/span")  # 点击取消收藏按钮
            self.click(love_button)
            self.sleep()
            sureBtn = ('xpath', "//div[@class='el-message-box__btns']/button[2]")
            self.click(sureBtn)
            self.sleep()
            self.home_button()
        except Exception as e:
            self.logger.error('失败：我的设计图片模版：取消收藏失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：我的设计图片模版：取消收藏失败")
            raise e

    def create_folder(self):  # <<<
        """创建文件夹"""
        try:
            new_file_button = ("xpath", "//i[@class='el-icon-plus']")
            self.click(new_file_button)
            make_new_file_button = ("xpath", "//div[@class='create']/div[2]/i")
            self.click(make_new_file_button)
            file_name = "文件夹1"
            input_name = ("xpath", "//div[@class='el-dialog__body']//input[@class='el-input__inner']")
            self.write(input_name, file_name)
            enter_button = (
            "xpath", "//div[@class='el-dialog dialog-create']//button[@class='el-button el-button--primary']//span")
            self.click(enter_button)
        except Exception as e:
            self.logger.error('失败：创建文件夹%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：创建文件夹")
            raise e

    def del_folder(self):  # <<<
        """删除文件夹"""
        try:
            last_file = ("xpath",
                         "//body/div[@id='app']/div[@name='content']/div[@class='folderList']/div[@class='el-row']/div[last()]")
            more_button = ("xpath", "//div[@class='folderList']/div[@class='el-row']/div[last()]/div/span/button")
            self.mouse_hover(last_file)
            self.click(more_button)
            # 获取最后一个文件的更多按钮的ID
            # id_path = self.getElementAttr(more_button, "aria-describedby")
            # delt_button = ("xpath", f"//div[@id='{id_path}']/div/div[last()]/i")
            delt_button = ("xpath", "//body/div[@class='el-popover el-popper pop-more']/div[@class='option']/div[2]/div[1]")
            self.click(delt_button)
            enter_button_del = ("xpath", "//div[@id='app']//div[3]//div[1]//button[2]")
            self.click(enter_button_del)
        except Exception as e:
            self.logger.error('失败：删除文件夹%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：删除文件夹")
            raise e

    def del_more_folder(self):
        """删除多余文件夹"""
        try:
            all_file = ('xpath', "//div[@class='folderList']//div[@class='el-row']/div")
            file_num = self.getElements(all_file)
            print(len(file_num), "len(file_num)")

            if len(file_num) == 0:
                self.create_folder()
                file_name = ("xpath", "//div[@class='folderList']/div[@class='el-row']/div[1]/div[1]/div[2]")
                file_name_t = self.getText(file_name)
                file_name_text = file_name_t.strip()
                assert file_name_text == "文件夹1"
            else:
                print(len(file_num))
                for i in range(1, len(file_num)):
                    self.del_folder()
        except Exception as e:
            self.logger.error('失败：删除多余文件夹并创建新文件夹%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：删除多余文件夹并创建新文件夹")
            raise e

    def first_file_operation(self):  # ##
        """第一个模板的选中"""
        first_file = ("xpath", "//div[@class='el-row']//div[1]//div[1]//div[1]//div[1]//div[1]//img[1]")
        self.mouse_hover(first_file)
        more_button = (
        "xpath", "//div[@class='el-row']//div[1]//div[1]//div[1]//div[1]//div[1]//span[1]//button[1]//i[1]")
        self.click(more_button)

    def Create_copy(self):
        """创建副本"""
        try:
            self.first_file_operation()
            create_copy = ("xpath", "//body/div[@class='el-popover el-popper pop-more']/div[@class='option']/div[1]/div[1]")
            self.click(create_copy)
            input_path = ("xpath", "//input[@placeholder='请输入创建的副本的名称']")

            time_tuple = time.localtime(time.time())
            filename = "更改名称时间为{}点{}分{}秒".format(time_tuple[3],time_tuple[4],time_tuple[5])
            self.write(input_path, filename)
            enter_button = ("xpath", "//*[@id='app']/div[7]/div/div[3]/div/button[2]/span")
            self.click(enter_button)
            tips = ("xpath", "//p[@class='el-message__content']")
            tips_mation = self.getText(tips)
            assert tips_mation == "保存成功"
            return filename
        except Exception as e:
            self.logger.error('失败：创建副本%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：创建副本")
            raise e

    def get_first_modo_name(self):  # ##
        """获取第一个模板的名称"""
        self.Create_copy()
        first_name = ("xpath", "//body/div[@class='container']/div[@name='content']/div[@class='list']/div[@class='el-row']/div[1]/div[1]/div[1]/div[1]/div[2]")
        pass_name = self.getText(first_name)
        real_name = pass_name.strip()
        return real_name
    def move_to_file(self):
        """移动到文件夹"""
        try:
            self.first_file_operation()
            move_button = ("xpath", "//body/div[@class='el-popover el-popper pop-more']/div[@class='option']/div[2]")
            self.click(move_button)
            select_button = ("xpath", "//div[@class='el-dialog__body']//input[@placeholder='请选择']")
            self.click(select_button)
            select_file = ("xpath", "//div[@class='el-select-dropdown el-popper']//li[@class='el-select-dropdown__item']")
            self.click(select_file)
            select_enter_button = ("xpath", "//div[@class='el-dialog dialog-move']//div[3]//div[1]//button[2]")
            self.click(select_enter_button)
            tip = ("xpath", "//p[@class='el-message__content']")
            tips = self.getText(tip)
            assert tips == "操作成功"
        except Exception as e:
            self.logger.error('失败：移动模板到文件夹%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：移动模板到文件夹")
            raise e

    def verification_move(self):  # ##
        """验证文件移动到文件夹"""
        file_path = ("xpath", "//div[@class='folder-item']//img")
        self.click(file_path)
        infile_name = ("xpath", "//div[@class='temp-text']")
        text_name = self.getText(infile_name)
        return text_name

    def assert_out_in_name(self):
        """执行移入和验证"""
        out_name = self.get_first_modo_name()
        self.move_to_file()
        into_name = self.verification_move()
        assert out_name == into_name

    def file_dosome_thing(self):  # ##
        """调出模板的更多"""
        first_mode = ("xpath",
                      "//body/div[@id='app']/div[@name='content']/div[@class='folder-list list']/div[@class='el-row']/div[1]")
        self.mouse_hover(first_mode)
        threee_tip = (
        "xpath", "//div[@class='el-row']//div[1]//div[1]//div[1]//div[1]//div[1]//span[1]//button[1]//i[1]")
        self.click(threee_tip)

    def change_name(self):  # ##
        """重命名副本"""
        self.file_dosome_thing()
        changename = ("xpath", "//div[@class='el-popover el-popper pop-more']//div[3]")
        self.click(changename)
        pass

    def del_mode(self):  # ##
        """验证删除"""
        mode_name = ("xpath", "//div[@class='temp-text']")
        mode_name_text = self.getText(mode_name)
        first_mode = ("xpath", "//body/div[@id='app']/div[@name='content']/div[@class='folder-list list']/div[@class='el-row']/div[1]")
        self.mouse_hover(first_mode)
        threee_tip = ("xpath", "//div[@class='el-row']//div[1]//div[1]//div[1]//div[1]//div[1]//span[1]//button[1]//i[1]")
        self.click(threee_tip)
        del_button = ("xpath", "//div[@class='el-popover el-popper pop-more']//div[4]//div[1]")
        self.click(del_button)
        del_enter = ("xpath", "//div[@class='el-dialog dialog-delete-folder']//div[3]//div[1]//button[2]//span[1]")
        self.click(del_enter)
        recycle_bin = ("xpath", "//div[@id='tab-recycle']")
        self.click(recycle_bin)
        pass