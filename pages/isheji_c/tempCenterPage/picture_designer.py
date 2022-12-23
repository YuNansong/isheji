from common.sendDingTalk import SendDingTalk
from pages.basePage import Action
from common.readLog import Log


class PictureDesigner(Action):
    log = Log()
    logger = log.getLog()

    def picture_designer(self):
        '''进入我的图片创作'''
        try:
            try:
                join_button = ('xpath', "//li[@class='block-item mycreation']//span[@class='block-text']")  # 首页--我的图片创作
                self.click(join_button)
                self.sleep()
                fving = ('xpath', "//h3[@class='create-item-title']")
                actual = self.getText(fving)
                expect = '我的图片创作'
                self.assert_text(expect, actual)
            except:
                self.logger.info('没有进入我的图片创作：未找到断言所需元素')
                self.sleep(1)
        except Exception as e:
            self.logger.error('失败：进入我的图片创作%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：进入我的图片创作")
            raise e

    def new_design(self):
        '''新建设计，进入工作台'''
        try:
            new_button = ('xpath', "//div[@class='create-new']")
            self.click(new_button)
            select_mode = ('xpath', "//li[@id='wx-qrcode']//img")
            self.click(select_mode)
            self.window(-1)
            self.sleep(5)
            try:
                self.jump_work()
            except:
                self.logger.info("进入工作台跳过按钮没有出现")
                self.sleep(1)
            backMyDesign = ('xpath', "//button[@class='show-return return-btn']")
            text = self.getText(backMyDesign)
            assert str(text).strip() == "返回我的创作"
        except Exception as e:
            self.logger.error('失败：新建设计，进入工作台%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：新建设计，进入工作台")
            raise e

    def submitApply(self):
        # 提交审核
        try:
            submit_button = ('xpath', "//button[@id='design-show-btn']")
            self.ptclick(submit_button)
            self.sleep(10)
        except Exception as e:
            self.logger.error('失败：图片创作提交审核%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：图片创作提交审核")
            raise e

    # def input_backgriund_picture(self):
    #     '''上传背景图'''
    #     input_backgriund_picture_button = ('xpath',
    #         "//div[@class='actbtn-box']//button[@class='el-button el-button--default']")
    #     self.click(input_backgriund_picture_button)
    #     logo = ('xpath', "//dd[contains(text(),'LOGO')]")
    #     self.click(logo)
    #     logo_back = ('xpath', "//ul[@class='clip-logo-ul']/li[last()]")
    #     self.click(logo_back)
    #     self.sleep(5)
    #     #提交审核
    #     submit_button = ('xpath', "//button[@id='design-show-btn']")
    #     self.ptclick(submit_button)
    #     self.sleep(10)

    def submit_to_rxamine(self):
        '''提交审核填写资料'''
        try:
            self.submitApply()
            # 标题
            tittle = ('xpath', "//input[@name='designTitle']")
            self.clear(tittle)
            self.sleep(1)
            say_songthing = '(不用通过)自动化测试输入'
            self.write(tittle, say_songthing)
            # 关键字(空格确认)
            basbou = ('xpath', "//div[@class='bootstrap-tagsinput']//input[@placeholder='输入后空格确认']")
            say_konmen1 = '自动化 测试 输入 关键字 忽略 '
            self.write(basbou, say_konmen1)

            # 模版字段
            self.sleep(2)
            mode_str = ('xpath', "//input[@placeholder='请输入模板中的字段']")
            say_mode = '简约'
            self.write(mode_str, say_mode)

            # 选择用途
            self.sleep(2)
            purpose = ('xpath', "//form[@novalidate='novalidate']/div[4]/div[1]/label[1]")
            self.click(purpose)
            # 选择场景
            self.sleep(2)
            scene = ('xpath', "//div[@class='multiple-box-scene multiple-box']//label[@id='child_14']")
            self.click(scene)

            # 另一个一个用途
            self.sleep(2)
            other_purpose = ('xpath', "//div[@class='multiple-box-purpose multiple-box']//label[@id='child_2']")
            self.click(other_purpose)

            # 行业
            self.sleep(2)
            industry = ('xpath', "//div[@class='multiple-box-industry multiple-box']//label[@id='child_2']")
            self.click(industry)

            self.page_down()
            # 老风格
            self.sleep(2)
            old_style = ('xpath', "//div[@class='old-style']//label[2]")
            self.click(old_style)

            # 新风格
            self.sleep(2)
            new_style = ('xpath', "//div[@class='new-style']//label[2]")
            self.click(new_style)

            # 旧颜色
            self.sleep(2)
            old_colour = ('xpath', "//div[@class='old-color']//li[1]")
            self.click(old_colour)

            # 新颜色
            self.sleep(2)
            new_colour = ('xpath', "//div[@class='new-color']//li[1]")
            self.click(new_colour)

            # 提交审核
            self.sleep(2)
            up_button = ('xpath', "//form[@novalidate='novalidate']/button")
            self.click(up_button)

            # 返回我的创作
            self.sleep(8)

            back_my_design = ('xpath', "//div[@class='confirm-btn-list']/button[2]")
            text = self.getText(back_my_design)
            assert text == "返回我的创作"
        except Exception as e:
            self.logger.error('失败：设计师上传图片：提交审核填写资料%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：设计师上传图片：提交审核填写资料")
            raise e

    def back_my_design(self):
        '''返回到我的设计，并关闭窗口'''
        self.logger.info("进入到首页，开始测试我的创作")
        try:
            back_my_design_btn = ('xpath', "//section[@id='mask']//button[2]")
            # self.click(back_my_design_btn)
            self.driver.close()
            self.window(0)
            self.refresh()
            assert True
        except:
            self.logger.info("提交材料后，返回我的设计出现异常")
            assert False

    def draft(self):
        '''关闭填写页面，保存草稿'''
        xbutton = ('xpath', "//img[@class='close-download-btn']")
        self.click(xbutton)
        self.preservation()
        self.sleep()
        self.back_my_design()

    def make_drafts(self):
        '''制造草稿'''
        try:
            for num in range(1, 4):
                # 新建设计
                self.new_design()
                self.sleep()
                self.submitApply()
                self.draft()
                self.logger.info("第%d个草稿"%num)
        except Exception as e:
            self.logger.error('失败：设计师图片创作--制造草稿%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：设计师图片创作--制造草稿")
            raise e

    def cuntiue_design(self):
        '''继续设计'''
        try:
            cuntiue_button = ('xpath',"//div[@class='creation-content-list']/ul/li[1]//button[1]")
            self.click(cuntiue_button)
            self.window(-1)
            self.sleep(5)
            try:
                self.jump_work()
            except:
                self.logger.info("进入工作台跳过按钮没有出现")
                self.sleep(1)
            backMyDesign = ('xpath', "//button[@class='show-return return-btn']")
            text = self.getText(backMyDesign)
            assert str(text).strip() == "返回我的创作"
            # 提交审核
            # self.submitApply()
            # 填写资料
            self.submit_to_rxamine()
            # 回到我的设计
            self.back_my_design()
        except Exception as e:
            self.logger.error('失败：设计师图片创作--继续设计%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：设计师图片创作--继续设计")
            raise e

    def submit_for_review(self):
        '''提交审核'''
        try:
            submitbutton = ('xpath', "//li[1]//div[6]//section[1]//button[2]")
            self.click(submitbutton)
            # 填写资料
            self.no_submit()
            self.refresh()
        except Exception as e:
            self.logger.error('失败：设计师图片创作--提交审核%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：设计师图片创作--提交审核")
            raise e

    def delete_design(self):
        '''删除'''
        try:
            deletebutton = ('xpath', "//li[1]//div[6]//section[1]//button[3]")
            self.click(deletebutton)
            remove_true = ('xpath', "//button[@class='remove_true']")
            self.click(remove_true)
        except Exception as e:
            self.logger.error('失败：设计师图片创作--删除%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：设计师图片创作--删除")
            raise e
        self.home_button()

    def no_submit(self):
        '''页面提交审核'''
        try:
            tittle = ('xpath', "//input[@name='designTitle']")
            self.clear(tittle)
            self.sleep(1)
            say_songthing = '(不用通过)自动化测试输入'
            self.write(tittle, say_songthing)
            # 关键字(空格确认)
            basbou = ('xpath', "//div[@class='bootstrap-tagsinput']//input[@placeholder='输入后空格确认']")
            say_konmen1 = '自动化 测试 输入 关键字 忽略 '
            self.write(basbou, say_konmen1)

            # 模版字段
            self.sleep(2)
            mode_str = ('xpath', "//input[@placeholder='请输入模板中的字段']")
            say_mode = '简约'
            self.write(mode_str, say_mode)

            # 选择用途
            self.sleep(2)
            purpose = ('xpath', "//form[@novalidate='novalidate']/div[4]/div[1]/label[1]")
            self.click(purpose)
            # 选择场景
            self.sleep(2)
            scene = ('xpath', "//div[@class='multiple-box-scene multiple-box']//label[@id='child_14']")
            self.click(scene)

            # 另一个一个用途
            self.sleep(2)
            other_purpose = ('xpath', "//div[@class='multiple-box-purpose multiple-box']//label[@id='child_2']")
            self.click(other_purpose)

            # 行业
            self.sleep(2)
            industry = ('xpath', "//div[@class='multiple-box-industry multiple-box']//label[@id='child_2']")
            self.click(industry)

            self.page_down()
            # 老风格
            self.sleep(2)
            old_style = ('xpath', "//div[@class='old-style']//label[2]")
            self.click(old_style)

            # 新风格
            self.sleep(2)
            new_style = ('xpath', "//div[@class='new-style']//label[2]")
            self.click(new_style)

            # 旧颜色
            self.sleep(2)
            old_colour = ('xpath', "//div[@class='old-color']//li[1]")
            self.click(old_colour)

            # 新颜色
            self.sleep(2)
            new_colour = ('xpath', "//div[@class='new-color']//li[1]")
            self.click(new_colour)

            # 提交审核
            self.sleep(2)
            up_button = ('xpath', "//form[@novalidate='novalidate']/button")
            self.click(up_button)

            # 关闭窗口
            x_button = ('xpath', "//div[@id='exsuccess']//div[@class='close']//img")
            self.click(x_button)

        except Exception as e:
            self.logger.error('失败：设计师申请提交：提交审核填写资料%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：设计师申请提交：提交审核填写资料")
            raise e
