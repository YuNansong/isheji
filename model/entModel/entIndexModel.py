from element.ent.entIndexElement import EntIndexElement
from pages.basePage import Action

class EntIndexModel(Action):
    # 点击首页的管理
    def click_manage(self):
        self.click(EntIndexElement.manageMenu_xpath)

    # 在首页管理按钮上点击成员管理菜单
    def click_member_manage(self):
        self.click(EntIndexElement.memberManage_xpath)
        self.sleep(2)

    # 在首页管理按钮上点击数据统计菜单
    def click_data_statistice(self):
        self.click(EntIndexElement.dataStatistice_xpath)
        self.sleep(2)

    # 在首页管理按钮上点击企业素材菜单
    def click_ent_sucai(self):
        self.click(EntIndexElement.entsucai_xpath)
        self.sleep(2)

    # 在首页管理按钮上点击企业素材菜单
    def click_ent_temp(self):
        self.click(EntIndexElement.enttemp_xpath)
        self.sleep(2)

    # 在首页管理按钮上点击企业素材菜单
    def click_ent_banquan(self):
        self.click(EntIndexElement.banquan_xpath)
        self.sleep(2)

    # 在首页管理按钮上点击企业素材菜单
    def click_ent_home(self):
        self.click(EntIndexElement.homemanage_xpath)
        self.sleep(2)

    # 在首页管理按钮上点我的设计菜单
    def click_ent_mydesign(self):
        self.click(EntIndexElement.mydesign_xpath)
        self.sleep(2)

    # 在首页管理按钮上点击我的搜藏菜单
    def click_ent_myColl(self):
        self.click(EntIndexElement.mycoll_xpath)
        self.sleep(2)

    # 首页企业VIP
    def click_ent_vip(self):
        self.click(EntIndexElement.entVip_xpath)
        self.sleep(2)

    # 首页模板中心
    def click_temp_center(self):
        self.click(EntIndexElement.tempCenter_xpath)
        self.sleep(2)

    # 首页新建设计
    def click_new_design(self):
        self.click(EntIndexElement.newdesign_xpath)
        self.sleep(2)

