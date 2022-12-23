from pages.basePage import Action
from common.interface import Interface
from common.readLog import Log
from common.sendDingTalk import SendDingTalk


# =======================================
# 爱设计个人VIP页面
# https://www.isheji.com/vip
# =======================================

class PersonalVip(Action):
    log = Log(__name__)
    logger = log.getLog()

    # 获取用户VIP身份
    def getUserVip(self):
        user = []
        is_vip = 0
        vip_type = 0
        company_vip_end_time = ""
        company_vip_level = 0
        try:
            userInfo = Interface().getUserInfo()
            self.sleep(2)
            is_vip = userInfo['data']['is_vip']
            vip_type = userInfo['data']['vip_type']
            try:
                company_vip_end_time = userInfo['data']['company_vip_end_time']
            except:
                company_vip_end_time = ""
            try:
                company_vip_level = userInfo['data']['company_vip_level']
            except:
                company_vip_level = 0
        except Exception as e:
            self.logger.error("用户身份信息获取异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在个人VIP页面获取用户信息失败，请立即查看")
        # append 向后加，不要向前加，否则影响后面的判断
        user.append(is_vip)  # 是否会员
        user.append(vip_type)  # 普通/终身
        user.append(company_vip_end_time)  # 企业会员到期日期
        if company_vip_level == "":
            company_vip_level = 0
        user.append(company_vip_level)  # 企业会员等级
        print(user)
        return user

    # 点击个人VIP tab

    def clickPersonalVip(self):
        try:
            cvip = ('xpath', "//a[contains(text(),'个人VIP')]")
            self.ptclick(cvip)
        except Exception as e:
            try:
                cvip = ('xpath', "//ul[@id='menulist']/li[1]")
                self.ptclick(cvip)
            except Exception as e:
                self.logger.error("点击导航的个人VIP菜单异常%s" % repr(e))
                SendDingTalk().sendDingTalkMsg("点击导航的个人VIP菜单失败")
                raise e

    # 实际需要支付金额
    def getPayMoney(self):
        try:
            payMoneyElement = ('xpath', "//span[@class='amount-paid-price']")  # 微信支付金额
            return self.getText(payMoneyElement)
        except Exception as e:
            self.logger.error("在个人VIP页面获取支付价格异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在个人VIP页面获取支付价格失败")
            raise e

    # 关闭支付弹窗
    def closePayFrame(self):
        closedBtn = ('xpath', "//span[contains(@class,'iconfont icon-no close_button')]")
        self.click(closedBtn)

    # 点击终身VIP的立即开通【立即续费】
    def clickLifeLongBtn(self):
        try:
            lifelong = ('xpath', "//div[@data-name='lifelong_vip_upgrade_pv']")
            self.click(lifelong)
        except:
            try:
                lifelong = ('xpath', "//div[@data-name='eight_lifelong_vip_renew_pv']")
                self.click(lifelong)
            except:
                try:
                    lifelong = ('xpath', "//li[@class='bottom-introduce-card bottom-introduce-card-zhengs']/div[4]")
                    self.click(lifelong)
                except Exception as e:
                    self.logger.error("在个人VIP页面点击终身VIP按钮异常%s" % repr(e))
                    SendDingTalk().sendDingTalkMsg("在个人VIP页面点击终身VIP按钮失败")
                    raise e

    # 点击开通企业VIP按钮
    def clickEnterpriseBtn(self):
        try:
            enterprise = ('xpath', "//div[@data-mark='企业标准版立即升级pv']")
            self.click(enterprise)
        except:
            enterprise = ('xpath', "//div[@data-mark='企业标准版立即续费pv']")
            self.click(enterprise)

    # 获取企业VIP原价值
    def getEnterpriseBtnText(self):
        try:
            enterprise = ('xpath', "//div[@data-mark='企业标准版立即升级pv']")
            text = self.getText(enterprise)
        except:
            enterprise = ('xpath', "//div[@data-mark='企业标准版立即续费pv']")
            text = self.getText(enterprise)
        return text

    # 点击终身VIP支付弹窗
    def getLifeLongVipText(self):
        value = []
        try:
            user = self.getUserVip()
            self.sleep(2)
            # user[1]代表vip_type,值为2时终身VIP
            if user[0] == 1 and user[1] == 2:
                self.clickLifeLongBtn()
                tips = self.errorTips()
                value.append(tips)
            else:
                self.clickLifeLongBtn()
                lifeLongCard = ('xpath', "//ul[@class='payContent-card']/li[1]")
                attr = self.getElementAttr(lifeLongCard, "class")
                if attr == "payContent-card-price  card-selected":  # 终身会员呈现选中状态
                    lifeLongCard_text = ('xpath', "//ul[@class='payContent-card']/li[1]/h5")
                    vipText = self.getText(lifeLongCard_text)#终身会员
                    showMoney = self.getShowLifeLongMoney()
                    payMoney = self.getPayMoney()
                    value.append(vipText)
                    value.append(showMoney)
                    value.append(payMoney)
                    self.closePayFrame()
            return value
        except:
            return value

    # 显示终身会员价格
    def getShowLifeLongMoney(self):
        #moneyTipsElement = ('xpath', "//ul[@class='payContent-card']/li[1]/p/span")  # 卡片的支付金额
        moneyTipsElement = ('xpath', "//ul[@class='payContent-card']/li[1]/div/section[2]/span")
        return self.getText(moneyTipsElement)

    # 点击右箭头
    def clickRightArrow(self):
        arrowElement = ('xpath', "//div[@class='payContent']/div[2]/span")
        self.click(arrowElement)

    # 无法购买提示
    def errorTips(self):
        tips = ""
        try:
            tipsElement = ('xpath', "//div[@class='permanent-texttip']")
            # tips = self.getText(tipsElement)
            tips = "已是终身会员"
            print("点击按钮弹窗的提示:", tips)
        except Exception as e:
            tips = ""
        return tips

    # 操作开通月，季，年 VIP
    def openPerVip(self, i):
        value = None
        returnValue = []
        try:
            self.sleep(2)
            # 点击立即升级按钮
            upgradeBbutton = ('xpath', "//ul[@class='qiul']/li[" + str(i) + "]/div[2]")
            # self.ptclick(button)
            # 如果是终身vip，则从接口获取
            user = self.getUserVip()
            self.sleep(2)
            if (user[0] == 1 and user[1] == 2):
                self.sleep(1)
                self.click(upgradeBbutton)
                tips = self.errorTips()
                returnValue.append(tips)
            else:
                self.click(upgradeBbutton)
                # 如果循环到3，需要点击又滑按钮 暂时不用
                # if i == 3:
                #     self.clickRightArrow()
                # 获取选项卡是否被选中
                self.sleep(2)
                yearVipCard = ('xpath', "//ul[@class='payContent-card']/li[" + str(i + 1) + "]")
                attr = self.getElementAttr(yearVipCard, "class")
                if i == 1:
                    if attr == "payContent-card-price biaozun card-selected":  # 年会员呈现选中状态
                        vipCard_text = ('xpath', "//ul[@class='payContent-card']/li[" + str(i + 1) + "]/h5")
                        value = self.getText(vipCard_text)
                else:
                    if attr == "payContent-card-price  card-selected" or attr == "payContent-card-price card-selected":
                        vipCard_text = ('xpath', "//ul[@class='payContent-card']/li[" + str(i + 1) + "]/h5")
                        value = self.getText(vipCard_text)
                moneyTipsElement = ('xpath', "//ul[@class='payContent-card']/li[" + str(i + 1) + "]/div/section[2]/span")  # 卡片的支付金额
                self.sleep(1)
                showMoney = self.getText(moneyTipsElement)
                self.sleep()
                payMoney = self.getPayMoney()
                returnValue.append(value)
                returnValue.append(showMoney)
                returnValue.append(payMoney)
                self.closePayFrame()
        except Exception as e:
            returnValue = []
        return returnValue

    # 查看企业VIP支付弹窗页面
    def enterpriseVipView(self, text, i):
        returnValue = []
        value = None
        if i < 4:
            vipCard = ('xpath', "//ul[@class='payContent-card']/li[" + str(i) + "]")
            self.click(vipCard)
            self.sleep(2)
            attr = self.getElementAttr(vipCard, "class")
            self.logger.info("在企业VIP支付弹框上获取到的属性%s" % attr)
            self.sleep(2)
            # 根据身份需要判断立即开通:payContent-card-price  card-selected:
            if str(text).strip() == "立即续费":
                if attr == "payContent-card-price payContent-company  card-selected" or attr == "payContent-card-price payContent-company card-selected":
                    self.logger.info("在企业VIP支付弹框上获取到的属性预期一致")
                    flag = True
                else:
                    self.logger.info("在企业VIP支付弹框上获取到的属性预期不一致")
                    flag = False
            elif str(text).strip() == "立即开通":
                # if attr == "payContent-card-price  card-selected":
                if attr == "payContent-card-price payContent-company card-selected":
                    self.logger.info("在企业VIP支付弹框上获取到的属性预期一致")
                    flag = True
                else:
                    self.logger.info("在企业VIP支付弹框上获取到的属性预期不一致")
                    flag = False
            else:
                self.logger.info("开通企业VIP按钮既不是立即开通，也不是立即续费")
                flag = False
            if flag == True:
                vipCard_text = ('xpath', "//ul[@class='payContent-card']/li[" + str(i) + "]/h5")
                value = self.getText(vipCard_text)
            else:
                value = None
            # 卡片的支付金额 使用了flex修饰无法定位
            if value != None:
                moneyTipsElement = ('xpath', "//ul[@class='payContent-card']/li[" + str(i) + "]")
                showMoney = self.getElementAttr(moneyTipsElement, "data-prize")
                # self.sleep()
                # showMoneyText = self.getText(moneyTipsElement) # Flex的获取不到值
                # showMoney = showMoneyText[:-3]
                self.sleep()
                payMoney = self.getPayMoney()
                returnValue.append(value)
                returnValue.append(showMoney)
                returnValue.append(payMoney)
            else:
                returnValue = []
        if i == 4:
            self.clickRightArrow()  # 点击右滑按钮
            self.sleep(1)
            service = ('xpath', "//ul[@class='payContent-card']/li[4]/div[2]")
            self.click(service)  # 点击咨询按钮
            tipsElement = ('xpath', "//p[@class='upgrade-text']")
            tips = self.getText(tipsElement)  # 获取点击咨询按钮弹出的页面提示信息
            self.sleep(2)
            returnValue.append(tips)
            closeBtnElement = ('xpath', "//button[@aria-label='Close']")
            self.click(closeBtnElement)  # 关闭咨询弹框
            self.closePayFrame()  # 关闭支付弹框
        return returnValue

    # 点击开通企业VIP按钮
    def openEnterpriseVip(self, i):
        returnValue = []
        value = None
        text = self.getEnterpriseBtnText()
        # text = "立即续费，立即开通"
        self.clickEnterpriseBtn()  # 点击立即续费/立即升级按钮
        userInfo = self.getUserVip()
        if int(userInfo[3]) > 7:
            # 如果购买过比基础版本高的进行提示
            tips = self.errorTips()
            returnValue.append(tips)
        else:
            returnValue = self.enterpriseVipView(text, i)
            self.closePayFrame()  # 关闭VIP支付弹框
        return returnValue

    # 在支付弹窗获取个人VIP与企业VIP属性
    def getVipTabAttr(self):
        tabElement = ('xpath', "//div[@class='vipTab']/div[2]")  # div[2]是企业，1是个人
        return self.getElementAttr(tabElement, "class")

    # 在支付弹窗点击个人VIP与企业VIP
    def clickVipTab(self, i):
        tabElement = ('xpath', "//div[@class='vipTab']/div[" + str(i) + "]")  # div[2]是企业，1是个人
        self.click(tabElement)

    # 打开企业VIP支付弹框，切换vip tab
    def switchVipTab(self):
        value = None
        returnValue = []
        userInfo = self.getUserVip()
        qiyeVipType = int(userInfo[3])
        if qiyeVipType > 7:
            self.clickEnterpriseBtn()
            value = self.errorTips()
            returnValue.append(value)
        else:
            for j in range(0, 2):
                if userInfo[3] == 7 or userInfo[3] == 0:
                    self.clickEnterpriseBtn()
                    if userInfo[3] == 7:
                        text = "立即续费"
                    else:
                        text = "立即开通"
                    qiye = self.getVipTabAttr()
                    if qiye == "company tab-selected":  # 在企业VIP Tab下
                        # 默认在企业VIPtab下
                        '''
                          默认在企业VIP Tab下
                          切换到个人VIP执行
                        '''
                        self.clickVipTab(1)  # 进入到个人VIP
                        self.sleep(2)
                        if int(userInfo[0] == 1 and userInfo[1] == 2):
                            qrcodeElement = ('xpath', "//div[@id='qrcode']/div")
                            value = self.getText(qrcodeElement)
                            returnValue.append(value)
                        else:
                            for i in range(1, 5):

                                if i == 3:
                                    self.clickRightArrow()  # 右滑
                                    # 获取选项卡是否被选中
                                yearVipCard = ('xpath', "//ul[@class='payContent-card']/li[" + str(i) + "]")
                                self.click(yearVipCard)
                                self.sleep()
                                attr = self.getElementAttr(yearVipCard, "class")
                                if i == 2:
                                    if attr == "payContent-card-price biaozun card-selected":  # 年会员呈现选中状态
                                        vipCard_text = ('xpath', "//ul[@class='payContent-card']/li[" + str(i) + "]/h5")
                                        value = self.getText(vipCard_text)
                                else:
                                    if attr == "payContent-card-price  card-selected":
                                        vipCard_text = ('xpath', "//ul[@class='payContent-card']/li[" + str(i) + "]/h5")
                                        value = self.getText(vipCard_text)
                                moneyTipsElement = (
                                    'xpath', "//ul[@class='payContent-card']/li[" + str(i) + "]/p/span")  # 卡片的支付金额
                                self.sleep()
                                showMoney = self.getText(moneyTipsElement)
                                self.sleep()
                                payMoney = self.getPayMoney()
                                returnValue.append(value)
                                returnValue.append(showMoney)
                                returnValue.append(payMoney)

                    # 循环到第二次 此时企业VIP tab 属性值为company
                    elif qiye == "company":
                        # 默认在个人VIP下
                        self.clickVipTab(2)  # 进入到企业VIP
                        for i in range(1, 5):  # 打开支付页面循环里面的产品类型
                            returnValue = self.enterpriseVipView(text, i)
        return returnValue

    # 倒计时
    def timeCountdown(self):
        num = []
        hourElement = ('xpath', "//ul[@class='countDown']/li[2]")  # 倒计时时间
        hour = self.getText(hourElement)
        self.sleep(1)
        minuteElement = ('xpath', "//ul[@class='countDown']/li[4]")  # 倒计时时间
        minute = self.getText(minuteElement)
        self.sleep(1)
        secondElement = ('xpath', "//ul[@class='countDown']/li[6]")  # 倒计时时间
        second = self.getText(secondElement)
        num.append(hour)
        num.append(minute)
        num.append(second)
        return num

    # 立即升级
    def upgradeNow(self):
        updateNow = ('xpath', "//div[@class='ljsj']")
        self.click(updateNow)

    # 开通VIP，设计更轻松
    def easierDesign(self):
        ed = ('xpath', "//div[@class='ktvip-btn']")
        self.click(ed)

    # 放心商用
    def business(self):
        business = ('xpath', "//div[@class='gmbtn' and contains(text(),'立即升级 放心商用')]")
        self.click(business)

    # 立即购买，报销无忧
    def buyNow(self):
        buynow = ('xpath', "//div[@class='gmbtn' and contains(text(),'立即购买 报销无忧')]")
        self.click(buynow)

    # =============================
    # 执行测试方法
    # =============================

    # 打开终身会员弹框，终身会员价格是否正确
    def test_clickLifeLongBtn(self):
        try:
            '''打开终身会员弹框，终身会员价格是否正确'''
            self.logger.info("开始测试在个人VIP页面点击开通终身VIP功能")
            value = self.getLifeLongVipText()
            self.logger.info("在test_clickLifeLongBtn方法中得到的value值为：%s" % value)
            userVip = self.getUserVip()
            self.sleep(3)
            if userVip[0] == 1 and userVip[1] == 2:
                try:
                    assert value[0] == "您已是爱设计终身VIP，快去享受专属特权吧"
                except:
                    SendDingTalk().sendDingTalkMsg("终身VIP用户点击开通终身VIP功能失败")
            else:
                if value != []:
                    if value[0] == "终身会员" and value[1] == value[2]:
                        assert True
                else:
                    SendDingTalk().sendDingTalkMsg("非终身VIP用户点击开通终身VIP功能失败")
                    assert False
        except Exception as e:
            self.logger.error("终身VIP用户点击开通终身VIP功能失败%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("终身VIP用户点击开通终身VIP功能失败")
            raise e

    # 测试开通个人VIP
    def test_openPerVip(self):
        '''打开年，季，月会员弹框，价格是否正确'''
        self.logger.info("开始测试在个人VIP页面点击开通终身、两年、年功能")
        try:
            for i in range(1, 4):
                try:
                    value = self.openPerVip(i)
                    self.logger.info("在test_openPerVip()方法中得到的value值为：%s" % value)
                    if value != []:
                        userVip = self.getUserVip()
                        self.sleep(2)
                        if userVip[0] == 1 and userVip[1] == 2:
                            try:
                                assert value[0] == "您已是爱设计终身VIP，快去享受专属特权吧"
                            except:
                                SendDingTalk().sendDingTalkMsg("终身VIP用户点击开通终身、两年、年功能失败")
                        else:
                            if i == 1:
                                if value[0] == "终身会员":
                                    self.logger.info("在test_openPerVip()方法中 循环到1的时候，得到的值为：%s%s %s" % (value[0], value[1], value[2]))
                                    assert value[1] == value[2]
                            elif i == 2:
                                if value[0] == "两年会员":
                                    self.logger.info(
                                        "在test_openPerVip()方法中 循环到2的时候，得到的值为：%s%s %s" % (value[0], value[1], value[2]))
                                    assert value[1] == value[2]
                            elif i == 3:
                                if value[0] == "年享会员":
                                    self.logger.info(
                                        "在test_openPerVip()方法中 循环到3的时候，得到的值为为：%s%s %s" % (value[0], value[1], value[2]))
                                    assert value[1] == value[2]
                            else:
                                SendDingTalk().sendDingTalkMsg("非终身VIP用户点击开通终身、两年、年功能失败")
                                assert False
                    else:
                        SendDingTalk().sendDingTalkMsg("用户点击开通终身、两年、年功能失败")
                        assert False
                except Exception as e:
                    self.logger.error("打开个人VIP支付弹框抛出了异常%s" % repr(e))
                    continue
        except Exception as e:
            self.logger.error("打开个人VIP支付弹框抛出了异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("用户点击开通终身、两年、年功能失败")
            raise e

    # 测试开通个人VIP
    def test_openEntVip(self):
        '''打开企业会员弹框，价格是否正确'''
        self.logger.info("开始测试在个人VIP页面点击开通企业VIP功能")
        self.sleep()
        try:
            for i in range(1, 5):
                try:
                    user = self.getUserVip()  # 获取用户信息
                    value = self.openEnterpriseVip(i)  # 调用打开vip弹窗方法
                    if value != []:
                        if user[3] > 7:
                            try:
                                assert value[0] == "您已是爱设计高级协作版VIP，快去享受专属特权吧"
                            except:
                                SendDingTalk().sendDingTalkMsg("用户点击开通企业会员功能失败")
                            break
                        else:
                            if i == 1:
                                if value[0] == "标准版":
                                    assert value[1] == value[2]
                                else:
                                    SendDingTalk().sendDingTalkMsg("企业VIP标准版获取的值不正确")
                                    assert False, "企业VIP标准版获取的值不正确"
                            elif i == 2:
                                if value[0] == "基础协作版":
                                    assert value[1] == value[2]
                                else:
                                    SendDingTalk().sendDingTalkMsg("企业VIP基础协作版获取的值不正确")
                                    assert False, "企业VIP基础协作版获取的值不正确"
                            elif i == 3:
                                if value[0] == "高级协作版":
                                    assert value[1] == value[2]
                                else:
                                    SendDingTalk().sendDingTalkMsg("企业VIP高级协作版获取的值不正确")
                                    assert False, "企业VIP高级协作版获取的值不正确"
                            else:
                                try:
                                    assert value[0] == "微信扫码联系专属顾问进行咨询"
                                except:
                                    SendDingTalk().sendDingTalkMsg("打开咨询弹框获取的值不正确")
                except Exception as e:
                    continue
        except Exception as e:
            self.logger.error("打开企业会员弹框，价格异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("打开企业会员弹框，价格失败")
            raise e

    # 在支付弹框切换企业和个人tab
    def test_switchVipTab(self):
        self.logger.info("开始测试在个人VIP页面支付弹框切换到商户VIP功能")
        userInfo = self.getUserVip()
        value = self.switchVipTab()
        self.logger.info("执行切换个人企业VIP弹框获取的值：%s" % value)
        if value != []:
            if int(userInfo[3]) > 7:
                assert "快去享受专属特权吧" in value[0]
            else:
                assert value[0] == "微信扫码联系专属顾问进行咨询"

    # 倒计时
    def test_timeCountdown(self):
        try:
            self.logger.info("开始测试在个人VIP页面获取倒计时功能")
            num = 0
            self.page_down(1000)
            value = self.timeCountdown()
            self.logger.info("在个人VIP页面获取倒计时的值为：%s" % value)
            for i in range(value.__len__()):
                num = num + int(value[i])
            self.logger.info("在个人VIP页面获取倒计时的值num值为：%d" % num)
            try:
                assert num > 0
            except:
                SendDingTalk().sendDingTalkMsg("在个人VIP页面获取倒计时值失败")
        except Exception as e:
            self.logger.error("在VIP页面获取倒计时异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在VIP页面点获取倒计时失败")
            raise e


    # 立即升级
    def test_upgradeNow(self):
        try:
            value = ""
            self.logger.info("开始测试在个人VIP页面立即升级功能")
            user = self.getUserVip()
            self.sleep(2)
            self.page_down(1000)
            if user[0] == 1 and user[1] == 2:
                i = 0
                while i < 3:
                    self.upgradeNow()
                    self.sleep(0.5)
                    value = self.errorTips()
                    if value == "":
                        i=i+1
                    else:
                        break

                self.logger.info("终身会员用户在个人VIP页面点击【立即升级】按钮得到的提示%s" % value)
                try:
                    assert value == "您已是爱设计终身VIP，快去享受专属特权吧"
                except:
                    SendDingTalk().sendDingTalkMsg("终身会员用户在个人VIP页面点击【立即升级】按钮获取到的提示失败")
            else:
                self.upgradeNow()
                self.sleep(2)
                value = self.getPayMoney()
                self.closePayFrame()
                if value != None:
                    self.logger.info("用户在个人VIP页面点击【立即升级】按钮得到的支付金额%s" % value)
                    try:
                        assert float(value) > 0
                    except:
                        SendDingTalk().sendDingTalkMsg("用户在个人VIP页面点击【立即升级】按钮弹出的VIP弹框，获取到的支付价格错误")
        except Exception as e:
            self.logger.error("在VIP页面点击立即升级异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在VIP页面点击点击立即升级失败")
            raise e
    # 点击开通VIP，轻松设计
    def test_easierDesign(self):
        try:
            value = ""
            self.logger.info("开始测试点击【开通VIP，轻松设计】按钮")
            user = self.getUserVip()
            self.sleep(2)
            self.page_down(1200)
            if user[0] == 1 and user[1] == 2:
                i = 0
                while i < 3:
                    self.easierDesign()
                    self.sleep(0.5)
                    value = self.errorTips()
                    if value == "":
                        i=i+1
                    else:
                        break

                self.logger.info("终身会员用户在个人VIP页面点击【开通VIP，轻松设计】按钮得到的提示%s" % value)
                try:
                    assert value == "您已是爱设计终身VIP，快去享受专属特权吧"
                except:
                    SendDingTalk().sendDingTalkMsg("终身会员用户在个人VIP页面点击【开通VIP，轻松设计】按钮获取到的提示失败")
            else:
                self.easierDesign()
                self.sleep(2)
                value = self.getPayMoney()
                self.logger.info("用户在个人VIP页面点击【开通VIP，轻松设计】按钮弹出的VIP弹框，获取到的支付价格%s" % value)
                self.closePayFrame()
                try:
                    assert float(value) > 0
                except:
                    SendDingTalk().sendDingTalkMsg("用户在个人VIP页面点击【开通VIP，轻松设计】按钮弹出的VIP弹框，获取到的支付价格错误")
        except Exception as e:
            self.logger.error("在VIP页面点击开通VIP，轻松设计异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在VIP页面点击点击开通VIP，轻松设计失败")
            raise e
    # 放心商用
    def test_business(self):
        try:
            value = ""
            self.logger.info("开始测试在个人VIP页面【放心商用】功能")
            user = self.getUserVip()
            self.page_down(2000)
            if user[0] == 1 and user[1] == 2:
                i = 0
                while i < 3:
                    self.business()
                    self.sleep(0.5)
                    value = self.errorTips()
                    if value == "":
                        i=i+1
                    else:
                        break
                try:
                    assert value == "您已是爱设计终身VIP，快去享受专属特权吧"
                except:
                    SendDingTalk().sendDingTalkMsg("终身会员用户在个人VIP页面点击【放心商用】获取到的提示失败")
            else:
                self.business()
                self.sleep(2)
                value = self.getPayMoney()
                self.logger.info("用户在个人VIP页面点击【放心商用】按钮弹出的VIP弹框，获取到的支付价格%s" % value)
                self.closePayFrame()
                try:
                    assert float(value) > 0
                except:
                    SendDingTalk().sendDingTalkMsg("用户在个人VIP页面点击【放心商用】按钮弹出的VIP弹框，获取到的支付价格错误")
        except Exception as e:
            self.logger.error("在VIP页面点击放心商用异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在VIP页面点击放心商用失败")
            raise e
    # 立即购买，报销无忧
    def test_buyNow(self):
        try:
            value = ""
            self.logger.info("开始测试在个人VIP页面【立即购买，报销无忧】功能")
            user = self.getUserVip()
            self.page_down(2200)
            if user[0] == 1 and user[1] == 2:
                i = 0
                while i < 3:
                    self.buyNow()
                    self.sleep(0.5)
                    value = self.errorTips()
                    self.logger.info("获取到终身VIP提示:%s"%value)
                    if value == "":
                        i=i+1
                    else:
                        break
                try:
                    assert value == "您已是爱设计终身VIP，快去享受专属特权吧"
                except:
                    SendDingTalk().sendDingTalkMsg("终身会员用户在个人VIP页面点击【立即购买，报销无忧】获取到的提示失败")
            else:
                self.buyNow()
                self.sleep(2)
                value = self.getPayMoney()
                self.logger.info("用户在个人VIP页面点击【立即购买，报销无忧】按钮弹出的VIP弹框，获取到的支付价格%s" % value)
                self.closePayFrame()
                try:
                    assert float(value) > 0
                except:
                    SendDingTalk().sendDingTalkMsg("用户在个人VIP页面点击【立即购买，报销无忧】按钮弹出的VIP弹框，获取到的支付价格错误")
        except Exception as e:
            self.logger.error("在VIP页面点击立即购买，报销无忧异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在VIP页面点击立即购买，报销无忧失败")
            raise e
        finally:
            home_button = ("xpath", "//img[@class='logo']")
            self.click(home_button)
    def close_down_tip(self):
        '''今日不再提醒'''
        try:
            tip_button = ('xpath', "//span[@class='bottom_no_warn']")
            self.click(tip_button)
        except:
            self.logger.info('没有出现下方8折提醒框')

    # 打开商户VIP弹框
    def test_open_company(self):
        # 商户版立即开通
        try:
            open_div_xpath = ('xpath',"//div[@class='card-container']/ul/li[1]/div[2]")
            self.click(open_div_xpath)
            # 获取价格
            payMoney = self.getPayMoney()
            self.closePayFrame()
            assert payMoney =="399"
        except Exception as e:
            self.logger.error("在VIP页面点击开通商户VIP异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在VIP页面点击开通商户VIP失败")
            raise e


    # 打开商户VIP弹框,切换到个人VIP
    def test_per_company(self):
        # 商户版立即开通
        try:
            open_div_xpath = ('xpath',"//div[@class='card-container']/ul/li[1]/div[2]")
            self.click(open_div_xpath)
            # 获取价格
            payMoney = self.getPayMoney()
            if payMoney == "399":
                # 切换到个人vip
                switch_per_xpath = ('xpath',"//div[@class='viptype-tabitem vip']")
                self.click(switch_per_xpath)
                money = self.getPayMoney()
                self.closePayFrame()
                assert float(money) > 0
        except Exception as e:
            self.logger.error("在VIP页面由商户VIP切换到个人VIP异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在VIP页面由商户VIP切换到个人VIP失败")
            raise e
