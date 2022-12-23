from pages.basePage import Action

class PerCenterModel(Action):
    # 下载记录--批量授权按钮
    def click_all_auth(self):
        author_button = ('xpath', "//div[@class='shouquan-btn']")
        self.click(author_button)
    # 下载记录--全选
    def select_all_button(self):
        all_button = ('xpath', "//thead[@class='has-gutter']//span[@class='el-checkbox__input']")
        self.click(all_button)

    # 下载记录--批量授权--下载授权书按钮
    def download_auth_button(self):
        download_button = ('xpath', "//div[@class='caozuo']/div[2]")
        self.click(download_button)

    # 授权选择企业名称
    def select_enterprise(self):
        select_enterprise = ('xpath', "//span[@class='el-radio__inner']")
        self.click(select_enterprise)

    # 授权弹框下载按钮
    def sure_download(self):
        download = ('xpath', "//button[@class='user-btn banquan-btn']")
        self.click(download)
    # 获取tips
    def get_tips(self):
        try:
            success_tips_xpath = ('xpath', "//p[@class='el-message__content']")
            success_tips = self.getText(success_tips_xpath)
        except:
            success_tips = ""
        return str(success_tips).strip()

    # 授权弹框的关闭
    def click_x_button(self):
        x_button = ('xpath', "//div[@class='banquan-close']")
        self.click(x_button)

    # 在下载记录点击取消按钮
    def click_cancel_button(self):
        cancel = ('xpath', "//div[contains(@class,'caozuo')]//div[1]")
        self.click(cancel)

    # 企业素材菜单
    def ent_mertal(self):
        enter_path = ('xpath', "//div[@class='personal']/nav/ul/li[4]")
        self.click(enter_path)

    # 企业素材 -- 获取文件夹个数
    def get_folder_num(self):
        try:
            centent_path = ('xpath', "//ul[@class='folder']/li")#有几个文件夹
            count = len(self.getElements(centent_path))
        except:
            count = 0
        return count
