class EntBrandElement:
    brandManage_xpath = ('xpath',"//div[@class='nav-title']/div/h2") # 品牌管理页面
    # 上传logo
    brandInputLogo_xpath = ('xpath', "//input[@name='file']")
    logo_li_xpath = ('xpath',"//li[@class='logo-li']")
    last_logo_li_xpath = ('xpath',"//li[@class='logo-li'][last()]") # 最后一个logo
    last_logo_li_more_xpath = ('xpath',"//li[@class='logo-li'][last()]/div/span") # 更多
    last_logo_li_del_xpath = ('xpath',"//li[@class='logo-li'][last()]/div/div/p[contains(text(),'删除')]") # 删除logo
    last_logo_li_del_button_xpath = ('xpath',"//div[@aria-label='是否确认删除该LOGO']//button[2]") # 确认删除

    # 重命名logo
    last_logo_li_name = ('xpath',"//li[@class='logo-li'][last()]//p[@class='text-hidden']")# 获取logo名称
    last_logo_li_rename_xpath = ('xpath',"//li[@class='logo-li'][last()]/div/div/p[contains(text(),'重命名')]") # 删除logo
    rename_logo_xpath = ('xpath',"//input[@placeholder='请输入名称']")
    last_logo_li_rename_button_xpath = ('xpath',"//div[@aria-label='重命名']//button[2]") # 确认重命名
    # 下载logo
    last_logo_li_download_xpath = ('xpath',"//li[@class='logo-li'][last()]/div/div/p[contains(text(),'下载')]") # 删除logo

    # 颜色
    add_coloer = ('xpath',"//p[contains(text(),'添加新颜色')]")
    one_input = ('xpath', "//div[@class='rgb-input']//div[1]//input[1]")
    two_input = ('xpath', "//div[@class='rgb-input']//div[2]//input[1]")
    three_input = ('xpath', "//div[@class='rgb-input']//div[3]//input[1]")
    commit_button = ('xpath', "//div[@class='color-btn-wrap']/button[2]")
    # 获取颜色个数
    color_num = ('xpath',"//div[@class='brand-color']//li[contains(@style,'background-color')]")

    # 最后一个颜色
    last_color_li_xpath = ('xpath',"//div[@class='brand-color']//li[contains(@style,'background-color')][last()]")
    last_color_li_more_xpath = ('xpath',"//div[@class='brand-color']//li[contains(@style,'background-color')][last()]/div[1]/span[2]")
    last_color_li_name_xpath = ('xpath',"//div[@class='brand-color']//li[contains(@style,'background-color')][last()]/div[1]/span[1]")
    last_color_li_del_xpath = ('xpath',"//div[@class='brand-color']//li[contains(@style,'background-color')][last()]/div[2]/p")
    sure_del_button_xpath = ('xpath',"//div[@aria-label='是否确认删除该颜色']//button[2]") # 确定删除color

    # 字体
    font_li_num = ('xpath',"//div[@class='brand-font']//li[@class='font-li']")
    upload_font_xpath = ('xpath', "//div[@class='brand-font']//div[@class='logo-uploader']")
    select_font_xpath = ('xpath', "//div[@class='selected-font-input']//i[@class='el-icon-arrow-down']")
    font_name_xpath = ('xpath',"//div[@class='brand-font']//li[@class='font-li'][last()]/div[2]/p")
    first_font_xpath = ('xpath',"//div[@aria-label='选择字体']//div[@class='font-list']//li[1]")  # 添加字体
    # 选择字体确定按钮
    select_font_sure_xpath = ('xpath',"//div[@class='dialog-footer']/div/button[2]")
    # 选择字体取消按钮
    select_font_cancel_button_xpath = ('xpath',"//div[@class='dialog-footer']/div/button[1]")

    # 错误提示
    error_tips_xpath = ('xpath',"//p[@class='el-message__content']")
    # 成功提示
    sucess_tips_xpath = ('xpath', "//p[@class='el-message__content']")
    # 字体more
    last_font_li_xpath = ('xpath',"//div[@class='brand-font']//li[@class='font-li'][last()]")
    last_font_more_xpath = ('xpath',"//div[@class='brand-font']//li[@class='font-li'][last()]//span")
    last_font_modify_xpath = ('xpath',"//div[@class='brand-font']//li[@class='font-li'][last()]/div[last()]/p[1]")
    modiy_font_sure_button_xpath = ('xpath',"//div[@aria-label='修改成功后，使用过该字体的模板将更新为修改后的字体']/div[3]/span/button[2]")
    # 删除字体
    last_font_del_xpath = ('xpath',"//div[@class='brand-font']//li[@class='font-li'][last()]/div[last()]/p[2]")
    # 删除字体确认
    delete_button_xpath = ('xpath',"//button[@class='el-button el-button--primary']/span[contains(text(),'删 除')]")








