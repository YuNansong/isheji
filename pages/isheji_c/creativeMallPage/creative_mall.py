from common.sendDingTalk import SendDingTalk
from common.readLog import Log
from pages.basePage import Action


class CreativeMall(Action):
    log = Log()
    logger = log.getLog()

    # 创意热店搜索，进入热店页面在测试类中控制
    def find_key_word(self):
        find_box = ('xpath', "//div[@class='search banner-search']//input[@placeholder='请搜索服务类型、标签等关键词']")
        key = '插画'
        self.write(find_box, key)
        try:
            try:
                # 搜索按钮
                open_jing = ('xpath', "//div[@class='search banner-search']//i[@class='iconfont icon-sousuo1']")
                self.click(open_jing)
            except Exception as e:
                self.sayok(find_box)
                self.logger.error('失败：创意热店--搜索框放大镜按钮%s' % repr(e))
                SendDingTalk().sendDingTalkMsg("失败：创意热店--搜索框放大镜按钮")
        except Exception as e:
            self.logger.error('失败：创意热店--搜索框无法搜索%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：创意热店--搜索框无法搜索")
            raise e
        self.sleep()
        '''搜索结果断言'''
        out_word = ('xpath', "//span[@class='weight']")
        actual = self.getText(out_word)
        expect = '"插画"'
        self.assert_text(expect, actual)

    def screen(self):
        '''四个筛选后点击'''
        # 创意类型
        try:
            # 第一个筛选
            screen_one = ('xpath',"//div[@class='select-list']/div[1]/span[1]")
            self.click(screen_one)
            one_son = ('xpath', "//body/div[@class='el-popover el-popper custom-item-popover']/div[@class='item-popover-inner']/div[2]")
            self.click(one_son)
            self.sleep(1)
            # 第二个筛选
            screen_two = ('xpath',"//div[@class='select-list']/div[2]/span[1]") # SKU的选项
            self.click(screen_two)
            self.sleep(1)
            two_son = ('xpath',"//body/div[6]/div[1]/div[2]")
            sku_type_value = self.getText(two_son)
            # print(sku_type_value)
            self.click(two_son)
            self.sleep(1)
            # 点击作品标题，进入详情页
            recommend_onebutton = ('xpath', "//div[@class='product-list mh450']/div[1]/div[1]/div[2]/div[1]/p[1]")
            self.click(recommend_onebutton)
            self.sleep(1)
            # 获取作品详情的创意SKU
            sku_type_xpath = ('xpath',"//div[@class='main-inner-r-top']/div[@class='sku-type'][4]/div[1]/span")
            element_list = self.getElements(sku_type_xpath)
            # print("list>>>>>>>", type(element_list), element_list)
            list_len = len(element_list)
            if list_len > 1:
                for i in range(1, list_len):
                    # print(i)
                    assert_tip = ("xpath", "//div[@class='main-inner-r-top']/div[@class='sku-type'][4]/div[1]/span["+str(i)+"]")
                    str_tip = self.getText(assert_tip)
                    # print(str_tip.strip())
                    # print(sku_type_value.strip())
                    if str_tip.strip() == sku_type_value.strip():
                        break
                    else:
                        continue
            else:
                assert_tip = (
                "xpath", "//div[@class='main-inner-r-top']/div[@class='sku-type'][4]/div[1]/span[" + str(i) + "]")
                str_tip = self.getText(assert_tip)
                self.assert_text(str_tip.strip(), sku_type_value.strip())

            # for i in element_list:
            #     print(i)
            #     sku_type = self.getText(i)
            #     if str(sku_type_value).strip() == str(sku_type).strip():
            #         break
            #     else:
            #         continue
            # assert str(sku_type_value).strip() == str(sku_type).strip()
        # except Exception as e:
        #     self.logger.error('失败：创意热店--筛选平面插画%s' % repr(e))
        #     SendDingTalk().sendDingTalkMsg("失败：创意热店--筛选平面插画")
        #     raise e
        # self.sleep(1)
        # # 所属行业
        # try:
        #     self.back()
        #     screen_three = ('xpath', "//div[@class='select-list']/div[3]")
        #     self.click(screen_three)
        #     three_son = ('xpath', "//div[@role='tooltip']//div[contains(text(),'新消费')]")
        #     self.click(three_son)
        # except Exception as e:
        #     self.logger.error('失败：创意热店--筛选所处行业%s' % repr(e))
        #     SendDingTalk().sendDingTalkMsg("失败：创意热店--筛选所处行业")
        #     raise e
        # self.sleep(1)
        # try:
        #     screen_four = ('xpath', "//div[@class='select-list']/div[4]")
        #     self.click(screen_four)
        #     four_son = ('xpath', "//div[@role='tooltip']//div[contains(text(),'复古')]")
        #     self.click(four_son)
        except Exception as e:
            self.logger.error('失败：创意热店--筛选设计风格%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：创意热店--筛选设计风格")
            raise e
        # picture = ('xpath', "//div[@class='product-list-inner']//div[1]//div[1]//div[1]//img[1]")
        # self.click(picture)

    def recommend(self):
        '''右下：问价、服务推荐和更多按钮'''
        # 询问价格
        try:
            # 问价
            inquiry = ('xpath', "//div[@class='nav-tab']/div[@class='xunjia' and contains(text(),'询价')]")
            self.click(inquiry)
            # 关掉窗口
            x_but = ('xpath', "//span[@class='iconfont icon-no close_button']")
            self.click(x_but)
            # 再问
            self.click(inquiry)
            self.sleep(2)
            # 断言出现询价
            phono_tip = ('xpath', "//div[@class='consult-dialog-modal-r']//h1[@class='title']")
            actual = self.getText(phono_tip)
            actual = actual.strip()
            expect = '询价'
            self.assert_text(expect, actual)

        except Exception as e:
            self.logger.error('失败：创意热店--询问价格出错%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：创意热店--询问价格出错")
            raise e
        cancel_button = ('xpath', "//div[@class='cancel-btn']")
        self.click(cancel_button)
        try:
            # 服务推荐第一个
            recommend_onebutton = ('xpath', "//div[@class='product-list']/div[1]/div[1]/div[2]/div[1]/p[1]")
            actual = self.getText(recommend_onebutton)
            self.click(recommend_onebutton)
            self.sleep()
            title = ('xpath', "//div[@class='title']")
            expect = self.getText(title)
            self.assert_text(expect, actual)
        except Exception as e:
            self.logger.error('失败：创意热店--服务推荐进入后与标题不符%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：创意热店--服务推荐进入后与标题不符")
            raise e
        self.sleep()
        try:
            more_button = ('xpath', "//p[@class='too-more']//a[contains(text(),'更多')]") # 右侧更多按钮
            self.click(more_button)
            self.sleep()
            title = ('xpath', "//div[@class='title']//h1")
            actual = self.getText(title)
            expect = '服务推荐'
            self.assert_text(expect, actual)
        except Exception as e:
            self.logger.error('失败：创意热店--未来返回服务推荐%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：创意热店--未来返回服务推荐")
            raise e

    def right_top_seach(self):
        '''创意热店右上角搜索'''
        try:
            seach_input = ('xpath', "//input[@class='el-input__inner']")
            key = '插画'
            self.write(seach_input, key)
            # 放大镜
            magnifier = ('xpath', "//i[@class='iconfont icon-sousuo1']")
            self.click(magnifier)
            self.sleep()
        except Exception as e:
            self.logger.error('失败：创意热店--右上角搜索按钮%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：创意热店--右上角搜索按钮")
            raise e
        # 返回创意热店首页
        logo_button = ('xpath', "//a[@class='logo active']")
        self.click(logo_button)
        # self.driver.close()
        self.window(0)

    # def all_commodity(self):
    #     '''爱设计创意商品所有商品'''
    #     try:
    #         one_commodity = ('xpath', "//div[@class='cate-list-inner']/div[1]")
    #         self.click(one_commodity)
    #         for com in range(2, 10):
    #             other_com = f"//div[@class='cate-list-inner']/div[{com}]"
    #             self.move_to_stay(other_com)
    #
    #     except Exception as e:
    #         self.logger.error('失败：创意热店--首页商品按钮列点击失败%s' % e)
    #         SendDingTalk().sendDingTalkMsg("失败：创意热店--首页商品按钮列点击失败")
