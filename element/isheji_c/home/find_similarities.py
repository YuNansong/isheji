class FindSimilarities:
    first_template = ("xpath", "//div[@class='swiper-wrapper line5']/div[1]/div[@class='swiper-loading swiper-loading63']")#首页第一个模板
    similarutues_button = ("xpath", "//div[@class='swiper-wrapper line5']/div[@class='swiper-slide card swiper-slide63 swiper-slide-active']//div[@class='jbalert-box']/div[3]")#找相似按钮
    similarutues_str = ("xpath", "//*[@id='apptc']/div[23]/div/div[1]/span")#找相似三个字的位置
    find_first_template = ("xpath", "//div[@class='similar__templates']//div[1]//div[1]//div[1]//div[1]//div[1]//img[1]")#找相似中的第一个模板
    username_assert = ("xpath", "//li[@class='login-phone']//p")#账号密码登录
    login_x_button = ("xpath", "//span[@class='iconfont icon-no close_button']")#关闭登录窗口