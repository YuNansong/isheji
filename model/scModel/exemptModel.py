from pages.basePage import Action


class ExemptModel(Action):
    # 免抠元素列表查询结果
    def exempt_search_result(self):
        try:
            exempt_item_xpath = ('xpath', "//div[@id='coryright-exempt-list']/div")
            num = len(self.getElements(exempt_item_xpath))
        except:
            num = 0
        return num

    # 鼠标悬浮到第一个免抠元素
    def exempt_hover_first(self):
        exempt_item_xpath = ('xpath', "//div[@id='coryright-exempt-list']/div[1]")
        self.mouse_hover(exempt_item_xpath)

    # 点击收藏按钮
    def exempt_coll_first(self):
        exempt_yangtu_btn_xpath = (
        'xpath', "//div[@id='coryright-exempt-list']/div[1]//div[@class='image-item-shadowbox']//img")
        self.click(exempt_yangtu_btn_xpath)

    # 鼠标点击到第一个免抠元素
    def exempt_click_first(self):
        exempt_item_xpath = (
        'xpath', "//div[@id='coryright-exempt-list']/div[1]/img")
        self.click(exempt_item_xpath)

    # 定位免抠元素下载成功提示
    def exempt_get_tips_list(self):
        first_download = ('xpath', "//div[@class='el-message el-message--success']")
        again_download = ('xpath', "//p[@class='el-message__content']")
        tips_list = [first_download, again_download]
        return tips_list

    # 判断是否已收藏
    def exempt_is_coll(self, element):
        try:
            self.getElementAttr(element, "alt")  # alt 属性存在则代表未收藏
            alt = True  # 未收藏
        except:
            alt = False  # 已收藏
        return alt

    # 鼠标点击到第一个免抠元素
    def exempt_detail_get_name(self):
        try:
            exempt_name_xpath = ('xpath', "//div[@class='img-detail']//h1")
            exempt_name = self.getText(exempt_name_xpath)
        except:
            exempt_name = ""
        return exempt_name

    # 在免抠元素模版详情，点击“下载源文件”
    def exempt_detail_download_source_file(self):
        video_detail_source_file_btn_xpath = ('xpath', "//div[@class='type']/div")
        self.click(video_detail_source_file_btn_xpath)

    # 在免抠元素模版详情，点击“下载样图”
    def exempt_detail_download_yangtu(self):
        video_detail_yangtu_btn_xpath = ('xpath', "//div[@class='yangt']")
        self.click(video_detail_yangtu_btn_xpath)

    # 在免抠元素模版详情，点击“收藏按钮”
    def exempt_detail_coll(self):
        exempt_detail_coll_btn_xpath = ('xpath', "//div[@class='right']//span/img[@alt='']")
        self.click(exempt_detail_coll_btn_xpath)
