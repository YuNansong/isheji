from pages.basePage import Action
from element.sc_copyright.sc_special_element import SpecialmoreElement
from element.sc_copyright.sc_home_element import SCHomePageElement


class SpecialModel(Action):
    # 在专题页面悬浮到第一张图片上
    def zt_hover_first_pic(self):
        self.mouse_hover(SpecialmoreElement.zt_first_pic_xpath)

    def zt_click_first_pic(self):
        self.ptclick(SpecialmoreElement.zt_first_pic_xpath) # 在专题上点击第一张图片


    # 获取第一张图片的alt属性值
    def zt_get_pic_alt(self):
        try:
            attr = self.getElementAttr(SpecialmoreElement.yangtu_element_attr,"alt")
        except:
            attr = ""
        return attr

    def zt_get_pic_name(self):
        try:
            name = self.getText(SCHomePageElement.img_name_xpath)
        except:
            name = ""
        return name

    # 下载样图
    def zt_click_yt_pic(self):
        self.click(SpecialmoreElement.zt_download_btn)

    # 点击相似图片
    def zt_click_xs_pic(self):
        self.click(SpecialmoreElement.xs_download_btn)

    # 相似图片列表图片个数
    def zt_get_xs_pic_list(self):
        try:
            pic_num = len(self.getElements(SpecialmoreElement.pic_list_xpath))
        except:
            pic_num = 0
        return pic_num

