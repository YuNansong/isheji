from common.readLog import Log
from common.sendDingTalk import SendDingTalk
from common.getYaml import url
from model.scModel.homeModel import HomeModel
from model.scModel.vipModel import VIPModel

# 个人VIP和企业VIP
class PerEntVIP(HomeModel,VIPModel):
    log = Log(__name__)
    logger = log.getLog()
    urlInfo = url['url']['testUrl']

    def qr_code(self):###
        '''验证二维码是否存在'''
        try:
            self.sleep(3)
            iframe = ('xpath', "//div[@class='zfb-box']//iframe") # 支付宝二维码
            self.switch_iframe(iframe)
            code = ('xpath', "//div[@style='position: relative;display: inline-block;']/img")
            len_code = len(self.getElements(code))
            self.out_of_iframe()
            return len_code
        except Exception as e:
            self.logger.error('失败：个人支付页面没有二维码%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：个人支付页面没有二维码")
            raise e

    '''验证VIP--顶部价格'''
    def test_per_vip_price(self,start,end):
        try:
            self.click_per_vip_menu()
            url = self.getUrl()
            if url == self.urlInfo+"/vip":
                for i in range(start,end):
                    vip_type_xpath = ('xpath',"//div[@class='vip-box']/div[@class='vips']/ul/li["+str(i)+"]")
                    self.click(vip_type_xpath)
                    self.sleep(1)
                    price_xpath = ('xpath',"//div[@class='vip-box']/div[@class='vips']/ul/li["+str(i)+"]/div[@class='price']/span[2]")
                    price_text = self.getText(price_xpath)
                    final_price = self.get_per_final_price()
                    assert price_text == final_price
                    self.sleep(0.5)
        except Exception as e:
            self.logger.error('版权站-个人VIP支付页面价格错误%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-个人VIP支付页面价格错误")
            raise e

    '''验证VIP--表格价格'''
    def test_per_vip_price_table(self,start,end):
        try:
            self.click_bar() # 操作滚动条
            self.sleep(1)
            # 点击授权范围对比
            self.click_shouquan()
            self.sleep(1)
            for i in range(int(start),int(end)):
                preliminary_price = ('xpath', "//div[@class='table-box']/div["+str(i)+"]//span[@class='price']")
                price_text = self.getText(preliminary_price)#外边价格的字符串
                price = price_text[:-1]
                self.logger.info("VIP页面上的支付价格: %s" % price)
                buy_button_xpath = ('xpath', "//div[@class='table-box']/div["+str(i)+"]//span[contains(text(),'立即购买')]")
                self.mouse_hover(buy_button_xpath)
                self.ptclick(buy_button_xpath)
                self.sleep(2)
                final_price = self.get_alert_price()
                self.logger.info("支付弹框上的支付价格: %s" % final_price)
                self.alert_close_btn()
                assert final_price == price
        except Exception as e:
            self.logger.error('版权站个人VIP支付页面表格打开支付价格错误%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站个人VIP支付页面表格打开支付价格错误")
            raise e
    # 验证企业VIP价格是否正确
    def test_ent_vip(self,start,end):
        try:
            #进入企业VIP页面
            self.click_ent_vip_menu()
            url = self.getUrl()
            if url == self.urlInfo+"/teamvip":
                for i in range(int(start),int(end)):
                    price_text = self.get_vip_price(i)
                    final_price = self.get_alert_price()
                    code_num = self.qr_code() # 获取支付宝二维码
                    self.sleep(2)
                    self.alert_close_btn()
                    assert final_price == price_text
                    assert code_num == 1
        except Exception as e:
            self.logger.error('企业VIP页面团队套餐价格异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业VIP页面团队套餐价格异常")
            raise e

    '''验证企业VIP--表格价格'''
    def test_ent_vip_price_table(self,start,end):
        try:
           self.click_ent_shouquan()
           self.sleep(2)
           for i in range(int(start),int(end)):
               preliminary_price = ('xpath', "//div[@class='table-box']/div["+str(i)+"]//span[@class='price']")
               price_text = self.getText(preliminary_price)#外边价格的字符串
               price = price_text[:-1]
               self.logger.info("VIP页面上的支付价格: %s" % price)
               buy_button_xpath = ('xpath', "//div[@class='table-box']/div["+str(i)+"]//span[contains(text(),'立即购买')]")
               self.mouse_hover(buy_button_xpath)
               self.ptclick(buy_button_xpath)
               self.sleep(2)
               final_price = self.get_alert_price()
               self.logger.info("支付弹框上的支付价格: %s" % final_price)
               self.alert_close_btn()
               assert final_price == price
        except Exception as e:
            self.logger.error('企业VIP页面表格中团队套餐价格异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业VIP页面表格中团队套餐价格异常")
            raise e

     # 验证购买单张套餐
    def buy_package_sheet(self):
        try:
            for i in range(1,3):
                select_one_price_xpath = ('xpath',"//div[@class='team-type']/div[@class='team-item']["+str(i)+"]//li[1]/div[last()]//div[@class='price']")
                danjia_price = self.getText(select_one_price_xpath)
                self.logger.info("danjia_price: %s" % danjia_price[1:])
                select_one_xpath = ('xpath',"//div[@class='team-type']/div[@class='team-item']["+str(i)+"]//li[1]/div[1]")
                self.click(select_one_xpath)
                self.sleep(1)
                buy_button_xpath = ('xpath',"//div[@class='team-type']/div["+str(i)+"]/div[contains(text(),'立即购买')]")
                self.click(buy_button_xpath)
                # 在弹框上获取价格
                self.sleep(2)
                yingfu_price_xpath = ('xpath',"//div[@class='pay-info']/p/span") # 弹框的应付价格
                price_num = self.getText(yingfu_price_xpath)
                self.logger.info("price_num: %s" % price_num[1:])
                # 关闭弹框
                self.alert_close_btn()
        except Exception as e:
            self.logger.error('单张购买页面价格异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("单张购买页面价格异常")
            raise e

    # 验证购买单张图片价格
    def test_buy_package_sheet(self):
        try:
            self.buy_single_package()
            url = self.getUrl()
            if url == self.urlInfo+"/solavip?type=1":
                self.buy_package_sheet()
        except Exception as e:
            self.logger.error('购买单张价格异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("购买单张价格异常")
            raise e

    # 验证购买单条视听价格
    def test_buy_package_single(self):
        try:
            self.click_media() # 切换到视听
            self.sleep(2)
            self.buy_package_sheet()
            self.close_handle()
        except Exception as e:
            self.logger.error('购买单条价格异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("购买单条价格异常")
            raise e