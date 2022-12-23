from pages.basePage import Action

class VideoModel(Action):
    # 视频列表查询结果
    def video_search_result(self):
        try:
            video_item_xpath = ('xpath',"//div[@id='coryright-video-list']/div")
            num = len(self.getElements(video_item_xpath))
        except:
            num = 0
        return num
    # 鼠标悬浮到第一个视频
    def video_hover_first(self):
        video_item_xpath = ('xpath',"//div[@id='coryright-video-list']/div[1]")
        self.mouse_hover(video_item_xpath)
    # 点击收藏按钮
    def video_coll_first(self):
        video_yangtu_btn_xpath = ('xpath',"//div[@id='coryright-video-list']/div[1]//div[@class='image-item-shadowbox']//img")
        self.click(video_yangtu_btn_xpath)
    # 鼠标点击到第一个视频
    def video_click_first(self):
        video_item_xpath = ('xpath',"//div[@class='search-list autoscroll-box']//div[@id='coryright-video-list']/div[1]/img")
        self.click(video_item_xpath)

        # 定位视频下载成功提示
    def video_get_tips_list(self):
        first_download = ('xpath', "//div[@class='el-message el-message--success']")
        again_download = ('xpath', "//p[@class='el-message__content']")
        tips_list = [first_download, again_download]
        return tips_list

    # 判断是否已收藏
    def video_is_coll(self, element):
        try:
            self.getElementAttr(element, "alt") # alt 属性存在则代表未收藏
            alt = True # 未收藏
        except:
            alt = False # 已收藏
        return alt
    # 鼠标点击到第一个视频
    def video_detail_get_name(self):
        try:
            video_name_xpath = ('xpath',"//div[@class='right']//h1")
            video_name = self.getText(video_name_xpath)
        except:
            video_name = ""
        return video_name

    # 在视频模版详情，点击“下载源文件”
    def video_detail_download_source_file(self):
        video_detail_source_file_btn_xpath = ('xpath',"//div[@class='type']/div")
        self.click(video_detail_source_file_btn_xpath)

    # 在视频模版详情，点击“收藏按钮”
    def video_detail_coll(self):
        video_detail_coll_btn_xpath = ('xpath',"//div[@class='right']//span/img[@alt='']")
        self.click(video_detail_coll_btn_xpath)