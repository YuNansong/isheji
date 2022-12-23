from common.readLog import Log
from common.sendDingTalk import SendDingTalk
from model.entModel.entIndexModel import EntIndexModel
from model.entModel.newDesignModel import NewDesignModel
from model.workbench.workbenchModel import WorkbenchModel
class NewDesign(EntIndexModel,NewDesignModel,WorkbenchModel):
    '''我的企业：企业空间'''
    log = Log(__name__)
    logger = log.getLog()
    def act_new_design(self):
        self.click_manage()
        self.click_new_design()

    # 企业端--自定义尺寸
    def test_create_custome_temp(self):
        wide = 300
        high = 300
        try:
            self.click_custom_button()
            self.sleep(1)
            self.input_custom_wide(wide)
            self.input_custom_high(high)
            self.click_start_design()
            self.window(-1)
            self.jump_home()
            self.save_btn()
            url = self.get_qiye_url()
            assert "designworkbench" in url
            self.close_handle()
        except Exception as e:
            self.logger.error('企业端--点击自定义尺寸失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业端--点击自定义尺寸失败")
            raise e

    # 企业端--新建设计页面点击各个分类模板
    def test_click_temp(self):
        try:
            for i in range(1,6):
                temp_size_xpath = ("xpath","//section[@class='create-a-design']/section/ul["+str(i)+"]/li[1]/div/p[2]")
                temp_size = self.getText(temp_size_xpath)
                index = temp_size.index('x')
                size = str(temp_size[index+2:-2]).strip()
                temp_xpath = ("xpath","//section[@class='create-a-design']/section/ul["+str(i)+"]/li[1]")
                self.click(temp_xpath)
                self.window(-1)
                self.jump_home()
                self.save_btn()
                workbench_size = self.get_temp_size() # 工作台获取模板
                self.close_handle()
                assert size == workbench_size
        except Exception as e:
            self.logger.error('企业端--新建设计页面点击各个分类模板失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业端--新建设计页面点击各个分类模板失败")
            raise e

