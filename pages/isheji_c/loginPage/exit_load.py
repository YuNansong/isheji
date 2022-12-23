from pages.basePage import Action
from common.readLog import Log
from common.sendDingTalk import SendDingTalk


class Exit_Load(Action):
    log = Log(__name__)
    logger = log.getLog()

    def exit_action(self):
        try:
            self.close_and_home_page()
            self.close_and_home_page()
            self.logger.info("开始退出登录")
            # self.move_to_stay("//img[@class='head-image']")
            self_mede = ("xpath", "//img[@class='head-image']")
            self.mouse_hover(self_mede)
            self.sleep(2)
            exitcli = ("xpath", "//li[@id='loginquit']//a//span")
            self.click(exitcli)
            self.sleep()
        except Exception as e:
            self.logger.error("账号退出登录异常%s" % str(e))
            SendDingTalk().sendDingTalkMsg("账号退出登录失败")
            raise e
