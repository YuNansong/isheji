from common.readLog import Log
from pages.basePage import Action
from common.sendDingTalk import SendDingTalk
from element.isheji_c.home.find_similarities import FindSimilarities


class Similarities(Action):
    log = Log(__name__)
    logger = log.getLog()

    def into_find_page(self):
        """首页的找相似功能"""
        try:
            self.mouse_hover(FindSimilarities.first_template)
            self.click(FindSimilarities.similarutues_button)
            find_str = self.getText(FindSimilarities.similarutues_str)
            assert find_str == "找相似"
        except Exception as e:
            self.logger.error("首页找相似功能错误%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("首页找相似功能错误")
            self.refresh()
            raise e

    def into_preview_page(self):
        """找相似页面进入模板"""
        try:
            self.into_find_page()
            self.click(FindSimilarities.find_first_template)
            self.sleep()
            try:#未登录的状态，出现登录弹窗
                winds = self.driver.window_handles
                winds_num = len(winds)
                if winds_num == 1:
                    name_pwd = self.getText(FindSimilarities.username_assert)
                    if name_pwd == "账号密码登录":
                        self.click(FindSimilarities.login_x_button)
                    else:
                        self.logger.info("点击找相似模板未出现登录或已登录")
                else:
                    self.close_and_window()
            except:#登录状态
                self.window(-1)
                try:
                    self.jump_work()
                except:
                    self.logger.info("进入工作台未出现跳过按钮")
                self.preservation()
                self.close_and_window()
        except Exception as e:
            self.logger.error("首页找相似页面点击模板错误%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("首页找相似页面点击模板错误")
        finally:
            self.refresh()