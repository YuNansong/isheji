'''
    企业登录页面
'''
class EntLoginElement:
    loginBtn = ('xpath',"//div[@class='info']/div[2]")
    username_xpath = ('xpath',"//input[@placeholder='请输入手机号']")
    password_xpath = ('xpath',"//input[@placeholder='请输入密码']")
    errorUsername = ('xpath',"//input[@placeholder='请输入手机号']/ancestor-or-self::div[@class='el-form-item__content']/div[2]")
    errorPassword = ('xpath',"//input[@placeholder='请输入密码']/ancestor-or-self::div[@class='el-form-item__content']/div[2]")
    tipsError_xpath = ('xpath',"//p[@class='el-message__content']")
    sureLogin_xpath = ('xpath',"//button/span[contains(text(),'登录')]")
    email_xpath = ('xpath',"//div[contains(text(),'邮箱')]")
    input_email_xpath = ('xpath',"//input[@placeholder='请输入邮箱地址']")
    errorEmail = ('xpath',"//input[@placeholder='请输入邮箱地址']/ancestor-or-self::div[@class='el-form-item__content']/div[2]")


