from common.sendDingTalk import SendDingTalk
from pages.basePage import Action
from common.getYaml import url
from common.readLog import Log


class NewMediaPage(Action):
    log = Log(__name__)
    logger = log.getLog()

    def info_new_media_page(self):
        '''验证进入新媒体落地页功能'''
        self.transfer_url('/xinmeitilp.html')
        self.sleep()

    def make_one_picture(self):
        '''验证开始做图功能'''
        try:
            one_make_button = ('xpath', "//div[@class='banner-inner']//button[@class='box_content_btn']")
            self.click(one_make_button)#进入首页
            self.window(-1)
            new_url = self.getUrl()
            urlInfo = url['url']['testUrl']+'/'
            self.close_and_window()
            print(new_url)
            print(urlInfo)
            assert new_url == urlInfo
        except Exception as e:
            self.logger.error('失败：未从新媒体落地页点击开始做图进入首页%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：未从新媒体落地页点击开始做图进入首页")
            raise e

    def info_work_page(self):
        try:
            title_list = self.driver.find_elements('xpath', "//ul[@class='nav']/li")
            num = range(1, len(title_list))
            for i in num:
                title_button = ('xpath', "//ul[@class='nav']/li["+str(i)+"]")
                title_text = self.getText(title_button)
                title_text = title_text.strip()
                print("title_text",title_text)
                self.click(title_button)
                self.window(-1)
                other_title_text = ('xpath', "//div[@class='search-item-content typelist']/span[@class='search-active']/a")
                other_title_text_real = self.getText(other_title_text)
                other_title_text_real = other_title_text_real.strip()
                print("other_title_text_real",other_title_text_real)
                self.close_and_window()
                # self.move_to_stay("//ul[@class='nav']/li["+str(i)+"]")
                move_ready = ("xpath", "//ul[@class='nav']/li["+str(i)+"]")
                self.mouse_hover(move_ready)
                one_temp = ("xpath", "//ul[@class='nav-content']/li["+str(i)+"]/div[1]/img")
                self.click(one_temp)
                self.window(-1)
                try:
                    self.jump_work()
                except:
                    self.logger.info('进入工作台未出现跳过')
                # save_button = ('xpath', "//button[@class='save-btn']")
                # self.click(save_button)
                self.preservation()
                self.close_and_window()
                print("title_text:", title_text, ">>>>>>", "other_title_text_real:", other_title_text_real)
                assert title_text == other_title_text_real
        except Exception as e:
            self.logger.error('失败：未从新媒体落地页点击模版进入工作台%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：未从新媒体落地页点击模版进入工作台")
            raise e

    def make_two_picture(self):
        '''验证中部开始作图按钮'''
        try:
            two_make_button = ('xpath', "//section[@id='content_box2']//button[@class='box_content_btn']")
            self.click(two_make_button)#进入首页
            self.window(-1)
            new_url = self.getUrl()
            urlInfo = url['url']['testUrl']+'/'
            self.close_and_window()
            assert new_url == urlInfo
        except Exception as e:
            self.logger.error('失败：未从新媒体落地页点击开始做图进入首页%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：未从新媒体落地页点击开始做图进入首页")
            raise e

    def info_scene(self):
        '''验证进入落地页场景'''
        try:
            scene_buttons_list = self.driver.find_elements('xpath', "//div[@class='content_box-inner']/ul/li")
            scene_buttons_num = len(scene_buttons_list)
            for i in range(1, scene_buttons_num+1):
                print(i)
                scene = ('xpath', "//div[@class='content_box-inner']/ul/li["+str(i)+"]")
                self.click(scene)
                self.window(-1)
                fving = ('xpath', "//li[@class='block-item template-tp block-item-active']//span[@class='block-text']")
                pingk = self.getText(fving)
                self.sleep(1)
                self.close_and_window()
                assert pingk == '图片模板'
        except Exception as e:
            self.logger.error('失败：未从新媒体落地页点击场景进入首页%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：未从新媒体落地页点击场景进入首页")
            raise e

    def other_make_picture(self):
        '''验证其他开始作图按钮功能'''
        try:
            three_make_button = ('xpath', "//button[@id='btn5']")
            self.click(three_make_button)

            self.window(-1)
            self.sleep()
            new_url_one = self.getUrl()
            urlInfo = url['url']['testUrl'] + '/'
            self.close_and_window()
            #===============================
            four_make_button = ('xpath', "//section[@id='content_box4']//button[@class='box_content_btn']")
            self.click(four_make_button)
            self.window(-1)
            self.sleep()
            new_url_two = self.getUrl()
            self.close_and_window()
            #===============================
            last_make_button = ('xpath', "//div[@class='content_box5-left']//button[@class='box_content_btn']")
            self.click(last_make_button)
            self.window(-1)
            self.sleep()
            new_url_three = self.getUrl()
            self.close_and_window()

            logo = ('xpath', "//img[@class='logo']")
            self.click(logo)

            assert new_url_one == urlInfo and new_url_two == urlInfo and new_url_three == urlInfo
        except Exception as e:
            logo = ('xpath', "//img[@class='logo']")
            self.click(logo)
            self.logger.error('失败：未从新媒体落地页点击其他开始作图按钮跳转至首页%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：未从新媒体落地页点击其他开始作图按钮跳转至首页")
            raise e