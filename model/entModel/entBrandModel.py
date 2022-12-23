import random
from pages.basePage import Action
from element.ent.entBrandElemen import EntBrandElement
from element.ent.entIndexElement import EntIndexElement
class EntBrandModel(Action):

    # 点击首页的管理
    def click_manage(self):
        self.click(EntIndexElement.manageMenu_xpath)

    # 在首页管理按钮上点击品牌管理菜单
    def click_brand_manage(self):
        self.click(EntIndexElement.brandManage_xpath)

    # 品牌管理页面的品牌管理
    def get_brand_manage_text(self):
        return self.getText(EntBrandElement.brandManage_xpath)


    #=================================
    #   操作品牌logo
    #=================================
    # 上传logo 图片
    def input_logo(self,file):
        self.write(EntBrandElement.brandInputLogo_xpath,file)

    # 获取logo个数
    def get_logo_num(self):
        try:
            logo_list = self.getElements(EntBrandElement.logo_li_xpath)
            logo_num = len(logo_list)
        except:
            logo_num = 0
        return logo_num

    # 定位到最后一个logo
    def last_logo(self):
        self.mouse_hover(EntBrandElement.last_logo_li_xpath)

    # logo more
    def last_logo_more(self):
        self.click(EntBrandElement.last_logo_li_more_xpath)

    # 删除logo
    def last_logo_del(self):
        self.click(EntBrandElement.last_logo_li_del_xpath)
    # 确定删除logo
    def sure_del_logo(self):
        self.click(EntBrandElement.last_logo_li_del_button_xpath)

    #获取logo名称
    def get_last_logo_name(self):
        return self.getText(EntBrandElement.last_logo_li_name)

    # 重命名logo
    def last_logo_rename(self):
        self.click(EntBrandElement.last_logo_li_rename_xpath)

    # 清空logo名称
    def clear_logo_name(self):
        self.clear(EntBrandElement.rename_logo_xpath)

    # 输入logo名称
    def input_logo_name(self,name):
        self.write(EntBrandElement.rename_logo_xpath,name)

    # 确定重命名logo按钮
    def sure_rename_logo(self):
        self.click(EntBrandElement.last_logo_li_rename_button_xpath)

    # 下载logo
    def download_logo(self):
        self.click(EntBrandElement.last_logo_li_download_xpath)

    #=================================
    #   操作品牌颜色
    #=================================
    # 添加颜色
    def click_add_color(self):
        self.click(EntBrandElement.add_coloer)
    # 输入颜色值
    def input_colors(self):
        self.clear(EntBrandElement.one_input)
        self.clear(EntBrandElement.two_input)
        self.clear(EntBrandElement.three_input)

        self.write(EntBrandElement.one_input, 20)
        self.sleep()
        self.write(EntBrandElement.two_input, 220)
        self.sleep()
        self.write(EntBrandElement.three_input, 100)

    # 确定按钮
    def commit_color(self):
        self.click(EntBrandElement.commit_button)

    # 获取颜色个数
    def get_color_num(self):
        try:
            color_num = self.getElements(EntBrandElement.color_num)
            num = len(color_num)
        except:
            num = 0
        return num

    # 获取颜色名称
    def get_color_name(self):
        try:
            return self.getText(EntBrandElement.last_color_li_name_xpath)
        except:
            return None

    # 颜色模块more
    def click_color_more(self):
        self.mouse_hover(EntBrandElement.last_color_li_xpath)
        self.sleep(1)
        self.click(EntBrandElement.last_color_li_more_xpath)

    # 在颜色模块更多点击删除
    def click_color_del_button(self):
        self.click(EntBrandElement.last_color_li_del_xpath)

    # 确认删除
    def commit_del_color_button(self):
        self.click(EntBrandElement.sure_del_button_xpath)

    #=================================
    #   操作品牌字体
    #=================================

    # 点击上传字体按钮
    def click_upload_font(self):
        self.click(EntBrandElement.upload_font_xpath)

    # 选择字体
    def select_font(self):
        self.click(EntBrandElement.select_font_xpath) # 点击选择字体小三角
        i = random.randint(20,100)
        select_font_name = ('xpath', "//div[@aria-label='选择字体']//div[@class='font-list']//li["+str(i)+"]")
        print("字体定位:",select_font_name)
        self.click(select_font_name)
    # 选择第一个字体
    def select_first_font(self):
        self.click(EntBrandElement.select_font_xpath) # 点击选择字体小三角
        self.sleep(1)
        self.click(EntBrandElement.first_font_xpath)
    # 点击确定按钮
    def sure_font_btn(self):
        self.click(EntBrandElement.select_font_sure_xpath)
        self.sleep(1)
    # 选择字体取消按钮
    def cancel_select_font_btn(self):
        self.click(EntBrandElement.select_font_cancel_button_xpath)
        self.sleep(1)
    # 获取当前字体个数
    def get_font_num(self):
        try:
            font_list = self.getElements(EntBrandElement.font_li_num)
            font_num = len(font_list)
        except:
            font_num = 0
        return font_num

    # 获取接口返回的错误提示
    def get_error_tips(self):
        try:
            return self.getText(EntBrandElement.error_tips_xpath)
        except:
            return None
    # 接口返回成功提示
    def get_success_tips(self):
        return self.getText(EntBrandElement.sucess_tips_xpath)

    # 悬浮到最后一个字体上
    def click_font_more(self):
        self.refresh()
        self.page_down(3000)
        self.mouse_hover(EntBrandElement.last_font_li_xpath)
        self.ptclick(EntBrandElement.last_font_more_xpath)
    # 获取字体名称
    def get_font_name(self):
        return self.getText(EntBrandElement.font_name_xpath)
    # 修改字体
    def click_modfiy_font_button(self):
        self.click(EntBrandElement.last_font_modify_xpath)

    # 确认修改字体
    def sure_modiy_font(self):
        self.click(EntBrandElement.modiy_font_sure_button_xpath)

    # 删除字体
    def click_del_font_button(self):
        self.click(EntBrandElement.last_font_del_xpath)
    # 弹框上的删除按钮
    def click_sure_del_button(self):
        self.click(EntBrandElement.delete_button_xpath)