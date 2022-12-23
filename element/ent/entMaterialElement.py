class EntMaterialElement:
    upload_button_xpath = ('xpath', "//div[@class='tmp-title nav-title']//button[2]//span[1]")
    upload_file = ('xpath', "//input[@name='file']") # 上传素材，选择文件
    sp = ('xpath', "//ul[@class='submenulist']/li[1]/a[@href='/material']/span")
    file_ed = ('xpath',"//div[@class='el-dialog__wrapper rename-dialog']//button[@class='el-button el-button--primary']//span")
    ok_button = ('xpath', "//div[@class='btn-wrap']//button[@class='el-button el-button--primary']//span")