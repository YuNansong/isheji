from element.ent.entNewDesignElement import NewDesignElement
from pages.basePage import Action

class NewDesignModel(Action):
    # 自定义尺寸按钮
    def click_custom_button(self):
        self.click(NewDesignElement.custom_xpath)

    # 输入尺寸大小--宽
    def input_custom_wide(self,wide):
        self.write(NewDesignElement.input_wide_xpath,wide)

    # 输入尺寸大小--高
    def input_custom_high(self,high):
        self.write(NewDesignElement.input_high_xpath,high)

    # 点击开始设计
    def click_start_design(self):
        self.click(NewDesignElement.start_design_xpath)


