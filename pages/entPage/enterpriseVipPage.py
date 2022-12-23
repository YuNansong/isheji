import time
from pages.basePage import Action
from common.interface import Interface
from common.readLog import Log


class EnterpriseVipPage(Action):
    log = Log(__name__)
    logger = log.getLog()

    def getUserInfo(self):
        userInfo = Interface().getUserInfo()
        return userInfo

    def test_safe(self):
        try:
            gaoji = ('xpath', "//button[@id='details-button']")
            self.click(gaoji)
            unsafe = ('xpath', "//a[@id='proceed-link']")
            self.click(unsafe)
        except Exception as e:
            self.sleep()
            self.logger.error('我的企业：没有出现：风险提示%s' % repr(e))
            raise e

    def safe(self):
        self.appoint_url(self.sleep, self.test_safe)

    # 在导航点击企业VIP
    def click_ent_vip(self):
        en_vip = ('xpath', "//a[@id='jumpToCompanyVip']")
        self.click(en_vip)
        self.window(-1)
        self.safe()

    # 在企业VIP页面获取开通企业版按钮的值
    def getQiyeVipContent(self):
        openButton = ('xpath', "//div[@class='landing-page-banner-btn']/button[1]/span")
        text = self.getText(openButton)
        return str(text).strip()

    # 开通企业版
    def click_qiye_button(self):
        openButton = ('xpath', "//div[@class='landing-page-banner-btn']/button[1]/span")
        self.click(openButton)

    # 进入企业版
    def get_info_qiye_button(self):
        button = ('xpath', "//div[@class='landing-page-banner-btn']/button[2]/span")
        self.click(button)
        self.sleep()
        self.window(-1)
        self.safe()

    def edit_qiye_contact_information(self):
        name = ('xpath', "//div[contains(text(),'方式二')]/parent::div/form[@class='el-form']/div[1]/div[1]/div/input")
        self.write(name, "测试账号")
        time.sleep(1)
        phone = ('xpath', "//div[contains(text(),'方式二')]/parent::div/form[@class='el-form']/div[2]/div[1]/div/input")
        self.write(phone, "13222222222")
        time.sleep(1)
        entName = ('xpath', "//div[contains(text(),'方式二')]/parent::div/form[@class='el-form']/div[3]/div[1]/div/input")
        self.write(entName, "测试企业名称")
        time.sleep(1)
        job = ('xpath', "//div[contains(text(),'方式二')]/parent::div/form[@class='el-form']/div[4]/div[1]/div/input")
        self.write(job, "总经理")
        time.sleep(1)
        question = ('xpath', "//input[@readonly='readonly']")
        self.ptclick(question)  # 点击关注问题
        time.sleep(1)
        selectQus = ('xpath', "//span[contains(text(),'定制设计服务')]/parent::label/span[1]")
        self.ptclick(selectQus)  # 选择定制服务
        time.sleep(1)
        self.ptclick(name)  # 点击职位，让选择的问题框消失
        time.sleep(1)
        submitButton = ('xpath', "//div[contains(text(),'方式二')]/parent::div/form[@class='el-form']/button")
        self.ptclick(submitButton)

    # 添加开通企业版提交成功提示
    def get_add_succ_tips(self):
        time.sleep(1)
        tipsElement = ('xpath', "//p[@class='el-message__content']")
        tips = self.getText(tipsElement)
        return tips

    # 已经进入企业版中
    def get_into_qiye(self):
        # 如果用户开通了企业版本则进入企业版本页面，否则打开联系方式
        self.get_info_qiye_button()
        try:
            mySpaceElement = ('xpath', "//li[@class='leftnav-submenu']/span[contains(text(),'我的空间')]")
            text = self.getText(mySpaceElement)
        except:
            text = self.edit_qiye_contact_information()
        return text

    def click_jichu_pay(self):
        pay_now_button = ('xpath', "//div[@class='product-wrapper']/div[1]/p[5]/button")
        self.click(pay_now_button)

    def click_gaoji_pay(self):
        pay_now_button = ('xpath', "//div[@class='product-wrapper']/div[2]/p[5]/button")
        self.click(pay_now_button)

    # 测试
    def pay_qiye_vip(self, i, vip_level):
        print("\ni=", i, "vip_level:", vip_level)
        returnValue = []
        pay_now_button = ('xpath', "//div[@class='product-wrapper']/div[" + str(i) + "]/p[5]/button")

        '''
           判断用户企业等级身份,老板本：7，8，9，10，
           新版本 37，38
           如果是7，37则可以点击基础协作版本与高级协作版本
           如果 8，38 则可以点击高级协作版本
           如果 9，10 基础协作版本与高级协作版本都不可点击
        '''

        if vip_level == 7 or vip_level == 37:
            if i == 1 or i == 2:
                self.ptclick(pay_now_button)
                self.window(-1)
                self.sleep()
                if vip_level == 7:
                    switchOtherVersion = ('xpath', "//div[@class='current-version-box']/span")
                    self.click(switchOtherVersion)
                self.sleep()
                for j in range(1, 3):
                    print("j=", j)
                    element = ('xpath', "//div[@class='product-list']/div[" + str(j) + "]")
                    self.ptclick(element)
                    if self.getElementAttr(element, "class") == "product-list-item select":
                        moneyeElement = ('xpath', "//div[@class='product-list']/div[" + str(j) + "]/h1")
                        moneyText = self.getText(moneyeElement)
                        money = moneyText[:-3]
                        payMoneyElemnt = ('xpath', "//div[@class='select-price-wrapper-right']/h1")
                        payMoneyText = self.getText(payMoneyElemnt)
                        payMoney = payMoneyText[1:]
                        returnValue.append(money)
                        returnValue.append(payMoney)
                        self.sleep()
                self.ptclick(('xpath', "//div[@class='modal_mask']/div[1]/span"))  # 关闭弹框
            elif i == 3:
                zixunElement = ('xpath', "//div[@class='product-wrapper']/div[3]/p[4]/button")
                self.click(zixunElement)
                self.sleep()
                self.edit_qiye_contact_information()
                value = self.get_add_succ_tips()
                returnValue.append(value)

        if vip_level == 8 or vip_level == 38:
            if i == 1:
                pay_now_button_attr = self.getElementAttr(pay_now_button, 'disabled')
                returnValue.append(pay_now_button_attr)
            elif i == 2:
                self.ptclick(pay_now_button)
                self.window(-1)
                self.sleep()
                if vip_level == 8:
                    switchOtherVersion = ('xpath', "//div[@class='current-version-box']/span")
                    self.click(switchOtherVersion)
                self.sleep()
                element = ('xpath', "//div[@class='product-list']/div[" + str(i) + "]")
                if self.getElementAttr(element, "class") == "product-list-item select":
                    moneyeElement = ('xpath', "//div[@class='product-list']/div[" + str(i) + "]/h1")
                    moneyText = self.getText(moneyeElement)
                    money = moneyText[:-3]
                    payMoneyElemnt = ('xpath', "//div[@class='select-price-wrapper-right']/h1")
                    payMoneyText = self.getText(payMoneyElemnt)
                    payMoney = payMoneyText[1:]
                    returnValue.append(money)
                    returnValue.append(payMoney)
                    self.ptclick(('xpath', "//div[@class='modal_mask']/div[1]/span"))  # 关闭弹框
            elif i == 3:
                time.sleep(2)
                zixunElement = ('xpath', "//div[@class='product-wrapper']/div[3]/p[4]/button")
                self.click(zixunElement)
                self.sleep()
                self.edit_qiye_contact_information()
                value = self.get_add_succ_tips()
                returnValue.append(value)
            else:
                print("i值不对")

        if vip_level == 9 or vip_level == 10:
            if i == 1 or i == 2:
                pay_now_button_attr = self.getElementAttr(pay_now_button, 'disabled')
                returnValue.append(pay_now_button_attr)

            if i == 3:
                zixunElement = ('xpath', "//div[@class='product-wrapper']/div[3]/p[4]/button")
                self.click(zixunElement)
                self.sleep()
                self.edit_qiye_contact_information()
                value = self.get_add_succ_tips()
                returnValue.append(value)
        print("returnValue=", returnValue)
        return returnValue

    # =============================testcase=============================

    # 进入企业VIP页面获取标识
    def test_get_into_qiyeVip(self):
        self.click_ent_vip()
        text = self.getQiyeVipContent()
        self.sleep()
        # self.close_and_home_page()
        assert text == "开通企业版"

    # 测试添加开通企业版提交成功提示
    def test_open_qiye(self):
        '''开通企业VIP添加联系方式'''
        # self.click_ent_vip()
        self.click_qiye_button()  # 点击开通企业版
        self.edit_qiye_contact_information()  # 编写开通企业版填写联系方式
        tips = self.get_add_succ_tips()
        self.sleep(2)
        # self.close_and_home_page()
        assert tips == "操作成功"

    # 测试点击进入企业版
    def test_click_get_qiye_button(self):
        tips = "我的空间,操作成功"
        # self.click_ent_vip()
        text = self.get_into_qiye()  # 进入企业版按钮
        self.sleep(3)
        self.close_and_home_page()
        assert text in tips

    # 验证打开企业VIP支付价格是否正确
    def test_qiye_pay_money(self):
        self.click_ent_vip()
        userInfo = self.getUserInfo()
        vip_level = userInfo['data']['company_vip_level']
        for i in range(1, 4):
            money = self.pay_qiye_vip(i, vip_level)
            if money != []:
                if i == 1:
                    if vip_level in [7, 37]:
                        assert money[0] == money[1]
                    elif vip_level in [8, 9, 10, 38]:
                        assert money[0] == "true"
                if i == 2:
                    if vip_level in [7, 37]:
                        assert money[0] == money[1]
                    elif vip_level in [9, 10]:
                        assert money[0] == "true"
                if i == 3:
                    assert money[0] == "操作成功"
            else:
                assert False
