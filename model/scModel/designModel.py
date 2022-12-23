from pages.basePage import Action

class DesignModel(Action):
    # 设计列表查询结果
    def design_search_result(self):
        try:
            design_item_xpath = ('xpath',"//div[@class='search-item']/div[@class='plane-material']")
            num = len(self.getElements(design_item_xpath))
        except:
            num = 0
        return num
    # 鼠标悬浮到第一张图片
    def design_hover_first_pic(self):
        design_item_xpath = ('xpath',"//div[@class='search-item']/div[@class='plane-material'][1]")
        self.mouse_hover(design_item_xpath)

    # 点击样图下载
    def design_download_first_yangtu(self):
        design_yangtu_btn_xpath = ('xpath',"//div[@class='search-item']/div[@class='plane-material'][1]//div[contains(text(),'样图下载')]")
        self.click(design_yangtu_btn_xpath)

    # 点击收藏按钮
    def design_coll_first_pic(self):
        design_yangtu_btn_xpath = ('xpath',"//div[@class='search-item']/div[@class='plane-material'][1]//div[@class='image-item-shadowbox']//img")
        self.click(design_yangtu_btn_xpath)

    # 鼠标点击第一张图片
    def design_click_first_pic(self):
        design_item_xpath = ('xpath',"//div[@class='search-item']/div[@class='plane-material'][1]")
        self.click(design_item_xpath)

    # 鼠标点击到第一张图片
    def design_detail_get_name(self):
        try:
            design_name_xpath = ('xpath',"//div[@class='right']//h1")
            design_name = self.getText(design_name_xpath)
        except:
            design_name = ""
        return design_name

    # 在设计模版详情，点击“下载样图”
    def design_detail_download_yangtu(self):
        design_detail_download_btn_xpath = ('xpath',"//div[@class='yangt']")
        self.click(design_detail_download_btn_xpath)

    # 在设计模版详情，点击“下载源文件”
    def design_detail_download_source_file(self):
        design_detail_source_file_btn_xpath = ('xpath',"//div[@class='type']/div")
        self.click(design_detail_source_file_btn_xpath)

    # 在设计模版详情，点击“收藏按钮”
    def design_detail_coll(self):
        design_detail_coll_btn_xpath = ('xpath',"//div[@class='right']//span/img[@alt='']")
        self.click(design_detail_coll_btn_xpath)