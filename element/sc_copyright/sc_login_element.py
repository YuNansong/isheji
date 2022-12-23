class SCLoginElement:
    tel_phone_element = ('xpath',"//div[@class='login-way-font' and contains(text(),'账号密码登录')]")
    phone_element =  ('xpath',"//div[@class='phone-chang-bar']//button[1]//span[1]") # 登录页面的手机密码登录
    usname_element = ('xpath',"//input[@placeholder='请输入手机号']") # 登录页面的手机号输入框
    psword_element = ('xpath',"//input[@placeholder='请输入密码']") # 登录页面的密码输入框
    login_button_element = ('xpath',"//span[contains(text(),' 登录 ')]") # 登录页面的登录按钮