class LoginElement:
    login_phone_element = ('xpath', "//li[@class='login-phone']")  # 登录页面的手机号登录
    phone_pwd_element = ('xpath', "//a[@class='phone-login']")# 手机密码登录
    usname_element = ('id', 'land-tel')  # 登录页面的手机号输入框
    psword_element = ('id', 'land-pwd')  # 登录页面的密码输入框
    login_button_element = ('xpath', "//button[@class='login-btn purple-btn']")  # 登录页面的手登录按钮
