import random
from pages.basePage import Action
from element.sc_copyright.sc_home_element import SCHomePageElement

# 公共方法

class CommModel(Action):

    # 点击右上角头像
    def click_head_img(self):
        head_img_xpath = ('xpath',"//div[@class='header-left']")
        self.click(head_img_xpath)

    # 点击个人头像
    def click_img(self):
        self.mouse_hover(SCHomePageElement.head_img)
        self.sleep(2)

    # 关闭VIP 弹框
    def close_vip(self):
        try:
            vip_closed_btn_xpath = ('xpath',"//div[@id='tanc']/span")
            self.click(vip_closed_btn_xpath)
            try:
                vip_closed_btn_xpath = ('xpath',"//div[@class='login-modal']/span")
                self.click(vip_closed_btn_xpath)
            except:
                self.logger.info("右侧VIP弹框未出现")
        except:
            try:
                vip_closed_btn_xpath = ('xpath',"//div[@class='login-modal']/span")
                self.click(vip_closed_btn_xpath)
            except:
                self.logger.info("右侧VIP弹框未出现")

    # 在导航点击图片
    def click_pic_menu(self):
        music_button = ('xpath', "//div[@id='header']//li//a[contains(text(),'图片')]") # 首页音乐
        self.click(music_button)
    # 在导航点击音乐
    def click_music_menu(self):
        music_button = ('xpath', "//div[@id='header']//li//a[contains(text(),'音乐')]") # 首页音乐
        self.click(music_button)

    # 在导航点击设计
    def click_design_menu(self):
        design_button = ('xpath', "//div[@id='header']//li//a[contains(text(),'设计')]") # 首页音乐
        self.click(design_button)

    # 在导航点击视频
    def click_video_menu(self):
        video_button = ('xpath', "//div[@id='header']//li//a[contains(text(),'视频')]") # 首页视频
        self.click(video_button)
        self.sleep(2)

    # 在导航点击免抠元素
    def click_exempt_menu(self):
        video_button = ('xpath', "//div[@id='header']//li//a[contains(text(),'免抠元素')]") # 首页免抠元素
        self.click(video_button)
        self.sleep(2)

    # 在导航点击PPT
    def click_ppt_menu(self):
        video_button = ('xpath', "//div[@id='header']//li//a[contains(text(),'PPT')]") # 首页免抠元素
        self.click(video_button)
        self.sleep(2)

    # 定位图片下载成功提示
    def design_get_tips_list(self):
        first_download = ('xpath', "//div[@class='el-message el-message--success']")
        again_download = ('xpath', "//p[@class='el-message__content']")
        tips_list = [first_download, again_download]
        return tips_list

    # 判断是否已收藏
    def design_is_coll_pic(self, element):
        try:
            self.getElementAttr(element, "alt") # alt 属性存在则代表未收藏
            alt = True # 未收藏
        except:
            alt = False # 已收藏
        return alt

    # 获取样图申请弹框
    def design_detail_get_apply(self):
        try:
            design_detail_apply_xpath = ('xpath',"//div[@class='downdemo-inner']/div[1]")
            title = self.getText(design_detail_apply_xpath)
        except:
            title = ""
        return title

    # 获取样图申请弹框
    def design_detail_close_apply(self):
        design_detail_close_btn_xpath = ('xpath',"//div[@class='banquan-close']")
        self.click(design_detail_close_btn_xpath)

    # 视频、音乐、图片详情页点击关键词
    def click_keyword(self):
        key_xpath = ('xpath',"//div[@class='keyword-box']/ul/li")
        key_num = len(self.getElements(key_xpath))
        if key_num > 0:
            num = random.randint(1,key_num)
            keyword_xpath = ('xpath',"//div[@class='keyword-box']/ul/li["+str(num)+"]")
            keyname = self.getText(keyword_xpath)
            self.click(keyword_xpath)
            return keyname

    # 在PPT、免抠元素详情情页点击关键词
    def other_click_keyword(self):
        key_xpath = ('xpath',"//div[@class='keyword']/ul/li")
        key_num = len(self.getElements(key_xpath))
        if key_num > 0:
            num = random.randint(1,key_num)
            keyword_xpath = ('xpath',"//div[@class='keyword']/ul/li["+str(num)+"]")
            keyname = self.getText(keyword_xpath)
            self.click(keyword_xpath)
            return keyname

    # 获取搜索框中的值
    def get_input_key(self):
        try:
            input_xpath = ('xpath',"//input[@type='text']")
            key = self.getElementAttr(input_xpath,"value")
        except:
            key = ""
        return key

    # 在图片/音乐/设计/视频详情页点击购买单张套餐
    def click_leaflet_meal(self):
        buy_meal_xpath = ('xpath',"//div[@class='topay-box dz-box']//span[@class='pay-btn']")
        self.click(buy_meal_xpath)