from element.isheji_c.workbench.workbenchElement import WorkBenchElement
from common.readLog import Log
from pages.basePage import Action
class WorkbenchModel(Action):
    log = Log(__name__)
    logger = log.getLog()
    # 在工作台点击跳过按钮
    def jump_home(self):
        try:
            self.logger.info("进入工作台点击跳过按钮")
            self.click(WorkBenchElement.jump_btn_element)
            self.sleep(1)
        except:
            self.logger.info("进入工作台跳过按钮没有出现")

    # 在工作台点击保存按钮
    def save_btn(self):
        self.logger.info("在工作台点击保存按钮")
        self.click(WorkBenchElement.save_btn_element)

    # 工作台右侧获取模板大小【高】
    def get_temp_size(self):
        workbench_temp_size = self.getText(WorkBenchElement.workbench_temp_size_xpath)
        workbench_size = str(workbench_temp_size[:-2]).strip()
        return workbench_size