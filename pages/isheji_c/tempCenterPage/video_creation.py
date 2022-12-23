import random
from common.path import heng
from common.readLog import Log
from common.path import zip_file
from common.sendDingTalk import SendDingTalk
from common.op_windows import OpWindows
from pages.basePage import Action


class VideoCreation(Action):
    log = Log(__name__)
    logger = log.getLog()

    def into_my_video_create(self):
        '''进入我的视频创作'''
        try:
            vlog_click = ('xpath', "//li[@class='block-item myvideocreation']//span[@class='block-text']")
            self.click(vlog_click)
            self.sleep(2)
            fving = ('xpath', "//section[@class='create-a-design']/div[1]/h3[1]")  # 获取我的视频创作标题
            actual = self.getText(fving)
            expect = '我的视频创作'
            self.assert_text(expect, actual)
        except Exception as e:
            self.logger.info('没有进入我的视频创作列表%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("进入我的视频创作列表失败")
            raise e

    # 获取视频模版数据
    def temp_num(self):
        try:
            video_temp = ('xpath', "//ul[@class='reation-data']/li")
            num = len(self.getElements(video_temp))
        except:
            num = 0
        return num

    def get_status_num(self, i):
        try:
            video_temp = ('xpath', "//div[@class='search-item-content typelist']/span[" + str(i) + "]/a")
            text = self.getText(video_temp)
            num = int(text)
        except:
            num = 0
        return num

    # 进入草稿列表
    def draft_list(self):
        draft = ('xpath', "//div[@class='search-item-content typelist']/span[2]")
        self.click(draft)

    # 进入全部列表
    def all_list(self):
        try:
            self.page_down(10)
            self.sleep(1)
            all_list_xpath = ('xpath', "//div[@class='search-item-content typelist']/span[contains(text(),'全部')]")
            self.click(all_list_xpath)
            num = self.temp_num()
            self.logger.info("进入我的视频模板--全部列表模板数为%d" % num)
            assert num > 0
        except Exception as e:
            self.logger.error("进入我的视频模板--全部列表异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("进入我的视频模板--全部列表失败")
            raise e

    # 进入草稿列表
    def test_draft_list(self):
        try:
            self.page_down(0)
            self.sleep(1)
            self.draft_list()
            self.sleep(2)
            num = self.temp_num()
            self.logger.info("进入我的视频模板--草稿列表模板数为%d" % num)
            assert num > 0
        except Exception as e:
            self.logger.error("进入我的视频模板--草稿列表异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("进入我的视频模板--草稿列表失败")
            raise e

    # 进入审核中列表
    def approve_list(self):
        try:
            self.page_down(0)
            self.sleep(1)
            draft = ('xpath', "//div[@class='search-item-content typelist']/span[3]")
            self.ptclick(draft)
            num = self.temp_num()
            self.logger.info("进入我的视频模板--审核中列表模板数为%d" % num)
            assert num >= 0
        except Exception as e:
            self.logger.error("进入我的视频模板--审核中列表异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("进入我的视频模板--审核中列表失败")
            raise e

    # 进入审核成功列表
    def approve_succ_list(self):
        try:
            draft = ('xpath', "//div[@class='search-item-content typelist']/span[4]")
            self.ptclick(draft)
            num = self.temp_num()
            self.logger.info("进入我的视频模板--审核成功列表模板数为%d" % num)
            assert num >= 0
        except Exception as e:
            self.logger.error("进入我的视频模板--审核成功列表异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("进入我的视频模板--审核成功列表失败")
            raise e

    def new_vlog(self):
        '''点击上传模版'''
        input_button = ('xpath', "//section[@class='create-a-design']/div[1]/div[2]")
        self.click(input_button)
        self.sleep(1)

    def input_zip(self):
        '''上传zip文件'''
        input_buttpn = ('xpath', "//div[@id='container']/div/input")
        self.write(input_buttpn, zip_file)
        self.sleep(3)

    def input_cover_and_text(self):
        '''上传封面和文本输入'''
        id = random.randint(0, 1000)
        input_cover_button = ('xpath', "//input[@name='file']")
        self.write(input_cover_button, heng)
        title = ('xpath', "//form[@id='upload-video']/div[5]/input")  # 视频标题
        title_name = '自动化测试(请忽略)' + str(id)
        self.write(title, title_name)
        self.sleep(1)
        # 模版介绍
        temple_introduce = ('xpath', "//textarea[@id='template-introduction']")
        introduce = '模版介绍' + str(id)
        self.write(temple_introduce, introduce)
        self.sleep(1)
        # 关键词
        for i in range(1, 6):
            key_word = ('xpath', "//input[@placeholder='输入后回车确认']")
            word_key = f'风格{i}'
            self.write(key_word, word_key)
            self.sayok(key_word)
            self.sleep(1)
            # 横版字段
        row_word = ('xpath', "//div[8]//input[1]")
        input_row_word = '横版字段' + str(id)
        self.write(row_word, input_row_word)

    def select_button(self):
        '''下拉框以及单选框'''
        self.page_down()
        transfer = ('xpath', "//form[@id='upload-video']/div[9]/label")  # 用途字

        # 用途下拉框
        purpose = ('xpath', "//form[@id='upload-video']/div[9]/div[1]/div[1]")
        self.click(purpose)
        self.sleep(2)
        OpWindows.keybd_event(40)
        self.sleep(1)
        OpWindows.keybd_event(40)
        self.sleep(1)
        OpWindows.keybd_event(13)
        self.sleep(2)
        self.click(transfer)

        # 风格下拉框
        style_down_button = ('xpath', "//form[@id='upload-video']/div[10]/div[1]/div[1]")
        self.click(style_down_button)
        self.sleep(1)
        OpWindows.keybd_event(40)
        self.sleep(1)
        OpWindows.keybd_event(40)
        self.sleep(1)
        OpWindows.keybd_event(13)
        self.sleep(2)
        self.click(transfer)

        # 三种颜色
        # 第一个颜色 #data-hex="#ff7936"
        self.sleep(2)
        first_coloer = ('xpath', "//ul[@class='clors-ul']//li[1]//span[1]")
        self.click(first_coloer)
        self.sleep(2)
        select_color = ('xpath', "//*[@class='IroWheel']//*[@class='IroHandle IroHandle--0 IroHandle--isActive']")
        self.click(select_color)
        self.click(transfer)

        time_input = ('xpath', "//input[@placeholder='请输入视频时长，如00:15']")
        self.write(time_input, "00:15")

        up_button = ('xpath', "//div[@class='btns-box']/div[2]")
        self.click(up_button)
        self.sleep(10)

    # 新增视频模板
    def test_upload_video_temp(self):
        try:
            self.all_list()
            num = self.get_status_num(1)
            self.logger.info("获取目前存在的模板数：%d" % num)
            self.new_vlog()
            self.input_zip()
            self.input_cover_and_text()
            self.select_button()
            self.sleep(2)
            self.refresh()
            self.sleep(3)
            new_num = self.get_status_num(1)
            self.logger.info("新增后获取存在的模板数：%d" % new_num)
            result = new_num - num
            assert result == 1
        except Exception as e:
            self.logger.error("新增视频模板出现异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("新增视频模板出现失败")
            # 如果出现异常则新打开一个窗口
            js = "window.open()"
            self.executeJs(js, "")
            self.sleep(2)
            self.window(-1)
            self.transfer_url("/video/mycreation")

    # 编辑视频模板
    def test_edit_video_temp(self):
        try:
            self.page_down(0)
            self.draft_list()
            self.sleep(2)
            num = self.temp_num()
            get_status_num = self.get_status_num(2)
            self.logger.info("测试编辑视频，获取草稿列表的视频个数为%s" % get_status_num)
            if num > 1:
                # 查看其状态，如果是草稿则进行编辑
                for i in range(1, num):
                    video_status = ('xpath', "//ul[@class='reation-data']/li[" + str(i) + "]/div[last()-1]")
                    if self.getText(video_status) == "草稿":
                        edit_btn = ('xpath', "//ul[@class='reation-data']/li[" + str(i) + "]/div[last()]/div/button[1]")
                        self.ptclick(edit_btn)
                        self.page_down()  # 滑动浏览器到底部
                        # 在编辑页面点击立即投稿按钮
                        up_button = ('xpath', "//div[@class='btns-box']/div[2]")
                        self.click(up_button)
                        break
                    else:
                        self.logger.info("我的视频列表没有草稿状态的模板")
        except Exception as e:
            self.logger.error("在我的视频--草稿列表，编辑草稿状态的视频异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在我的视频--草稿列表，编辑草稿状态的视频失败")
            raise e

    # 删除视频模板
    def test_delete_video_temp(self):
        try:
            self.page_down(0)
            self.sleep(1)
            # 获取视频模版数据
            num = self.temp_num()
            get_status_num = self.get_status_num(2)
            self.logger.info("测试删除视频，获取草稿列表的视频个数为%d" % get_status_num)
            if num > 1:
                # 点击删除按钮
                self.page_down()
                edit_btn = ('xpath', "//ul[@class='reation-data']/li[last()]/div[last()]/div/button[3]")
                self.ptclick(edit_btn)
                # 处理确定弹框
                self.sleep(1)
                remove_true = ('xpath', "//button[@class='remove_true']")
                self.ptclick(remove_true)
                # 验证是否删除成功
                get_status_new_num = self.get_status_num(2)
                result = get_status_num - get_status_new_num
                assert result == 1
        except Exception as e:
            self.logger.error("在我的视频--草稿列表，删除视频异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在我的视频--草稿列表，删除视频失败")
            raise e
