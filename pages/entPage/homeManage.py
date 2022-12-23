from common.sendDingTalk import SendDingTalk
from common.readLog import Log
from common.path import vcg
from common.getYaml import url
from model.entModel.entIndexModel import EntIndexModel

class HomepageManagement(EntIndexModel):
    '''我的企业：首页管理'''
    log = Log(__name__)
    logger = log.getLog()

    # 进入首页管理
    def test_act_ent_homemange(self):
        '''进入我的企业'''
        try:
            self.click_manage()
            self.click_ent_home()
            self.sleep(2)
            sign = ('xpath', "//span[@class='s-h-text']")
            actual = self.getText(sign)
            expect = '开启分发首页'
            self.assert_text(expect, actual)
        except Exception as e:
            self.logger.error('企业-首页管理-进入首页管理失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业-首页管理-进入首页管理失败")
            raise e

    def test_open_button(self):
        '''分发首页开关按钮'''
        openbutton = ('xpath', "//div[@role='switch']")
        attr = self.getElementAttr(openbutton,"class")
        if attr == "el-switch is-checked":
            aria_checked = self.getElementAttr(openbutton,"aria-checked")
            assert aria_checked == "true"
        elif attr == "el-switch":
            self.click(openbutton)
            self.sleep(1)
            attr = self.getElementAttr(openbutton,"class")
            assert attr == "el-switch is-checked"
        else:
            self.logger.info("开启首页分发功能异常")

    # 首页配置
    def test_page_manege(self):
        try:
            # 配置logo
            manege_button = ('xpath', "//div[@class='setting-home']/button[1]/span")
            self.click(manege_button)
            self.sleep(1)
            input_button = ('xpath', "//input[@name='file']")
            self.write(input_button, vcg)
            self.sleep()
            manage_button = ('xpath', "//div[@class='team-info']//span[contains(text(),'首页管理')]")
            self.click(manage_button)
        except Exception as e:
            self.logger.error('失败：我的企业：首页管理--首页配置失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：我的企业：首页管理--首页配置失败")
            raise e

    def textlcon(self):
        '''配置文字图标点击'''
        text = ('xpath', "//div[@class='icon-info']/div[1]/div[last()]/p")
        self.click(text)
        banner_name = self.getText(text)
        return banner_name

    # 获取模板个数
    def get_banner_num(self):
        muban_num_xpath = ('xpath',"//form/div/div[@class='banner-f-item']")
        muban_num = len(self.getElements(muban_num_xpath))
        print("muban_num:",muban_num)
        return muban_num
    # 配置过程删除
    def delete_banner(self):
        # 删除最后一个
        last_text_banner_xpath = ('xpath',"//form/div/div[@class='banner-f-item'][last()]//button[@type='button']/span[contains(text(),'删除')]")
        self.click(last_text_banner_xpath)
        self.sleep(1)
        # 点击确定按钮
        delete_btn_xpath = ('xpath',"//div[@aria-label='提示']//button[2]")
        self.click(delete_btn_xpath)

    # 点击添加图文导航
    def add_pictrue_nav(self):
        pictrue_nav = ('xpath', "//form[@class='el-form']//button/span[contains(text(),'添加')]")
        self.click(pictrue_nav)

    def add_temp_nav(self):
        pictrue_nav = ('xpath', "//form[@class='el-form']//button/span[contains(text(),'添加模板')]")
        self.click(pictrue_nav)

    # # 处理滚动条
    # def click_scroll_bar(self):
    #     pictrue_nav = ('xpath', "//form[@class='el-form']//button/span[contains(text(),'添加')]")
    #     self.custom_scroll_bar(pictrue_nav) # 处理滚动条
    #     self.sleep(2)

    # 处理滚动条
    def click_muban_scroll_bar(self):
        self.sleep(1)
        pictrue_nav = ('xpath', "//form/div/div[@class='banner-f-item'][last()]//button[1]/span[contains(text(),'删除')]")
        self.custom_scroll_bar(pictrue_nav) # 处理滚动条
        self.sleep(2)
    # 配置文字导航
    def test_aborted_input(self):
        try:
            # manage_button = ('xpath', "//div[@class='team-info']//span[contains(text(),'首页管理')]")
            # self.click(manage_button)
            name = ""
            self.textlcon()  # 配置文字图标点击
            self.sleep(1)
            text_num = self.get_banner_num()
            if text_num >= 6:
                self.click_muban_scroll_bar()
                self.delete_banner()

            text_num = self.get_banner_num()
            if text_num < 6:
                self.sleep(1)
                self.click_muban_scroll_bar()
                self.add_pictrue_nav()
                input_button = ('xpath', "//form/div/div[@class='banner-f-item'][last()]//div[@class='el-upload el-upload--text']/input")
                self.write(input_button, vcg)
                self.sleep()
                # 输入名称
                #self.click_scroll_bar()
                last_text_banner_text = ('xpath',"//form/div/div[@class='banner-f-item'][last()]//p[@class='edit-title']/span")
                self.click(last_text_banner_text)
                self.sleep(2)
                # last_text_banner_input = ('xpath',"//form/div/div[@class='banner-f-item'][last()]//p[@class='edit-title']//input")
                # # etree.HTML(last_text_banner_input.ge)
                # self.clear(last_text_banner_input)
                # name = "新导航"+str(random.randint(0,100))
                # self.write(last_text_banner_input,name)
                # 设置链接
                link_xpath = ('xpath',"//form/div/div[@class='banner-f-item'][last()]//p[3]/span")
                self.click(link_xpath)
                self.sleep(1)
                folder_xpath = ('xpath',"//div[@id='pane-folder']//div[@class='el-scrollbar__view']/div/ul/li[1]")
                self.click(folder_xpath)
                # 点击确定按钮
                sure_button_xpath = ('xpath',"//div[@class='home-content content']/div[3]//button[@class='el-button el-button--primary']")
                self.click(sure_button_xpath)
            banner_name = self.textlcon() # 操作完点击 文字导航
            # 断言
            # assert banner_name == name
        except Exception as e:
            self.logger.error('企业-首页管理--配置文字导航失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业-首页管理--配置文字导航失败")
            raise e

    # def delete_correctly(self):
    #     '''删除上传的图片'''
    #     try:
    #         # manage_button = ('xpath', "//div[@class='team-info']//span[contains(text(),'首页管理')]")
    #         # self.click(manage_button)
    #         self.textlcon()
    #         input_button = ('xpath', "//input[@name='file']")
    #         self.write(input_button, png)
    #         self.sleep(2)
    #         delete_button = ('xpath', "//button[@class='el-button r del el-button--text']/span")
    #         self.click(delete_button)  # 删除按钮
    #         self.sleep(1)
    #         enter_button = ('xpath', "//div[@class='el-message-box__btns']/button[2]")
    #         self.click(enter_button)  # 确定删除
    #     except Exception as e:
    #         self.logger.error('失败：我的企业：首页管理--删除上传的图片%s' % repr(e))
    #         SendDingTalk().sendDingTalkMsg("失败：我的企业：首页管理--删除上传的图片")
    #         raise e

    # 点击某个分类进行配置
    def click_muban_class(self):
        class_title_xpath = ('xpath', "//div[@class='template home-border']/div[last()-1]/div[@class='temp-title']/h2")
        class_name = self.getText(class_title_xpath)
        self.click(class_title_xpath)
        return class_name

     # 分类
    def test_classification(self):
        name = ""
        try:
            self.page_down(3000)
            self.click_muban_class()
            # 获取模版个数
            muban_num = self.get_banner_num()
            if muban_num >= 10:
                self.click_muban_scroll_bar()
                self.delete_banner()

            # 获取模版个数
            muban_num = self.get_banner_num()
            if muban_num < 10:
                if muban_num < 5:
                    self.add_temp_nav() # 添加图文导航
                if muban_num >=5:
                    self.click_muban_scroll_bar()
                    self.add_temp_nav() # 添加图文导航
                # # # 输入分类名称
                # # name = "节日"+str(random.randint(1,100))
                # name = "节日"
                # class_name_xpath = ('xpath',"//form/div/div[@class='banner-f-item'][last()]//div[@class='b-c-left']/p/span")
                # self.click(class_name_xpath)
                # self.sleep(1)
                # class_name_xpath2 = ('xpath',"//form/div/div[@class='banner-f-item'][last()]//div[@class='b-c-left']/p/*")
                # # a = self.getElements(class_name_xpath2)
                # # print("a",a)
                # self.clear(class_name_xpath2)
                # self.sleep(1)
                # self.write(class_name_xpath,name)

                # 添加模板
                add_button = ('xpath', "//form/div/div[@class='banner-f-item'][last()]//button[2]/span")
                self.click(add_button)
                self.sleep(2)
                # 验证模板是否被选中
                try:
                    first_picture = ('xpath', "//div[@class='el-scrollbar__view']/ul/li[1]//div[@class='active-box']")
                    self.click(first_picture)
                    self.sleep(1)
                    self.click(first_picture)
                    enter_button = ('xpath', "//button[@class='el-button confirm-btn el-button--primary']//span")
                    self.click(enter_button)
                except:
                    first_picture = ('xpath', "//div[@class='el-scrollbar__view']/ul/li[@class='image-li'][1]")
                    self.click(first_picture)
                    # 点击确定按钮
                    enter_button = ('xpath', "//button[@class='el-button confirm-btn el-button--primary']//span")
                    self.click(enter_button)
            # 断言：
            # 获取名称
            manage_button = ('xpath', "//div[@class='team-info']//span[contains(text(),'首页管理')]")
            self.click(manage_button)
            # assert class_name == name
        except Exception as e:
            self.logger.error('失败：我的企业：首页管理--分类%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：我的企业：首页管理--分类")
            raise e

    # 发布
    def test_send_home(self):
        try:
            urlInfo = url['url']['testUrl']
            send_button = ('xpath',"//div[@class='setting-home']/button[2]/span")
            self.click(send_button)
            qiye_url = self.get_qiye_url()
            assert qiye_url == urlInfo+"/home"
        except Exception as e:
            self.logger.error('企业-首页管理-发布失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业-首页管理-发布失败")
            raise e