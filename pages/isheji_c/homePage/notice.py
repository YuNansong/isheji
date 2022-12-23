from common.sendDingTalk import SendDingTalk
from pages.basePage import Action
from common.readLog import Log


class Notice(Action):
    '''右上角铃铛：通知中心'''
    log = Log(__name__)
    logger = log.getLog()

    def small_bell(self):
        '''进入小铃铛'''
        try:
            small_bell_button = ('xpath', "//span[@class='iconfont icon-tongzhi1']")
            self.click(small_bell_button)
            self.sleep()
            try:
                # 断言：消息通知
                fving = ('xpath', "//div[@class='message-content']//h5")
                actual = self.getText(fving)
                expect = '消息通知'
                self.assert_text(expect, actual)
            except Exception as e:
                look_more = ('xpath', "//div[@class='btn-more']")
                actual = self.getText(look_more)
                expect = '查看更多'
                self.assert_text(expect, actual)
                self.logger.error('失败：未找到消息通知标识%s' % repr(e))
                SendDingTalk().sendDingTalkMsg("失败：未找到消息通知标识")
        except Exception as e:
            self.logger.error('失败：进入消息通知失败%s' % e)
            SendDingTalk().sendDingTalkMsg("失败：进入消息通知失败")
            raise e
        self.home_button()
