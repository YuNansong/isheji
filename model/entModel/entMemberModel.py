from pages.basePage import Action
from element.ent.entMemberElement import EntMemberElement
class EntMemberManageModel(Action):
    # 点击编辑按钮
    def click_edit(self):
        self.click(EntMemberElement.edit_temp_xpath)

    # 清空输入框
    def clear_temp_name(self):
        self.clear(EntMemberElement.input_temp_name_xpath)

    # 输入团队名称
    def input_temp_name(self,name):
        self.write(EntMemberElement.input_temp_name_xpath,name)

    # 编辑名称确认框
    def click_temp_name_sure_btn(self):
        self.click(EntMemberElement.temp_name_sure_btn_xpath)

    # 获取团队名称
    def get_temp_name(self):
        name = self.getText(EntMemberElement.temp_name_xpath)
        return str(name).strip()

    # 点击邀请成员
    def click_invite_member_btn(self):
        self.click(EntMemberElement.invite_member_xpath)

    # 获取邀请链接
    def get_invite_link(self):
        link = self.getText(EntMemberElement.invite_member_link_xpath)
        return str(link).strip()

    # 点击复制链接按钮
    def click_copy_link_btn(self):
        self.click(EntMemberElement.copy_link_btn_xpath)

    # 获取复制链接按钮属性
    def get_copy_link_btn_attr(self):
        attr = self.getElementAttr(EntMemberElement.copy_link_btn_xpath,'style')
        return str(attr).strip()

    # 关闭邀请成员弹框
    def click_invite_link_close_btn(self):
        self.click(EntMemberElement.invite_member_link_close)

    # 点击发送邀请链接
    def click_send_invite_link(self):
        self.click(EntMemberElement.send_invite_link_xpath)

    # 点击发送邀请链接
    def click_add_member(self):
        self.click(EntMemberElement.add_member_xpath)

    # 点击发送邀请链接
    def click_add_one_member(self):
        self.click(EntMemberElement.add_one_member_xpath)

    # 点击发送邀请链接
    def click_add_more_member(self):
        self.click(EntMemberElement.add_more_member_xpath)

    # 添加手机号
    def input_phone(self,phone):
        self.write(EntMemberElement.input_phone_xpath,phone)
    # 添加email
    def input_email(self,email):
        self.write(EntMemberElement.input_email_xpath,email)
    # 添加备注
    def input_remark(self,remark):
        self.write(EntMemberElement.input_remak_xpath,remark)
    # 清空备注
    def clear_remark(self):
        self.clear(EntMemberElement.input_remak_xpath)
    # 点击确定按钮
    def click_sure_add_btn(self):
        self.click(EntMemberElement.add_one_member_btn)

    # 下载模版
    def download_xls(self):
        self.click(EntMemberElement.download_xls_xpath)

    # 上传成员模版
    def upload_xls(self):
        self.click(EntMemberElement.upload_xls_xpath)
    # 获取导入xls成功提示
    def get_upload_xls_succ(self):
        text = self.getText(EntMemberElement.upload_xls_succ_xpath)
        return str(text).strip()
    # 获取导入xls成功个数
    def get_upload_xls_num(self):
        text = self.getText(EntMemberElement.upload_xls_num_xpath)
        return str(text).strip()

    # 关闭上传xls弹框
    def closed_upload_alert(self):
        self.click(EntMemberElement.close_upload_xpath)

    # 编辑成员
    def edit_member(self):
        self.click(EntMemberElement.edit_member_xpath)

    # 编辑提交
    def srue_edit_member(self):
        self.click(EntMemberElement.sure_modify_btn_xpath)

    # 移除成员
    def move_member(self):
        self.click(EntMemberElement.move_member_xpath)

    # 确定移除
    def srue_move_member(self):
        self.click(EntMemberElement.sure_move_btn_xpath)

    # 获取最后一条成员备注
    def get_last_remark_text(self):
        remark = self.getText(EntMemberElement.last_remark_xpath)
        return str(remark).strip()
