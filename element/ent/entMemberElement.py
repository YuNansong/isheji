
class EntMemberElement:

    # PageTitle: "xpath,//div[@class='member info-con']/descendant::div[@class='tt-left']"
    edit_temp_xpath = ('xpath',"//div[@class='mil-title']/descendant::img") # 编辑团队按钮
    input_temp_name_xpath = ('xpath',"//div[@class='el-dialog__wrapper rename-dialog']/descendant::input[@type='text']") # 输入团队名称
    temp_name_sure_btn_xpath= ('xpath',"//div[@class='el-dialog__wrapper rename-dialog']/descendant::button[3]") #输入团队名称确认按钮
    temp_name_xpath = ('xpath',"//div[@class='mil-title']/h3") # 获取团队名称
    invite_member_xpath = ('xpath',"//div[@class='mi-right']/button") # 邀请成员
    invite_member_link_xpath = ('xpath',"//div[@class='invite-input']") # 邀请成员链接
    copy_link_btn_xpath = ('xpath',"//button[@class='el-button invite-dialog-btn el-button--primary']") # 复制邀请链接按钮
    invite_member_link_close = ('xpath',"//div[@class='el-dialog__wrapper invite-dialog']/descendant::button[@aria-label='Close']") # 关闭邀请弹框
    send_invite_link_xpath = ('xpath',"//li[contains(text(),'发送邀请链接')]") # 发送邀请链接
    add_member_xpath = ('xpath',"//div[@class='mi-right']/div[@class='el-dropdown']/button") # 添加成员按钮
    add_one_member_xpath = ('xpath',"//ul[@class='el-dropdown-menu el-popper member-drop']/li[2]") # 选择添加一个成员
    add_more_member_xpath = ('xpath',"//ul[@class='el-dropdown-menu el-popper member-drop']/li[1]") # 添加多个
    input_phone_xpath = ('xpath',"//input[@placeholder='请输入手机号']") # 添加手机号
    input_email_xpath = ('xpath',"//input[@placeholder='请输入邮箱']") # 添加邮箱
    input_remak_xpath = ('xpath',"//textarea[@placeholder='请输入备注']") # 添加备注
    add_one_member_btn = ('xpath',"//button[@class='el-button confirm-btn el-button--primary']/span") # 确定添加
    download_xls_xpath = ('xpath',"//div[@class='member-first']/button") # 点击下载
    upload_xls_xpath = ('xpath',"//div[@class='member-two']/descendant::button") # 点击上传:
    upload_xls_succ_xpath = ('xpath',"//div[@class='ua-success']/p[1]")
    upload_xls_num_xpath = ('xpath',"//div[@class='ua-success']/p[2]")
    close_upload_xpath = ('xpath',"//div[@aria-label='批量导入成员']/div[1]/button") # 关闭添加
    move_member_xpath = ('xpath',"//*[@id='app']/div[3]/div[3]/div[2]/div/div[3]/table/tbody/tr[last()]/td[9]/div/button[2]") # 移除成员
    sure_move_btn_xpath = ('xpath',"//div[@aria-label='是否确认删除该成员']//button[2]") # 确定移除
    edit_member_xpath = ('xpath',"//*[@id='app']/div[3]/div[3]/div[2]/div/div[3]/table/tbody/tr[last()]/td[9]/div/button[1]") # 编辑成员
    # = ('xpath',"//*[@id='app']/div[3]/div[4]/div/div[2]/div/form/div[5]/div/div/textarea") # 备注框
    sure_modify_btn_xpath= ('xpath',"//*[@id='app']/div[3]/div[4]/div/div[3]/span/button") # 保存修改
    last_remark_xpath = ('xpath',"//*[@id='app']/div[3]/div[3]/div[2]/div/div[3]/table/tbody/tr[last()]/td[last()-1]//p") # 备注信息
