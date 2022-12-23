from common.sendDingTalk import SendDingTalk
from common.readLog import Log
from model.entModel.entIndexModel import EntIndexModel


class DataStatistice(EntIndexModel):
    '''我的企业：数据统计'''

    log = Log(__name__)
    logger = log.getLog()

    def test_act_dataStat(self):
        '''进入数据统计'''
        try:
            self.click_manage()
            self.click_data_statistice()
            # 断言是否进入
            baqedata = ('xpath', "//div[@id='app']//div[1]//h4[1]")
            actual = self.getText(baqedata)
            expect = '版权数据'
            self.assert_text(expect, actual)
        except Exception as e:
            self.logger.error('我的企业：数据统计断言：版权数据是否在页面中断言失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("我的企业：数据统计断言：版权数据是否在页面中断言失败")
            raise e

    # def getcookie(self):
    #     cookie = Interface.getCookie()
    #     url = 'https://wy7tyx.jff.wxbjq.top/enter/team/copyright_image/use_num'
    #     headers = {
    #         'Cookie': "'" + cookie + "'"
    #     }
    #     bady = {
    #         "team_id": 185,
    #         "start_date": "2021-10-28",
    #         "end_date": "2021-11-03"
    #     }
    #     res = requests.request('post', url=url, headers=headers, json=bady)

    #     print(res.json())

    def one_more_button(self):
        '''版权用量更多按钮'''
        more_button = (
            'xpath', "//div[@class='statistics-content']//div[1]//div[1]//div[1]//div[2]//button[1]//span[1]")
        self.click(more_button)
        self.sleep()

    def refresh(self):
        '''刷新按钮'''
        refresh_button = ('xpath', "//div[@class='pop']//button[1]//span[1]")
        self.click(refresh_button)
        self.sleep()

    def export(self):
        '''导出按钮'''
        export_button = ('xpath', "//div[@class='pop']//button[2]//span[1]")
        self.click(export_button)
        self.sleep()

    def x_box(self):
        '''关闭'''
        x_button = ('xpath', "//div[@class='el-dialog__wrapper']//i[@class='el-dialog__close el-icon el-icon-close']")
        self.click(x_button)

    def use_export_button(self):
        '''版权用量导出'''
        try:
            export_button = (
                'xpath', "//div[@class='statistics-content']//div[1]//div[1]//div[1]//div[2]//button[2]//span[1]")
            self.click(export_button)
            self.sleep()
        except:
            self.logger('我的企业-数据统计：版权用量导出失败')
            SendDingTalk().sendDingTalkMsg("我的企业-数据统计：版权用量导出失败")

    def two_more_button(self):
        '''成员情况更多按钮'''
        more_button = (
            'xpath', "//div[@class='statistics-content']//div[2]//div[1]//div[1]//div[2]//button[1]//span[1]")
        self.click(more_button)
        self.sleep()

    def top_more_button(self):
        '''上边的导出更多'''
        try:
            top_button = ('xpath', "//button[@class='el-button export el-button--primary']//span//span")
            self.click(top_button)
        except Exception as e:
            self.logger('我的企业-数据统计：版权用量更多导出失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("我的企业-数据统计：版权用量导出失败")
            raise e

    def copyright_pictures_usage(self):
        '''版权图片用量'''
        self.one_more_button()
        self.refresh()
        self.export()
        self.x_box()
