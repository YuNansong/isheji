from pages.basePage import Action
from pages.isheji_c.tempCenterPage.workbenchPage import WorkBench

class EntMyCollModel(Action):
    # 获取图片模板个数
    def get_pictemp_num(self):
        pic_list_xpath = ('xpath',"//div[@class='mydeisgn-datalist']/ul[1]/li")
        pic_num = len(self.getElements(pic_list_xpath))
        return pic_num

    # 点模板进工作台
    def click_last_pictemp(self):
        last_pic_xpath = ('xpath',"//div[@class='mydeisgn-datalist']/ul[1]/li[last()]")
        self.click(last_pic_xpath)

    # 获取模板ID
    def get_temp_id(self,driver):
        try:
            id = WorkBench(driver).get_temp_id()
            temp_id = int(id)
        except:
            temp_id = 0
        return temp_id

    # 保存模板
    def save_temp(self,driver):
        WorkBench(driver).save_btn()

    # 悬浮到最后一张模板
    def hover_last_pictemp(self):
        last_pic_xpath = ('xpath',"//div[@class='mydeisgn-datalist']/ul[1]/li[last()]")
        self.mouse_hover(last_pic_xpath)
        self.sleep(1)

    # 取消收藏
    def click_cancel_coll(self):
        last_pic_coll_xpath = ('xpath',"//div[@class='mydeisgn-datalist']/ul[1]/li[last()]/div/div/span")
        self.click(last_pic_coll_xpath)

    # 在温馨提示弹框上点击确定按钮
    def click_cancel_sure_btn(self):
        sure_btn_xpath = ('xpath',"//div[@aria-label='温馨提示']//button[2]")
        self.click(sure_btn_xpath)