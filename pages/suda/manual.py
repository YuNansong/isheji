from common.path import jepg
from common.readLog import Log
from pages.basePage import Action
from pages.suda.suda_login import token
from common.sendDingTalk import SendDingTalk


class Manual(Action):
    log = Log(__name__)
    logger = log.getLog()

    def into_suda(self):
        self.driver.get('https://wangjun-isj-pc.wxbjq.top/iframeproduction.html')


    def change_token(self):
        '''手动初始化token'''
        input_box = ('xpath', "//div[@class='el-col el-col-12']//div[2]//input[1]")
        self.clear(input_box)
        self.write(input_box, token)
        initialization_button = ('xpath', "//button[@class='el-button el-button--danger']//span")
        self.click(initialization_button)
        #站内模版创建设计
        new_design_button = ('xpath', "//div[@class='el-col el-col-20']//button[1]//span[1]")
        self.click(new_design_button)
        self.sleep(8)


    def modo_list(self):
        '''模版'''
        #进入frame
        frame = ('xpath', "//div[3]//iframe[1]")
        self.switch_iframe(frame)
        # #模版搜索
        find_button = ('xpath', "//ul[@id='tab-item-list']/li[1]/div/input")
        values = '领取'
        self.write(find_button, values)
        self.sayok(find_button)

    def click_one_modo(self):
        '''更换模版'''
        one_modo = ('xpath', "//section[@class='template-wrap']/ul[1]/li[1]")
        self.click(one_modo)
        # try:
        #     enter_button = ('xpath', "//div[@class='el-message-box__btns']/button[2]/span[1]")
        #     self.ptclick(enter_button)
        # except:
        #     self.sleep(1)


    def phono_picture(self):
        '''照片'''
        photo = ('xpath', "//nav[@id='tabList']/ul[@class='guidance-tools']/li[2]/span")
        self.click(photo)
        shuru = ('xpath', "/html//ul[@id='tab-item-list']/li[2]//input[@type='text']")
        values = '电脑'
        self.write(shuru, values)
        self.sayok(shuru)
        self.sleep()
        first_photo = ('xpath',
                       "//ul[@id='tab-item-list']/li[2]/div/div[3]/div[@class='photos-list-all']/div[@class='coryright-photo-list infinite-list justified-gallery']/div[1]/img")
        self.click(first_photo)


    def download_upvip(self):
        '''下载升级VIP'''
        try:
            self.logger.info("进入工作台点击下载升级VIP按钮")
            download_button = ('xpath', "//button[@id='design-hide-btn']")
            self.click(download_button)
            download_pay_button = ('xpath', "//div[@class='download-btn-dialog pay-personal']")
            actual = self.getText(download_pay_button)
            actual = actual.strip()
            expect = '升级VIP免费商用'
            self.assert_text(expect, actual)
        except Exception as e:
            self.logger.error('失败:苏打工作台页面下载升级VIP%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:苏打工作台页面下载升级VIP")
            raise e


    def source_material(self):
        '''点击素材，断言'形状'''
        try:
            source = ('xpath', "//span[@class='iconfont icon-sucai']")
            self.click(source)
            all_of_the = ('xpath', "//section[@class='material-wrap-first']/div[1]/div[1]/p[1]")
            actula = self.getText(all_of_the)
            actual = actula.strip()
            expect = '形状'
            self.assert_text(expect, actual)
        except Exception as e:
            self.logger.error('失败:苏打工作台页面点击素材，断言"形状"%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:苏打工作台页面点击素材，断言'形状'")
            raise e

    def material_other(self):
        '''素材点击'''
        #查看全部
        all_one_material = ('xpath', "//section[@class='material-wrap-first']/div[1]/div[1]/p[2]")
        self.click(all_one_material)
        self.sleep()
        back_button = ('xpath', "//div[@class='material-wrap-type']/p")
        self.click(back_button)
        #素材搜索:手机
        find_button = ('xpath', "//ul[@id='tab-item-list']/li[3]//input[@type='text']")
        self.write(find_button, '手机')
        self.sayok(find_button)
        self.sleep()
        #点击一个形状
        shape = ('xpath', "//section[@class='material-wrap']/ul[1]/li[1]/div")
        self.ptclick(shape)
        self.sleep()



    def words_written(self):
        '''点击文字，断言标题'''
        try:
            words_button = ('xpath', "//span[@class='iconfont icon-wenzi']")
            self.click(words_button)
            tittle = ('xpath', "//button[@name='思源黑体-粗体']")
            self.click(tittle)
            actula = self.getText(tittle)
            actual = actula.strip()
            expect = '点击添加标题'
            self.assert_text(expect, actual)
        except Exception as e:
            self.logger.error('失败:苏打工作台页面点击文字，断言标题"%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:苏打工作台页面点击文字，断言标题'")
            raise e

    def background(self):
        '''点击背景，断言背景'''
        try:
            baclground_button = ('xpath', "//span[@class='iconfont icon-beijing']")
            self.click(baclground_button)
            back_ass = (
                'xpath', "//h6[@class='background-title-color background-title-normal background-imglist-title']")
            actula = self.getText(back_ass)
            actual = actula.strip()
            expect = '图片背景'
            self.assert_text(expect, actual)
            picture = ('xpath', "//div[@class='template-list template-background-left']//li[1]//img[1]")
            self.click(picture)
            self.sleep(10)
            replace_back = ('xpath', "//div[@class='el-upload el-upload--text']/button[@type='button']/span")
            actual2 = self.getText(replace_back)
            expect2 = '替换背景图'
            self.assert_text(actual2, expect2)

        except Exception as e:
            self.logger.error('失败:苏打工作台页面点击背景，断言背景"%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:苏打工作台页面点击背景，断言背景'")
            raise e

    def convenient(self):
        '''便捷上传图片，删除'''
        try:
            convenient_button = ('xpath', "//nav[@id='tabList']//img")
            self.click(convenient_button)
            input_button = ('xpath', "//input[@id='upload-qrcode-img']")
            self.write(input_button, jepg)
            self.sleep()
        except Exception as e:
            self.logger.error('失败:苏打工作台页面便捷上传图片，删除"%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:苏打工作台页面便捷上传图片，删除'")
            raise e

    def realy_input(self):
        '''上传，删除'''
        try:
            input_button = ('xpath', "//ul[@class='guidance-tools']//div[@class='el-upload el-upload--text']/input[@name='file']")
            self.write(input_button, jepg)
            self.sleep()
            ok_button = ('xpath', "//button[@class='el-button design-button-primary el-button--default']")
            self.click(ok_button)
            input_button = (
                'xpath', "//ul[@class='guidance-tools']//div[@class='el-upload el-upload--text']/input[@name='file']")
            self.write(input_button, jepg)
            self.sleep()
            self.sleep(60)
        except Exception as e:
            self.logger.error('失败:苏打工作台页面上传"%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:苏打工作台页面上传'")
            raise e

    def save_temp(self):
        save_name = ('xpath', "//div[@id='app']/header/ul[1]//input")
        self.clear(save_name)
        values = '自动化输入保存的名称'
        self.write(save_name, values)
        self.sleep()
        # self.logger.info("在工作台点击保存按钮，并关闭工作台页面")
        save_button = ('xpath', "//button[@class='save-btn']")
        self.click(save_button)
        self.sleep(2)
        # all_handles = self.driver.window_handles
        # if len(all_handles) > 1:
        #     self.logger.info("开始关闭工作台浏览器窗口")
        #     self.close_and_home_page()



    def ceshi(self):
        right_input = ('xpath', "//div[@id='toolbar-editor-box']//div[@class='el-upload el-upload--text']/input")
        self.write(right_input, jepg)