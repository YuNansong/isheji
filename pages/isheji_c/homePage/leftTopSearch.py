from model.entModel.entTempModel import EntTempModel
from common.readLog import Log
from common.sendDingTalk import SendDingTalk


class LeftSearch(EntTempModel):
    log = Log(__name__)
    logger = log.getLog()

    #  在首页左上角搜索模版
    def searchKey(self, key):
        try:
            lfsea = ('xpath', "//input[@id='header-search']")
            self.write(lfsea, key)
            self.sayok(lfsea)  # 按回车执行搜索
        except Exception as e:
            self.logger.error('失败:在首页左上角搜索模版%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:在首页左上角搜索模版")
            raise e

    def test_get_search_tips(self):
        '''断言：在首页左上角搜索模版'''
        try:
            self.page_down()
            self.sleep(1)
            lfsea = ('xpath', "//input[@id='header-search']")
            text = self.getElementAttr(lfsea, "placeholder")
            return str(text).strip() == "30w+正版素材模板"
        except Exception as e:
            self.logger.error('失败:断言：在首页左上角搜索模版%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:断言：在首页左上角搜索模版")
            raise e

    def left_search(self, key):
        '''左上角搜索框'''
        try:
            self.page_down()  # 鼠标向下滑动，才会出现搜索框
            self.sleep(1)
            self.searchKey(key)
            self.sleep(5)
            keyElement = ('xpath', "//div[@class='keyword']/span")
            text = self.getText(keyElement)
            self.logger.info("在模板搜索结果页获取到的关键字为%s" % text)
            assert str(text).strip() == key
        except Exception as e:
            self.logger.error('失败:左上角搜索框%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:左上角搜索框")
            raise e

    # 在搜索结果页面进入模版
    def clickTempOfSearchResultView(self,driver):
        self.logger.info("在模板搜索结果页进入工作台页面")
        try:
            self.sleep(2)
            temp_element = ('xpath', "//div[@id='waterfall']/div[1]/div[1]/div[1]/div[1]")  # 在模板列表点击模板
            self.ptclick(temp_element)
            self.window(-1)
            self.sleep(5)
            try:
                try:
                    self.jump_home()  # 在工作台提示上点击跳过
                except:
                    self.preservation()  # 点击保存按钮
                    self.logger.info("进入工作台跳过按钮没有出现")
                # 断言: 进入工作台查看是否显示模板
                tempId = self.get_temp_id(driver)
                assert int(tempId) > 0
                self.save_temp(driver)  # 点击保存按钮
            except:
                self.logger.info("进入工作台失败")
            self.close_handle()
        except Exception as e:
            SendDingTalk().sendDingTalkMsg("测试从搜索结果页点击模板进入工作台页面失败")
            raise e
