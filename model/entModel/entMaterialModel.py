from pages.basePage import Action
from element.ent.entMaterialElement import EntMaterialElement
class EntMaterialModel(Action):
    # 上传素材
    def upload_material(self):
        self.click(EntMaterialElement.upload_button_xpath)

    # 上传素材选择jpeg文件
    def add_pic_file(self,jpg):
        self.write(EntMaterialElement.upload_file, jpg)

    # 确定上传图片
    def sure_add_pic_file(self):
        self.click(EntMaterialElement.ok_button)

    # 右侧企业素材
    def right_menu_sucai(self):
        self.click(EntMaterialElement.sp)