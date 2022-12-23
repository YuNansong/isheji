from common.sendDingTalk import SendDingTalk
from pages.basePage import Action
from common.readLog import Log


class SubscribeAccount(Action):
    log = Log(__name__)
    logger = log.getLog()

    def info_first_picture(self, name):
        '''验证进入公共号首图功能'''
        try:
            try:
                tmpe_core = ('xpath', "//li[@class='block-item template-tp']//span[@class='block-text']")
                self.click(tmpe_core)
            except:
                tmpe_core = (
                    'xpath', "//li[@class='block-item template-tp block-item-active']//span[@class='block-text']")
                self.click(tmpe_core)
            button_list = self.driver.find_elements('xpath', "//div[@class='search-item-content typelist']/span")
            num = range(1, len(button_list))  # 1-16
            self.logger.info(f'num的值为：{num}')  # -----------
            for i in num:  # 1-16
                all_tutton = ('xpath', "//div[@class='search-item-content typelist']/span[" + str(i) + "]/a")
                actual_no = self.getText(all_tutton)
                self.logger.info(f'actual_no的值为：{actual_no}')  # -----------
                actual = actual_no.strip()
                self.logger.info(f'all_tutton的值为：{all_tutton}')  # -----------
                # print("actual",actual)
                self.logger.info(f'namen的值为：{name}')  # -----------
                # print("name",name)
                if actual == name:
                    self.click(all_tutton)
                    self.sleep()
                    break
                else:
                    continue
        except Exception as e:
            self.logger.error('失败：未进入公共号首/次图%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：未进入公共号首图")
            raise e

    def save_subscribe(self):
        '''验证模版保存至公众号'''
        actual = ""
        one_tmpe = ('xpath', "//body[@class='template-page']/div/div[@class='continer']/div[@class='masonry']/div[1]/div[1]/div[1]")
        self.ptclick(one_tmpe)
        self.sleep()
        self.window(-1)
        try:
            self.jump_work()
        except:
            self.logger.info('进入工作台未出现跳过')
        try:
            # save_button = ('xpath', "//li[@class='hide_wechat']//span[2]")
            # self.click(save_button)
            self.preservation()
            self.sleep(2)
            seve_to_account = ("xpath", "//div[@class='editor-header-account']")
            self.click(seve_to_account)
            download_button = ('xpath', "//button[@class='ant-btn ant-btn-primary editor-download__btn']")
            self.click(download_button)
            self.sleep(2)
            my_name_button = ('xpath', "//div[@class='editor-header-account-modal__list__content']")
            self.click(my_name_button)
            self.sleep(15)
            self.screenshot_new("同步到公众号")
            know_button = ('xpath', "//div[@class='editor-header-account__success-known']")
            actual_no = self.getText(know_button)
            actual = actual_no.strip()
            # print("保存到公众号（不在下载内）获取到的text", actual, "数据类型为", type(actual))
            self.logger.info(f'保存模版至公众号实际结果：{actual}')
            self.click(know_button) # 关闭同步成功弹框
            self.sleep(2)
            # real_save = ('xpath', "//button[@class='save-btn']") # 点击保存模版按钮
            # self.click(real_save)
            self.preservation()
            self.sleep(1)
            self.close_and_home_page()
            assert actual == "知道了"
        except Exception as e:
            self.close_and_home_page()
            self.logger.error(f'失败：模版保存至公众号失败,实际结果为{actual}。%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：模版保存至公众号失败")
            raise e

    def info_qr_code(self):
        '''验证非公众号首图/次图模版保存至公众号'''
        try:
            one_tmpe = (
                'xpath', "//div[@id='waterfall']/div[1]/div[1]/div[1]/div[1]")
            self.ptclick(one_tmpe)
            self.sleep()
            self.window(-1)
            try:
                self.jump_work()
            except:
                self.logger.info('进入工作台未出现跳过')
            # 下载旁的角
            down_triangle = ('xpath', "//div[@class='editor-wechat__btn']//div[@class='icon']//*[local-name()='svg']//*[name()='use' and contains(@class,'icon_conte')]")
            self.click(down_triangle)
            save_WeChat = ('xpath', "//div[@class='editor-wechat__content']")
            self.click(save_WeChat)
            # download_button = ('xpath', "//div[@class='download-btn-dialog']")
            # self.click(download_button)
            my_name_button = ('xpath', "//div[@class='editor-header-account-modal__list__content']")
            self.click(my_name_button)
            self.sleep(10)
            save_success = ('xpath',
                            "//div[@class='editor-header-account__success-known']")
            actual_no = self.getText(save_success)
            actual = actual_no.strip()
            self.logger.info(f'保存模版至公众号实际结果：{actual}')
            # know_button = ('xpath', "//button[@class='wechat_dsbtn']")
            # self.click(know_button)
            # self.sleep(10)
            expect = '知道了'
            self.logger.info(f'保存模版至公众号预期结果:{expect}')
            # real_save = ('xpath', "//button[@class='save-btn']")
            # self.click(real_save)
            self.preservation()
            self.sleep(1)
            self.close_and_home_page()
            self.home_button()
            assert actual == expect
        except Exception as e:
            self.home_button()
            self.close_and_home_page()
            self.logger.error('失败：模版保存至公众号失败(横版二维码)%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：模版保存至公众号失败(横版二维码)")
            raise e
