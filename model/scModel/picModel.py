from pages.basePage import Action
from element.sc_copyright.sc_home_element import SCHomePageElement
from element.sc_copyright.sc_picdetail_element import PicDetailElement


# 图片列表页【搜索结果页】
class PicModel(Action):

    # 在图片列表获取搜索到的图片个数
    def pic_list_get_pic_num(self):
        try:
            pic_list_xpath = ('xpath', "//div[@id='coryright-image-list']/div")
            pic_num = len(self.getElements(pic_list_xpath))
        except:
            pic_num = 0
        return pic_num

    # 图片列表第一个图片
    def click_picList_first_pic(self):
        first_pic_xpath = ('xpath', "//div[@id='coryright-image-list']/div[1]")
        self.ptclick(first_pic_xpath)

    # 在图片详情获取视频名称
    def get_pic_name(self):
        try:
            img_name = self.getText(SCHomePageElement.img_name_xpath)
        except:
            img_name = ""
        return img_name

    # 在图片详情获取图片ID
    def get_pic_id(self):
        try:
            img_id = self.getText(SCHomePageElement.img_id_xpath)
        except:
            img_id = ""
        return img_id

    # 在图片详情获取第一个关键词
    def pic_detail_get_key_name(self):
        try:
            key_word_name = self.getText(PicDetailElement.key_word)
        except:
            key_word_name = ""
        return key_word_name

    # 在图片详情点击第一个关键词
    def pic_detail_click_key(self):
        self.click(PicDetailElement.key_word)

    # 在图片集合列表页面点击图片
    def click_sen_first_pic(self):
        try:
            other_first = ('xpath', "//div[@id='coryright-image-list']/div[1]/a/img")
            self.ptclick(other_first)
        except:
            other_first2 = ('xpath', "//div[@id='coryright-image-list']/div[1]/div[1]/img")
            self.ptclick(other_first2)

    # 悬浮到图片上
    def pl_hover_first_pic(self):
        try:
            first_pic = ('xpath', "//div[@id='coryright-image-list']/div[1]/a/img")
            self.mouse_hover(first_pic)
        except:
            first_pic = ('xpath', "//div[@id='coryright-image-list']/div[1]/div[1]/img")
            self.mouse_hover(first_pic)

    # 图片列表下载样图
    def download_yangtu(self):
        download_sample = ('xpath', "//div[@id='coryright-image-list']/div[1]//div[@class='cardiconbox iconbox-down']")
        self.click(download_sample)

    # 图片详情下载样图
    def pic_detail_download_yangtu(self):
        download_sample = ('xpath', "//div[@class='yangt']")  # 下载样图按钮
        self.click(download_sample)

    # 下载样图无额度，提示
    def apply_title(self):
        apply_title = self.getText(SCHomePageElement.apply_title_element)
        self.sleep(2)
        self.click(SCHomePageElement.closed_alert)  # 点击确定按钮，关闭弹框
        return apply_title

    # 下载原图
    def download_yuantu(self):
        drawing_download_button = ('xpath', "//div[@class='active']")
        self.click(drawing_download_button)

    # 获取重复下载图片提示
    def get_repeat_download_tips(self):
        first_download = ('xpath', "//p[@class='el-message__content']")
        real_tips = self.getText(first_download)
        return real_tips

    # 获取下载图片提示
    def get_download_tips(self):
        first_download = ('xpath', "//div[@class='el-message el-message--success']")
        real_tips = self.getText(first_download)
        return real_tips

    # 图片详情关闭
    def close_pic_detail(self):
        close_btn = ('xpath', "//div[@class='detailsPop']//button[@aria-label='Close']")
        self.click(close_btn)

    # 定位图片下载成功提示
    def get_tips_list(self):
        tips = ('xpath', "//div[@class='el-message el-message--success']")
        # again_download = ('xpath', "//p[@class='el-message__content']")
        # tips_list = [first_download, again_download]
        return tips
