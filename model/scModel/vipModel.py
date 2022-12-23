from pages.basePage import Action
from common.readLog import Log

class VIPModel(Action):
    log = Log(__name__)
    logger = log.getLog()
    # VIP 页面断言
    def get_vip_assert_content(self):
        try:
            duibi_xpath = ('xpath',"//div[@class='show-box']/i")
            self.click(duibi_xpath)
        except:
            self.logger.info("企业VIP无该信息")
        self.sleep(1)
        shuoming_xpath = ('xpath',"//div[@class='team-duibi']/h2")
        shuoming_text = self.getText(shuoming_xpath)
        return shuoming_text

    def get_alert_price(self):
        final_price_xpath = ('xpath', "//p[@class='pay-price']/span")
        final_price_text = self.getText(final_price_xpath)#里边的价格字符串
        final_price = final_price_text[1:]
        return final_price

    # 关闭弹框
    def alert_close_btn(self):
        x_button = ('xpath', "//div[@class='banquan-close']")
        self.click(x_button)

    # 在页面上获取vip价格
    def get_vip_price(self,i):
        preliminary_price = ('xpath', "//div[@class='team-type']/div["+str(i)+"]//div[@class='price']/span[@class='price-num']")
        price_text = self.getText(preliminary_price)#外边价格的字符串
        buy_buyyon = ('xpath', "//div[@class='team-type']/div["+str(i)+"]//div[contains(text(),'立即购买')]")
        self.click(buy_buyyon)
        self.sleep()
        return price_text

    # 在企业页面点击单张购买
    def buy_single_package(self):
        danzhang_button = ('xpath', "//div[@class='to-bay-box']/span")
        self.click(danzhang_button)
        self.window(-1)

    # 切换到视听
    def click_media(self):
        media_xpath = ('xpath',"//span[contains(text(),'视听')]")
        self.click(media_xpath)

    #  新个人VIP页面
    def click_shouquan(self):
        # 点击授权范围对比
        table_xpath = ('xpath',"//div[@class='show-box']/i")
        self.click(table_xpath)

    # 企业VIP操作对比
    def click_ent_shouquan(self):
        duibi_xpath = ('xpath',"//div[@class='to-duibi']")
        self.custom_scroll_bar(duibi_xpath)

    # 操作滚动条
    def click_bar(self):
        price_xpath = ('xpath',"//div[@class='vips']/ul/li[1]")
        self.custom_scroll_bar(price_xpath)

    # 获取支付价格
    def get_per_final_price(self):
        try:
            final_text_xpath = ('xpath',"//div[@class='vip-box']/div[@class='text']/span")
            final_price = self.getText(final_text_xpath)
        except:
            final_price = ""
        return  final_price