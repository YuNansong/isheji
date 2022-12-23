from pages.basePage import Action
from pages.isheji_c.homePage.homePage import HomePage
from common.sendDingTalk import SendDingTalk
from common.readLog import Log


class Cooperation(Action):
    log = Log(__name__)
    logger = log.getLog()

    # 在合作页面增加联系方式信息
    def test_addServiceProvider(self):
        try:
            self.page_down()  # 将页面滑到底部
            enterpriseNameElement = ('xpath', "//div[@id='applyForm']/form/div[1]//input")
            self.write(enterpriseNameElement, "测试企业名称")
            self.sleep(1)
            nameElement = ('xpath', "//div[@id='applyForm']/form//input[@placeholder='输入姓名']")
            self.write(nameElement, "测试姓名")
            jobElement = ('xpath', "//div[@id='applyForm']/form//input[@placeholder='请输入职位']")
            self.write(jobElement, "测试职位")
            phoneElement = ('xpath', "//div[@id='applyForm']/form//input[@placeholder='请输入手机号']")
            self.write(phoneElement, "13211112222")
            emailElement = ('xpath', "//div[@id='applyForm']/form//input[@placeholder='请输入电子邮箱']")
            self.write(emailElement, "aa@test.com")
            self.sleep(1)
            problemElement = ('xpath', "//div[@id='applyForm']/form//input[@placeholder='如何让设计师从重复修改中解脱出来？']")
            self.write(problemElement, "测试问题")
            submitElement = ('xpath', "//span[contains(text(),'提交')]")
            self.ptclick(submitElement)
            self.sleep(1)
            tipsElement = ('xpath', "//p[@class='el-message__content']")
            tips = self.getText(tipsElement)
            assert tips == "操作成功"
        except Exception as e:
            self.logger.error("在合作页面增加信息异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在合作页面增加联系方式信息失败")
            raise e

    # 在合作页面，点击个人VIP悬浮层的开通VIP
    def test_open_per_vip(self, driver):

        HomePage(driver).test_open_per_vip_floating_layer(driver)
