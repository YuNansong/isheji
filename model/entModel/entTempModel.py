from pages.basePage import Action
from element.ent.entTempElement import EntTempElement
from pages.isheji_c.tempCenterPage.workbenchPage import WorkBench

class EntTempModel(Action):
    # 上传模板
    def upload_temp(self):
        self.click(EntTempElement.upload_button_xpath)
        self.sleep(2)

    # 选择文件
    def add_pic_file(self,psd):
        self.write(EntTempElement.upload_file, psd)

    # 确定上传图片
    def sure_add_pic_file(self):
        self.click(EntTempElement.ok_button)

    # 新增文件夹
    def add_folder(self):
        self.click(EntTempElement.new_file)

    # 右侧企业素材
    def right_menu_temp(self):
        self.click(EntTempElement.sp)

    # 输入文件夹名称
    def input_folder_name(self,name="testmuban"):
        self.clear_folder_name()
        self.write(EntTempElement.file_name, name)

    # 清空文件夹
    def clear_folder_name(self):
        self.clear(EntTempElement.file_name)

    # 获取文件夹名称
    def get_first_folder_name(self):
        try:
            name = self.getText(EntTempElement.folder_name_xpath)
        except:
            name = ""
        return name
    # 悬浮到一个文件夹上
    def select_first_folder(self):
        self.mouse_hover(EntTempElement.first_folder_xpath)
        self.sleep(1)

    # 点击第一个文件夹的更多按钮
    def click_folder_more(self):
        self.click(EntTempElement.more_btn_xpath)

    # 重命名文件夹
    def rename_folder_name(self):
        self.click(EntTempElement.rename_folder_xpath)

    # 删除文件夹
    def delete_folder_name(self):
        self.click(EntTempElement.delete_folder_xpath)

    # 输入文件夹名称，确定
    def sure_add_folder(self):
        self.click(EntTempElement.file_ed)

    # 确定删除文件夹
    def sure_del_folder(self):
        self.click(EntTempElement.sure_delete_xpath)

    # 获取文件夹个数
    def get_folder_num(self):
        self.sleep(1)
        try:
            folder_xpath = ('xpath',"//div[@class='template-list']/ul[1]/li")
            folder_num = len(self.getElements(folder_xpath))
        except:
            folder_num = 0
        return folder_num

    # 获取文件夹中含有x个文件
    def get_folder_file_num(self,i):
        try:
            file_number_xpath = ('xpath',"//div[@class='template-list']/ul[1]/li["+str(i)+"]/p[2]")
            file_num_all = self.getText(file_number_xpath)
            file_num = str(file_num_all).strip()[0:-3]
        except:
            file_num = 0
        return int(file_num)

    # 双击打开文件夹
    def open_folder(self):
        file_num_new = 0
        folder_num = self.get_folder_num()
        for i in range(1,folder_num+1):
            file_num = self.get_folder_file_num(i)
            if file_num > 0:
                last_folder_xpath = ('xpath',"//div[@class='template-list']/ul[1]/li["+str(i)+"]")
                file_num_new = file_num
                self.double_click(last_folder_xpath)
                break
        return file_num_new

    # 上传模板
    def upload_modo(self,name):
        upload_file = ('xpath', "//input[@name='file']")
        self.write(upload_file, name)

    # 保存模板
    def save_temp(self,driver):
        WorkBench(driver).save_btn()

    # 获取模板ID
    def get_temp_id(self,driver):
        temp_id = WorkBench(driver).get_temp_id()
        id = int(temp_id)
        return id

    def get_temp_title(self):
        header_xpath = ('xpath',"//input[@class='header-nameinput']")
        name = self.executeJs("$(\".header-nameinput\").val()",header_xpath)
        print("tempName:",name)
        return name

    # 设置模板为企业模板
    def set_ent_team_temp(self):
        make_set = ('xpath', "//div[@class='set-team-template']")
        self.click(make_set)

    # 保存新模板
    def save_new_temp(self):
        self.click(EntTempElement.save_new_temp_xpath)

    # 移动文件选择文件夹
    def select_folder(self):
        select_children_folder = ('xpath',"//div[@class='el-tree-node__children']/div[last()]")
        self.click(select_children_folder)

    # 确定移动文件
    def sure_move_btn(self):
        sure_move_btn_xpath = ('xpath',"//div[@aria-label='移动']//button[2]")
        self.click(sure_move_btn_xpath)

    # 确认保存按钮
    def sure_save_btn(self):
        self.click(EntTempElement.sure_save_btn_xpath)

    # 保存新模版成功提示
    def get_save_succ_tips(self):
        tips = self.getText(EntTempElement.save_succ_tips_xpath)
        return str(tips).strip()

    # 返回团队模板
    def back_team_temp(self):
        self.click(EntTempElement.back_team_temp_xpath)

    # 移动模板
    def move_temp(self):
        move_button = ('xpath', "//div[@class='template-list']/ul[2]/li[last()]//div[@class='more-box']/p[contains(text(),'移动')]")
        self.click(move_button)

    # 删除模板按钮
    def click_delete_btn(self):
        flag = True
        try:
            delete_button = ('xpath', "//div[@class='more-box']/p[contains(text(),'删除')]")
            self.click(delete_button)
            return flag == True
        except:
            return flag == False

    # 确定删除模板按钮
    def click_sure_delete_btn(self):
        sure_btn_xpath = ('xpath',"//div[contains(@aria-label ,'是否确认删除该')]//button[@class='el-button el-button--primary']")
        self.click(sure_btn_xpath)
    # 获取模板名称
    def get_temp_name(self):
        temp_name_xpath = ('xpath',"//div[@class='template-list']/ul[2]/li[last()]/p")
        temp_name = self.getText(temp_name_xpath)
        return temp_name

    # 获取图片模板个数
    def get_pictemp_num(self):
        self.sleep(2)
        try:
            pictemp_xpath = ('xpath',"//div[@class='template-list']/ul[2]/li")
            pic_num = len(self.getElements(pictemp_xpath))
        except:
            pic_num = 0
        return pic_num

    # 点击最后一个模板
    def click_last_temp(self):
        picture_template = ('xpath', "//div[@class='template-list']/ul[2]/li[last()]")
        self.click(picture_template)
    # 悬浮到模板
    def hover_temp(self,i=0):
        picture_template = ('xpath', "//div[@class='template-list']/ul[2]/li[last()-"+str(i)+"]")
        self.mouse_hover(picture_template)
        self.sleep(1)

    # 点击图片模板的更多按钮
    def click_pic_temp_more(self,i=0):
        more_btn_xpath = ('xpath', "//div[@class='template-list']/ul[2]/li[last()-"+str(i)+"]//span[@class='iconfont icon-More font-icon-more more-act']")
        self.click(more_btn_xpath)
        self.sleep(1)

    # 企业模板--收藏模板
    def click_coll_temp(self):
        coll_button = ('xpath', "//div[@class='template-list']/ul[2]/li[last()]//div[@class='more-box']/p[contains(text(),'收藏')]")
        self.click(coll_button)

    # 企业模板--下载模板
    def click_download_temp(self):
        coll_button = ('xpath', "//div[@class='template-list']/ul[2]/li[last()]//div[@class='more-box']/p[contains(text(),'下载')]")
        self.click(coll_button)

    # 重命名模板
    def rename_temp(self):
        rename_button = ('xpath', "//div[@class='template-list']/ul[2]/li[last()]//div[@class='more-box']/p[contains(text(),'重命名')]")
        self.click(rename_button)

    # 输入新模板名称
    def input_new_temp(self,name):
        input_text = ('xpath',"//input[@placeholder='请输入名称']")
        self.clear(input_text)
        self.write(input_text,name)
    # 确定重命名按钮
    def click_sure_rename_btn(self):
        sure_btn_xpath = ('xpath',"//div[@aria-label='重命名']//button[@class='el-button el-button--primary']")
        self.click(sure_btn_xpath)

    # 移动文件选择文件夹
    def click_folder_tree(self):
        folder_tree_xpath = ('xpath',"//div[@class='el-tree']")
        self.click(folder_tree_xpath)

    #
    def get_page_num(self):
        # 进行翻页操作
        page_xpath = ('xpath',"//ul[@class='el-pager']/li")
        page_num = len(self.getElements(page_xpath))
        return page_num

    def click_fanye(self):
        last_page_xpath = ('xpath',"//ul[@class='el-pager']/li[last()]")
        self.click(last_page_xpath)
