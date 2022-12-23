from pages.basePage import Action
from element.ent.entLoginElement import EntLoginElement

class EntLoginModel(Action):

    # 点击企业首页登录注册按钮
    def click_loginBtn(self):
        self.click(EntLoginElement.loginBtn)

    # 输入手机号
    def input_userName(self,username):
        self.click(EntLoginElement.username_xpath)
        self.write(EntLoginElement.username_xpath,username)
    # 输入密码
    def input_password(self,password):
        self.click(EntLoginElement.password_xpath)
        self.write(EntLoginElement.password_xpath,password)

    # 邮箱tab
    def click_email_tab(self):
        self.click(EntLoginElement.email_xpath)
        self.sleep(2)

    # 输入邮箱地址
    def input_email(self,email):
        self.write(EntLoginElement.input_email_xpath,email)

    # 清空输入框
    def clear_userName(self):
        self.clear(EntLoginElement.username_xpath)
    # 清空密码框
    def clear_password(self):
        self.clear(EntLoginElement.password_xpath)

    #  用户名文本输入错误提示
    def error_userName(self):
        return self.getText(EntLoginElement.errorUsername)

    #  邮箱地址文本输入错误提示
    def error_email(self):
        return self.getText(EntLoginElement.errorEmail)

    # 密码框输入错误提示
    def error_password(self):
        return self.getText(EntLoginElement.errorPassword)

    # 接口返回的错误
    def get_tips_error(self):
        return self.getText(EntLoginElement.tipsError_xpath)

    # 登录按钮
    def sureLogin(self):
        self.click(EntLoginElement.sureLogin_xpath)
        self.sleep(1)