import random
from pages.basePage import Action
from element.sc_copyright.sc_favoristes_element import FavoristesElement
from element.sc_copyright.sc_home_element import SCHomePageElement


# 收藏逻辑判断
class FavoritesModel(Action):

    # 点击收藏夹的素材类型
    def click_type(self, i):
        type_xpath = ('xpath', "//div[@class='collect content']//ul[@class='type']/li[" + str(i) + "]")
        self.click(type_xpath)

    def get_list_folder(self):
        try:
            folder_num = len(self.getElements(FavoristesElement.folder_list_element))  # 返回收藏夹个数
        except:
            folder_num = 0
        return folder_num

    # 在点击收藏弹窗的提示框，选择收藏夹
    def select_coll_folder(self, driver):
        # 选择收藏夹
        # 如果收藏夹个数小于2个则再创建一个
        if self.get_list_folder() < 2:
            if self.get_list_folder() < 1:
                self.write_folder_name()
                self.click_coll_sure_btn()  # 为了保存

            # 弹框上的新建文件夹
            self.click_new_folder_btn()
            self.sleep(2)
            self.add_folder()

        self.sleep(2)
        self.logger.info("在弹框上获取到的收藏夹个数为%d" % self.get_list_folder())
        if self.get_list_folder() >= 2:
            # 循环遍历
            for i in range(1, self.get_list_folder() + 1):
                folder_li_element = ('xpath', "//ul[@class='collect-list']/li[" + str(i) + "]")
                folder_name_element = ('xpath', "//ul[@class='collect-list']/li[" + str(i) + "]/p")
                attr = self.getElementAttr(folder_li_element, "class")
                if attr != "noclick":
                    name = self.getText(folder_name_element)
                    self.click(folder_li_element)
                    self.logger.info("我选中的新文件夹为：%s" % name)
                    self.sleep(2)
                    self.click_coll_sure_btn()
                    break

    # 收藏图片，视频，平面模板判断逻辑
    def coll_material(self, alt, element, driver):
        flag = False
        if alt == True:  # 未收藏
            self.click(element)
            self.sleep(1)
            # 如果没有文件夹，则需要先创建
            try:
                self.select_coll_folder(driver)  # 应该判断没有可选的 出现异常，重新创建
            except:
                while flag == False:
                    try:
                        self.click_new_folder_btn()
                        self.write_folder_name()  # 输入收藏夹名称
                        self.sleep()
                        self.click_coll_sure_btn()  # 为了保存
                        tip = self.folder_name_repeat_tips()  # 创建成功重复的提示弹窗
                    except:
                        tip = ""

                    if tip == "文件夹名称重复":
                        flag = False
                    else:
                        flag = True
                self.select_coll_folder(driver)  # 新建完了再选择
            # 获取收藏成功提示

            tips = self.getText(SCHomePageElement.succ_tips_element)
            print(tips)
            return tips

    # 在菜单上点击收藏夹
    def click_coll_folder(self):
        self.click(FavoristesElement.coll_folder_element)

    # 左侧菜单--收藏夹
    def left_nav_folder(self):
        self.sleep(3)
        self.click(FavoristesElement.folder_element)
        self.sleep(2)

    # 左侧菜单--订单列表
    def left_nav_order(self):
        self.click(FavoristesElement.order_element)
        self.sleep(1)

    # 收藏夹为空,获取提示信息
    def get_default_tips(self):
        tips = self.getText(FavoristesElement.empty_tips_element)
        return tips

    # 新建收藏夹
    def create_folder(self):
        self.click(FavoristesElement.add_element)
        self.sleep(2)

    # 填写文件夹名称
    def write_folder_name(self):
        folderId = random.randint(0, 9999)
        self.clear(FavoristesElement.input_coll_folder_name)
        self.write(FavoristesElement.input_coll_folder_name, "收藏夹" + str(folderId))

    # 获取文件夹为空或者名字重复提示
    def folder_name_repeat_tips(self):
        tips = self.getText(FavoristesElement.repeat_tips_element)
        return tips

    # 弹框上的点击新建文件夹
    def click_new_folder_btn(self):
        self.click(FavoristesElement.new_btn)

    # # 点击确定按钮
    # def click_sure_btn(self):
    #     self.ptclick(FavoristesElement.sure_btn_element_xpath)

    # 点击确定按钮
    def click_coll_sure_btn(self):
        self.click(FavoristesElement.sure_btn_element_xpath)

    # 获取收藏夹个数
    def getFolderNum(self):
        try:
            folder_num = len(self.getElements(FavoristesElement.folder_li_element))
        except:
            folder_num = 0
        return folder_num

    # 新增收藏夹
    def add_folder(self):
        flag = False
        while flag == False:
            try:
                self.write_folder_name()  # 输入收藏夹名称
                self.sleep()
                self.click_coll_sure_btn()  # 为了保存
                tip = self.folder_name_repeat_tips()  # 创建成功重复的提示弹窗
            except:
                tip = ""

            if tip == "文件夹名称重复":
                flag = False
            else:
                flag = True
