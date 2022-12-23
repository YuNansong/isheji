from pages.basePage import Action


class PPTModel(Action):
    # 免抠元素列表查询结果
    def ppt_search_result(self):
        try:
            ppt_item_xpath = ('xpath', "//div[@class='search-item']/div")
            num = len(self.getElements(ppt_item_xpath))
        except:
            num = 0
        return num

    # 鼠标悬浮到第一个免抠元素
    def ppt_hover_first(self):
        ppt_item_xpath = ('xpath', "//div[@class='search-item']/div[1]")
        self.mouse_hover(ppt_item_xpath)

    # 点击收藏按钮
    def ppt_coll_first(self):
        ppt_yangtu_btn_xpath = ('xpath', "//div[@class='search-item']/div[1]//div[@class='image-item-shadowbox']//img")
        self.click(ppt_yangtu_btn_xpath)

    # 鼠标点击到第一个免抠元素
    def ppt_click_first(self):
        ppt_item_xpath = ('xpath', "//div[@class='search-item']/div[1]/div[1]/img")
        self.click(ppt_item_xpath)

    # 定位免抠元素下载成功提示
    def ppt_get_tips_list(self):
        first_download = ('xpath', "//div[@class='el-message el-message--success']")
        again_download = ('xpath', "//p[@class='el-message__content']")
        tips_list = [first_download, again_download]
        return tips_list

    # 判断是否已收藏
    def ppt_is_coll(self, element):
        try:
            self.getElementAttr(element, "alt")  # alt 属性存在则代表未收藏
            alt = True  # 未收藏
        except:
            alt = False  # 已收藏
        return alt

    # 鼠标点击到第一个免抠元素
    def ppt_detail_get_name(self):
        try:
            ppt_name_xpath = ('xpath', "//div[@class='img-detail']//h1")
            ppt_name = self.getText(ppt_name_xpath)
        except:
            ppt_name = ""
        return ppt_name

    # 在免抠元素模版详情，点击“下载源文件”
    def ppt_detail_download_source_file(self):
        video_detail_source_file_btn_xpath = ('xpath', "//div[@class='type']/div")
        self.click(video_detail_source_file_btn_xpath)

    # 在免抠元素模版详情，点击“收藏按钮”
    def ppt_detail_coll(self):
        ppt_detail_coll_btn_xpath = ('xpath', "//section[@class='collbtn']//span/img[@alt='']")
        self.click(ppt_detail_coll_btn_xpath)
