from pages.basePage import Action
from pages.isheji_c.tempCenterPage.workbenchPage import WorkBench
from common.readLog import Log
from common.sendDingTalk import SendDingTalk


# ======================================================
# 爱设计首页-->模板专题
# https://www.isheji.com/template_column_10_8
# ======================================================
class TempSpecial(Action):
    log = Log(__name__)
    logger = log.getLog()

    def move_to_temp(self):
        firstTempElement = ("xpath", "//div[@class='infinite-list-wrapper']/ul/li[1]")
        self.mouse_hover(firstTempElement)
        self.sleep(1)

    # 测试进入模板精选页
    def test_click_hotTemp(self):
        try:
            hotTempElement = ('xpath', "//div[@id='hottopic']/div[1]/div[1]/div[1]")
            self.click(hotTempElement)
            self.sleep(1)
            self.window(-1)
            url = self.getUrl()
            assert "template_column" in url
        except Exception as e:
            self.logger.error("HomePage:temp_class方法出现了异常信息：%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试在首页--热门精选下点击专题")
            raise e
        self.logger.info("开始关闭打开的图片模板列表页")

    # 在精选模板列表点击模板进入工作台
    def test_hot_temp_view(self, driver):
        try:
            firstTempElement = ('xpath', "//div[@class='infinite-list-wrapper']/ul/li[1]/div")
            self.ptclick(firstTempElement)
            self.sleep(3)
            self.window(-1)
            try:
                self.jump_work()  # 在工作台提示上点击跳过
            except:
                self.logger.info("进入工工作台后，跳过按钮没有出现")
            sucai_text = WorkBench(driver).work_material_text()
            self.sleep(2)
            self.preservation()
            self.sleep(2)
            self.close_and_window()
            sucai_text_ral = str(sucai_text).strip()
            assert sucai_text_ral == "素材"
        except Exception as e:
            self.logger.error("测试从精选模板点击模板进入工作台异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试从精选模板点击模板进入工作台失败")
            raise e

    # 在精选模板列表收藏模板
    def test_hot_temp_coll(self):
        try:
                self.move_to_temp()
                collBtn = ('xpath', "//div[@class='infinite-list-wrapper']/ul/li[1]/div[1]/div[3]/span")
                attr = self.getElementAttr(collBtn, 'class')
                print(attr)
                if attr == "iconfont icon-collected icon-uncollection":
                    print("，没有收藏")
                i = 0
                while i<3:
                    self.ptclick(collBtn)
                    self.sleep(2)
                    tipsElement = ('xpath', "//div[@class='scstauts item-shadow']")
                    tip = self.getText(tipsElement)
                    if tip == "收藏成功":
                        assert tip == "收藏成功"
                        break
                    else:
                        # tip != "收藏成功":
                        i = i + 1
                    # else:
                    #     assert tip == "收藏成功"
                    #     break

            # if attr == "iconfont icon-collected icon-collection":
                i = 0
                print("收藏了")
                while i < 3:
                    self.ptclick(collBtn)
                    self.sleep(2)
                    self.ptclick(collBtn)
                    tipsElement = ('xpath', "//div[@class='scstauts item-shadow']")
                    tip = self.getText(tipsElement)
                    if tip == "收藏成功":
                        assert tip == "收藏成功"
                        break
                    else:
                        # tip != "收藏成功":
                        i = i + 1
                    # else:
                    #     assert tip == "收藏成功"
                    #     break
        except Exception as e:
            self.logger.error("测试从精选模板点击收藏模板异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试从精选模板点击收藏模板失败")
            raise e

    # 在预览页面点击查看(小眼睛)按钮
    def test_hot_temp_see(self):
        try:
            self.move_to_temp()  # 移动到模板上
            seeBtn = ('xpath', "//li[1]//div[1]//div[2]//a[1]//span[1]")
            self.ptclick(seeBtn)
            self.sleep(2)
            self.window(-1)
            quickBtn = ('xpath', "//div[@class='quick_use_btn']")
            buttonName = self.getText(quickBtn)
            assert buttonName == "立即编辑"
            self.sleep(2)
            # self.close_and_window()
            self.close_and_home_page()
        except Exception as e:
            self.logger.error("测试从精选模板预览模板异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试从精选模板预览模板失败")
            raise e
        finally:
            self.close_and_home_page()
