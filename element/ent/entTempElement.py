class EntTempElement:
    upload_button_xpath = ('xpath', "//div[@class='tmp-title nav-title']//button[2]//span[1]")
    upload_file = ('xpath', "//input[@name='file']") # 上传模板，选择文件
    new_file = ('xpath', "//div[@class='tmp-title nav-title']//button[1]//span[1]")
    sp = ('xpath', "//ul[@class='submenulist']/li[1]/a[@href='/template']/span")
    file_name = ('xpath', "//input[@placeholder='请输入名称']")
    file_ed = ('xpath',"//div[@class='el-dialog__wrapper rename-dialog']//button[@class='el-button el-button--primary']//span")
    ok_button = ('xpath', "//div[@class='btn-wrap']//button[@class='el-button el-button--primary']//span")
    folder_name_xpath = ('xpath',"//div[@class='template-list']/ul[1]/li[1]/p[1]")
    first_folder_xpath = ('xpath',"//div[@class='template-list']/ul[1]/li[1]")
    more_btn_xpath = ('xpath',"//div[@class='template-list']/ul[1]/li[1]/span")
    rename_folder_xpath = ('xpath',"//div[@class='template-list']/ul[1]/li[1]//p[contains(text(),'重命名')]")
    delete_folder_xpath = ('xpath',"//div[@class='template-list']/ul[1]/li[1]//p[contains(text(),'删除')]")
    sure_delete_xpath = ('xpath',"//div[@aria-label='是否确认删除该文件夹']//button[2]") # 确定删除按钮
# 确定为企业模板
    save_new_temp_xpath = ('xpath',"//button[@class='el-button design-button-primary el-button--default']")
    three_jiao = ('xpath', "//span[@class='el-tree-node__expand-icon el-icon-caret-right']")
    sure_save_btn_xpath = ('xpath',"//button[@class='el-button design-button-primary el-button--default']/span[contains(text(),'确认')]")
    save_succ_tips_xpath = ('xpath',"//div[@class='dialog-main-tip' and contains(text(),'保存成功')]") # 保存成功
    back_team_temp_xpath = ('xpath',"//span[contains(text(),'返回团队模板')]")