from common.path import psd
from common.path import jepg
from common.readLog import Log
from common.sendDingTalk import SendDingTalk
from pages.basePage import Action


class EnterpirseSpace(Action):
    '''我的企业：企业空间'''
    log = Log(__name__)
    logger = log.getLog()

    def enterprise(self):
        '''进入我的企业'''
        enter = ('xpath', "//a[@id='toggle_team']")
        self.click(enter)
        self.window(-1)

    def design(self):
        '''企业模版'''
        try:
            sp = ('xpath', "//a[@class='router-link-exact-active router-link-active']")
            self.click(sp)
            template = 'template'
            template_url = self.getUrl()
            assert template in template_url
        except Exception as e:
            self.logger.error('我的企业-企业空间--未找到企业模版元素或未进入企业模版%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：我的企业-企业空间--未找到企业模版元素或未进入企业模版")
            raise e

    def mkdir(self):
        '''新建文件夹'''
        try:
            new_file = ('xpath', "//div[@class='tmp-title nav-title']//button[1]//span[1]")
            self.click(new_file)
            file_name = ('xpath', "//input[@placeholder='请输入名称']")
            self.write(file_name, "test_mkdir")
            file_ed = ('xpath',
                       "//div[@class='el-dialog__wrapper rename-dialog']//button[@class='el-button el-button--primary']//span")
            self.click(file_ed)
        except Exception as e:
            self.logger.error('失败：我的企业-企业空间--新建文件夹失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：我的企业-企业空间--新建文件夹失败版")
            raise e

    def upload_modo(self):
        '''点击上传模版'''
        try:
            upload_button = ('xpath', "//div[@class='tmp-title nav-title']//button[2]//span[1]")
            self.click(upload_button)
            upload_file = ('xpath', "//input[@name='file']")
            self.write(upload_file, psd)
        except Exception as e:
            self.logger.error('失败：我的企业-企业空间--上传模版失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：我的企业-企业空间--上传模版失败")
            raise e
        self.sleep()
        try:
            self.jump_work()
        except:
            self.sleep()

    def set_team_modo(self):
        '''设置团队模版'''
        try:
            self.sleep()
            make_set = ('xpath', "//div[@class='set-team-template']")
            self.click(make_set)
            self.sleep(3)
            three_jiao = ('xpath', "//span[@class='el-tree-node__expand-icon el-icon-caret-right']")
            self.click(three_jiao)
            self.sleep(2)
            save_file = ('xpath',"//div[@class='el-tree-node__children']/div[last()]")
            self.click(save_file)
            self.sleep()
            queding = ('xpath',
                       "//button[@class='el-button design-button-primary el-button--default']")
            self.click(queding)
            self.sleep()
            retn = (
                'xpath',
                "//div[@class='el-dialog el-dialog--center design-dialog-364']//div[@class='el-dialog__body']//span")
            self.click(retn)
        except Exception as e:
            self.logger.error('失败：我的企业-企业空间--设置团队模版%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：我的企业-企业空间--设置团队模版")
            raise e

    def inspect(self):
        '''返回'''
        self.sleep()
        self.window(-1)
        self.sleep()

    def material(self):
        '''企业素材'''
        sucai = ('xpath', "//li[2]//ul[1]//li[2]//a[1]//span[1]")
        self.click(sucai)
        self.sleep()
        # 新建文件夹
        self.mkdir()

    def upload_sucai(self):
        '''上传素材'''
        try:
            upload_button = ('xpath', "//div[@class='tmp-title nav-title']//button[2]//span[1]")
            self.click(upload_button)
            upload_file = ('xpath', "//input[@name='file']")
            self.write(upload_file, jepg)
            self.sleep()
            ok_button = ('xpath', "//div[@class='btn-wrap']//button[@class='el-button el-button--primary']//span")
            self.click(ok_button)
            self.sleep()
            self.close_and_window()
            self.close_and_home_page()
            self.sleep()
        except Exception as e:
            self.logger.error('失败：我的企业-企业空间--上传素材%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：我的企业-企业空间--上传素材")
            raise e
