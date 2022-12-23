from common.sendDingTalk import SendDingTalk
from common.path import file_upload
from pages.basePage import Action
from common.readLog import Log
from common.path import vcg


class AiMatting(Action):
    '''智能抠图'''
    log = Log(__name__)
    logger = log.getLog()

    def get_into_matting(self):
        '''进入智能抠图'''
        try:
            matting_botton = ('xpath', "//li[@class='block-item cutout-index']//span[@class='block-text']")
            self.click(matting_botton)
            titlt = ('xpath', "//div[@class='top-area-left']//h1")
            actual = self.getText(titlt)
            expect = '智能抠图'
            self.assert_text(expect, actual)
            self.logger.info('进入智能抠图')
        except Exception as e:
            self.logger.error('失败：智能抠图--未进入智能抠图%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：智能抠图--未进入智能抠图")
            raise e

    def uploadImg(self):
        try:
            input_button = ('xpath', "//body//button[1]")
            self.click(input_button)
            self.sleep(1)
            self.window(-1)
            test = ('xpath',
                    "//button[contains(@class,'el-button el-button--default el-button--small el-button--primary')]//span")
            self.click(test)
            self.sleep()
            file_upload(vcg)
            self.sleep(5)
            self.close_and_home_page()
        except Exception as e:
            self.close_and_home_page()
            self.logger.error('失败：智能抠图--无法在上传图片按钮进入后上传图片或不支持第三方库%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：智能抠图--无法在上传图片按钮进入后上传图片或不支持第三方库")
            raise e

    def experience(self):
        '''体验样图'''
        try:
            self.transfer_url('/cutout/index')
            wxper_button = ('xpath', "//button[2]//span[1]")
            self.click(wxper_button)
            self.sleep()
            self.window(-1)
            # 重新上传
            input_into = ('xpath', "//div[@class='upload-demo']//input[@name='file']")
            self.write(input_into, vcg)
            self.sleep(2)
            enter_button = ('xpath',
                            "//button[contains(@class,'el-button el-button--default el-button--small el-button--primary')]//span")
            self.click(enter_button)
            self.logger.info('智能抠图：体验样图')
        except Exception as e:
            self.logger.error('失败：智能抠图--体验样图失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：智能抠图--体验样图失败")
            raise e

    def background_change(self):
        '''换背景'''
        try:
            back_button = ('xpath', "//div[@class='control-btn']")
            self.click(back_button)
            try:
                # 纯色背景
                for i in range(1, 12):
                    color = ('xpath', f"//div[@class='bg-aside-color-list']//div[{i}]")
                    self.click(color)
                    self.sleep(1)
                    self.logger.info('纯色背景更换成功')
            except Exception as e:
                self.logger.error('失败：智能抠图--纯色背景更换失败%s' % repr(e))
                SendDingTalk().sendDingTalkMsg("失败：智能抠图--纯色背景更换失败")
                raise e
            self.sleep(1)
            try:
                self_def = ('xpath', "//div[@class='img-tag']//input[@name='file']")
                self.write(self_def, vcg)
                for mode in range(2, 7):
                    mode_have = ('xpath', f"//div[@class='bg-aside-img-list-scroll _overflow']//div[{mode}]")
                    self.click(mode_have)
                    self.sleep(1)

            except Exception as e:
                self.logger.error('失败：智能抠图--自定义更换背景失败%s' % repr(e))
                SendDingTalk().sendDingTalkMsg("失败：智能抠图--自定义更换背景失败")
                raise e
        except Exception as e:
            self.logger.error('失败：智能抠图--背景更换失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：智能抠图--背景更换失败")
            raise e

    def download_back(self):
        '''下载功能'''
        try:
            download_button = ('xpath', "//div[contains(@class,'el-dropdown')]//span")
            self.click(download_button)
            try:
                # 保存到我的上传
                my_upload = ('xpath', "//ul[@class='el-dropdown-menu el-popper download-dropdown']//li[1]")
                self.click(my_upload)
            except Exception as e:
                self.logger.error('失败：智能抠图--保存至我的上传%s' % repr(e))
                SendDingTalk().sendDingTalkMsg("失败：智能抠图--保存至我的上传")
                guiwei = ('xpath', "//div[@class='cutout-type-item active']")
                self.click(guiwei)
            self.click(download_button)
            try:
                # 保存至本地
                save_here = ('xpath', "//ul[@class='el-dropdown-menu el-popper download-dropdown']//li[2]")
                self.click(save_here)
                self.sleep()
            except Exception as e:
                self.logger.error('失败：智能抠图--保存至本地%s' % repr(e))
                SendDingTalk().sendDingTalkMsg("失败：智能抠图--保存至本地")
        except Exception as e:
            self.logger.error('失败：智能抠图--下载失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：智能抠图--下载失败")
            raise e

    def unseen_action(self):
        '''上下步和大小'''
        try:
            try:
                # 重置
                reset_action = ('xpath', "//div[@class='reset active']//span")
                self.click(reset_action)
                self.sleep()
                self.logger.info('抠图点击重置')
            except Exception as e:
                self.logger.error('失败：智能抠图--重置失败%s' % repr(e))
                SendDingTalk().sendDingTalkMsg("失败：智能抠图--重置失败")
            try:
                # 上一步
                back_action = ('xpath', "//div[@class='back active']//span")
                self.click(back_action)
                self.logger.info('抠图点击上一步')
                self.sleep()
            except Exception as e:
                self.logger.error('失败：智能抠图--上一步点击失败%s' % repr(e))
                SendDingTalk().sendDingTalkMsg("失败：智能抠图--上一步点击失败")
            self.sleep(1)
            # try:
            #     #下一步
            #     go_action = ('xpath', "//div[@class='go']//span")
            #     self.click(go_action)
            #     self.sleep()
            #     self.logger.info('抠图点击下一步')
            # except Exception as e:
            #     self.logger.error('失败：智能抠图--下一步点击失败%s' % e)
            #     SendDingTalk().sendDingTalkMsg("失败：智能抠图--下一步点击失败")
            # self.sleep(1)
        except Exception as e:
            self.logger.error('失败：智能抠图--上下步和大小失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：智能抠图--上下步和大小失败")
            raise e
        self.sleep(1)
        try:
            try:
                # 放大
                add_button = ('xpath', "//span[@id='add']")
                self.click(add_button)
            except Exception as e:
                self.logger.error('失败：智能抠图--图片放大%s' % repr(e))
                SendDingTalk().sendDingTalkMsg("失败：智能抠图--图片放大")
            self.sleep(1)
            try:
                # 缩小
                sub_button = ('xpath', "//span[@id='sub']")
                self.click(sub_button)
            except Exception as e:
                self.logger.error('失败：智能抠图--图片缩小%s' % repr(e))
                SendDingTalk().sendDingTalkMsg("失败：智能抠图--图片缩小")
            self.sleep(1)
        except Exception as e:
            self.logger.error('失败：智能抠图--尺寸按钮失灵%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：智能抠图--尺寸按钮失灵")
            raise e
        finally:
            self.close_and_home_page()
            self.home_button()
