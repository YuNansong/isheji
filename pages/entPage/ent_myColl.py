from common.sendDingTalk import SendDingTalk
from model.entModel.entIndexModel import EntIndexModel
from model.entModel.entMyCollModel import EntMyCollModel
from pages.entPage.ent_temp import EnterpirseTemp
from common.readLog import Log
'''
  企业--我的收藏
'''
class EntMyColl(EntIndexModel,EntMyCollModel):
    log = Log(__name__)
    logger = log.getLog()

    def test_act_myColl(self):
        try:
            self.click_manage()
            self.click_ent_myColl()
        except Exception as e:
            self.logger.error('企业--进入我的收藏异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业--进入我的收藏失败")
            raise e

    # 进入模板
    def test_click_temp(self,driver):
        try:
            pic_num = self.get_pictemp_num()
            if pic_num > 0:
                self.logger.info("进入到我的设计页面，点击图片模板")
                self.click_last_pictemp() # 点击最后一个模板
                self.sleep(2)
                self.window(-1)
                temp_url = self.get_qiye_url()
                try:
                    self.jump_work()
                except:
                    self.logger.info("跳过按钮没有出现")
                self.save_temp(driver) # 模板保存按钮
                if "designworkbench" in temp_url:
                    temp_id = self.get_temp_id(driver) # 获取模板ID
                    self.logger.info("打开模板后获取到的模板ID：%d"%temp_id)
                    assert int(temp_id) > 0
                    self.close_handle()
        except Exception as e:
            self.logger.error('企业--我的收藏-点击最后一个模板进入工作台异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业--我的收藏-点击最后一个模板进入工作台失败")
            raise e
    # 取消收藏
    def test_click_cancle_coll(self,driver):
        try:
            pic_num = self.get_pictemp_num()
            if pic_num < 0:
                EnterpirseTemp(driver).test_click_coll_pictemp(driver)
            if pic_num > 0:
                self.hover_last_pictemp()
                self.click_cancel_coll()
                self.click_cancel_sure_btn()
                pic_num_new = self.get_pictemp_num()
                num = pic_num - pic_num_new
                assert num == 1
        except Exception as e:
            self.logger.error('企业--我的收藏-点击取消收藏模板异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("企业--我的收藏-点击取消收藏模板失败")
            raise e