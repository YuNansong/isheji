from pages.basePage import Action
from element.sc_copyright import sc_search_element

class MusicModel(Action):
    Ele = sc_search_element.sc_Ele

    # 搜索音乐
    def clear_search_input(self):
        self.clear(self.Ele.scInput)
    # 输入音乐搜索关键词
    def write_search_input(self,sc_text):
        self.write(self.Ele.scInput, sc_text)
    # 点击搜索按钮
    def click_search_btn(self):
        self.click(self.Ele.scBtn)
    # 获取搜索结果
    def get_search_result(self):
        try:
            music_num_xpath = ('xpath', "//div[@class='search-title']/span")
            num_str = self.getText(music_num_xpath)
            num = int(num_str[3:-5])
        except:
            try:
                music_xpath = ('xpath',"//div[@class='zonggd']/div")
                num = len(self.getElements(music_xpath))
            except:
                num = 0
        return num

    # 悬浮第一个音乐
    def hover_music(self):
        self.mouse_hover(self.Ele.firstMu)

    # 在音乐列表播放音乐
    def musicList_play(self):
        self.click(self.Ele.playBtn)

    # 在音乐列表暂停播放音乐
    def musicList_pause(self):
        self.click(self.Ele.pauseBtn)

    # 点击收藏按钮
    def click_coll_btn(self):
        self.click(self.Ele.muCollect)

    # 获取收藏夹列表收藏夹个数
    def get_folder_is_null(self):
        try:
            folderList = self.getElements(self.Ele.coDialog)
            folderNum = len(folderList)
        except:
            folderNum = 0
        return folderNum
    # 收藏音乐点击新建文件夹
    def click_new_folder_btn(self):
        self.click(self.Ele.coCrBtn)
    # 收藏音乐填写文件夹名称
    def writh_folder_name(self):
        self.write(self.Ele.coCrInput, "测试收藏")
    # 收藏音乐提交文件夹名称
    def click_submmit(self):
        self.click(self.Ele.coSubBtn)
    #
    def select_first_folder(self):
        self.click(self.Ele.coList)


# ===============================
    # 关闭音乐详情
    def closed_music_detail(self):
        closed_detail_xpath = ('xpath', "//div[@class='detailsPop']//button[@type='button']")
        self.click(closed_detail_xpath)

    # 在音乐详情获取音乐名称
    def get_music_name(self):
        try:
            music_name_xpath = ('xpath', "//div[@class='right']/div[1]//h1[@class='h1']")
            music_name = self.getText(music_name_xpath)
        except:
            music_name = ""
        return music_name

    # 音乐详情页，下载音乐
    def download_music_btn(self):
        download_music_xpath = ('xpath',"//div[@class='music-detail']//div[contains(text(),'下载音乐')]")
        self.click(download_music_xpath)

