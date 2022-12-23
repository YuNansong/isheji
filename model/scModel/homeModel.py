from element.sc_copyright.sc_home_element import SCHomePageElement
from model.scModel.commModel import CommModel

class HomeModel(CommModel):
    def click_change(self):
        change_button = ('xpath', "//span[contains(text(),'切换身份')]")
        self.click(change_button)
        self.sleep(2)

    # 首页图片分类---悬浮图片
    def mouse_hover_pic(self):
        self.mouse_hover(SCHomePageElement.first_img_xpath) # 图片素材第一张图
        self.sleep(2)

    # 热门推荐第一个集合
    def click_index_first_pic(self):
        first_picture = ('xpath', "//div[@class='home-hot clear']/div[1]/div[1]/div[2]//li[1]")
        self.click(first_picture)
    # 切换身份
    def change_shenfen(self):
        change_button = ('xpath', "//div[@class='dropdown_area']/ul//span[contains(text(),'切换身份')]")
        self.click(change_button)
    # 选择个人
    def select_person(self):
        person = ('xpath', "//div[@class='user-check']/div[1]")
        self.click(person)

    # 点击选择团队箭头
    def click_jiantou(self):
        select_jiantou = ('xpath',"//div[@class='user-check']//span[@class='iconfont icon-xiangxiajiantou']")
        self.click(select_jiantou)

    # 切换身份弹框上点击确定按钮
    def click_sure_btn(self):
        enter_button = ('xpath', "//div[@class='switch-user-inner']/div[@class='user-btn']")
        self.click(enter_button)

    def get_change_title(self):
        title_xpath = ('xpath', "//div[@class='switch-user-inner']//div[@class='title']")
        title = self.getText(title_xpath)
        return title

    # 点击个人VIP
    def click_per_vip_menu(self):
        personal_vip_xpath = ('xpath',"//a[@class='vip-btn l geren' and contains(text(),'个人')]")
        self.click(personal_vip_xpath)
        self.sleep(2)
        self.window(-1)
    # 点击企业VIP
    def click_ent_vip_menu(self):
        personal_vip_xpath = ('xpath',"//a[@class='vip-btn l qiye' and contains(text(),'企业VIP')]")
        self.click(personal_vip_xpath)
        self.sleep(2)
        self.window(-1)

    # 点击收藏夹
    def click_coll_folder(self):
        coll_folder_xpath = ('xpath',"//div[@class='collect-btn l']")
        self.click(coll_folder_xpath)
        self.window(-1)

    # 选择团队
    def select_team(self):
        test_team = ('xpath', "//ul[@class='group-list']/li[1]")
        self.click(test_team)


    def act_download_record(self):
        download_record_xpath = ('xpath',"//div[@class='dropdown_area']/ul//span[contains(text(),'下载记录')]")
        self.click(download_record_xpath)

    # 切换到团队身份
    def change_team(self):
        try:
            self.sleep(1)
            self.click_img()
            self.change_shenfen()
            self.click_jiantou()
            self.select_team()
            self.click_sure_btn()
        except Exception as e:
            self.logger.error('切换团队身份失败%s' % repr(e))
            raise e
    # 切换到个人身份
    def change_per(self):
        try:
            self.sleep(1)
            self.click_img()
            self.sleep(0.5)
            self.change_shenfen()
            self.sleep(0.5)
            self.select_person() # 选择个人身份
            self.sleep(0.5)
            self.click_sure_btn()
            self.sleep(0.5)
        except Exception as e:
            self.logger.error('切换团队身份失败%s' % repr(e))
            raise e

        # 进入个人中心下载记录列表
    def act_account_center(self):
        self.click_img()
        self.act_download_record()
        self.sleep(2)
        self.window(-1)
    # 悬浮到第一个视频
    def hover_first_video(self):
        self.mouse_hover(SCHomePageElement.first_video_xpath) # 1.悬浮到第一个视频