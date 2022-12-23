from common.sendDingTalk import SendDingTalk
from pages.basePage import Action
from common.readLog import Log
from common.getYaml import url


class PosterHome(Action):
    log = Log(__name__)
    logger = log.getLog()

    def info_poster_home_page(self):
        '''验证进入海报家落地页功能'''
        self.transfer_url('/poster.html')
        self.sleep()

    def design_button_info(self):
        '''验证开始作图进入新建设计'''
        try:
            des_button = ('xpath', "//div[@class='row']//div[@class='button']")
            self.click(des_button)
            self.window(-1)
            now_url = self.getUrl()
            urlInfo = url['url']['testUrl'] + '/design'
            self.close_and_window()
            assert now_url == urlInfo
        except Exception as e:
            self.logger.error('失败：未从海报家落地页点击开始做图进入新建设计%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：未从海报家落地页点击开始做图进入新建设计")
            raise e

    def info_poster(self):
        '''验证进入海报'''
        try:
            input_box = ('xpath', "//input[@id='template-search']")
            self.write(input_box, '公众号次图')
            poster_list = self.driver.find_elements('xpath', "//section[@class='classList']/div")
            poster = len(poster_list)
            poster +=1
            for i in range(1, poster):
                print(i)
                post_button = ('xpath', "//section[@class='classList']/div["+str(i)+"]")
                self.click(post_button)
                self.window(-1)
                fving = ('xpath', "//li[@class='block-item template-tp block-item-active']//span[@class='block-text']")
                pingk = self.getText(fving)
                if pingk == '模板中心':
                    self.close_and_window()
                    continue
                else:
                    SendDingTalk().sendDingTalkMsg("失败：未从海报家落地页点击海报进入模版中心")
                    print(i)
                    break
        except Exception as e:
            self.logger.error('失败：未从海报家落地页点击海报进入模版中心%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：未从海报家落地页点击海报进入模版中心")
            raise e

    def input_boxfind(self):
        '''验证海报搜索功能'''
        try:
            input_box = ('xpath', "//input[@id='template-search']")
            preset = '公众号次图'
            self.write(input_box, preset)
            self.sayok(input_box)
            self.window(-1)
            fving = ('xpath', "//div[@class='search-item-content typelist']/span[@class='search-active']/a")
            imprint = self.getText(fving)
            assert preset == imprint
        except Exception as e:
            self.logger.error('失败：未从海报家落地页搜索进入模版中心%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：未从海报家落地页搜索进入模版中心")
            raise e

    def poster_posters(self):
        poster_list = self.driver.find_elements('xpath', "//div[@id='navList']/div")
        poster_num = len(poster_list)
        poster_num += 1
        for i in range(1, poster_num):
            self.move_to_stay("//div[@id='navList']/div["+str(i)+"]")
            #海报家落地页中间海报，需要遍历再下一层
