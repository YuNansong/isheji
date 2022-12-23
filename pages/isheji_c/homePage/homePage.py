import time
from pages.basePage import Action
from pages.isheji_c.vipPage.personalVipPage import PersonalVip
from pages.isheji_c.tempCenterPage.workbenchPage import WorkBench
from pages.entPage.enterpriseVipPage import EnterpriseVipPage
from common.readLog import Log
from common.getYaml import url
from common.sendDingTalk import SendDingTalk
from element.isheji_c.home.homePageElement import HomePageElement
from element.isheji_c.cooperation.cooperationElement import CooperationElement
from element.isheji_c.api.apiElement import ApiElement
from element.isheji_c.aiBuckleDiagram.aiCutoutPicElement import AiCutoutPicElement
from element.isheji_c.ideamall.ideaMall import IdeaMall


# ======================================================
# 爱设计首页定位元素功能
# https://www.isheji.com
# ======================================================

class HomePage(Action):
    log = Log(__name__)
    logger = log.getLog()

    # ====================================================================
    # 测试首页的搜索功能
    # ====================================================================

    # 获取搜索框中的tips
    def test_get_search_tips(self):
        attr = self.getElementAttr(HomePageElement.search_element, "placeholder")
        self.screenshot_new("04搜索页面")
        self.logger.info('首页banner显示为:%s' % attr)
        assert attr == "30W+正版素材模板"

    # 测试搜索
    def test_home_banner_search(self):
        self.logger.info("==========开始执行首页Banner处的搜索功能")
        key = "七夕"
        try:
            self.write(HomePageElement.search_element, key)
            self.ptclick(HomePageElement.searchBtn_element)
            self.sleep()
            self.window(-1)
            actual_text = self.getText(HomePageElement.key_element)
            self.screenshot_new("05搜索结果页面")
            actual = actual_text.strip()
            self.close_and_home_page()
            self.logger.info("获取到的关键字为:%s" % actual)
            assert actual == key
        except Exception as e:
            self.screenshot_new("06搜索结果页面出现异常")
            self.logger.error("在首页测试搜索获取元素失败%s" % repr(e))
            actual = ""
            self.logger.error(f'获取到的key为：{key}%s' % repr(e))
            assert actual == key
        self.close_handle()

    # ====================================================================
    # 测试在首页搜索后进入结果页点击模板功能
    # ====================================================================

    def click_temp(self, i):
        '''在首页每个分类下 点击第1个模板'''
        try:
            # pictr = ('xpath',"//div[@id='waterfall']/div[1]")
            # 在首页每个分类下 点击第1个模板
            self.logger.info("//div[@id='apptc']/div[@class='vertical'][" + str(i) + "]/div[2]/div[1]/div[1]/div[1]")
            # pictr = ('xpath', "//div[@id='nav-content" + str(i) + "']/div/div[1]")
            try:
                pictr = (
                'xpath', "//div[@id='apptc']/div[@class='vertical'][" + str(i) + "]/div[2]/div[1]/div[1]/div[1]")
                self.click(pictr)
            except:
                pictr = (
                'xpath', "//div[@id='apptc']/div[@class='vertical'][" + str(i) + "]/div[1]/div[1]/div[1]/div[1]")
                self.click(pictr)
            self.sleep(5)
            self.screenshot_new("07进入工作台页面")
            self.window(-1)
        except Exception as e:
            self.screenshot_new("07进入工作台失败")
            self.logger.error("在搜索结果页面点击某一个模版失败-----%s" % str(e))
            raise e

    # 点击首页模板进入工作台并保存
    def test_click_index_temp(self, driver):
        sucai_text = ""
        temp_class = self.getElements(HomePageElement.temp_class_element)
        num = len(temp_class)
        self.logger.info("在首页获取到的模板分类一共有 %d 个" % num)
        for i in range(1, num, 4):
            self.click_temp(i)
            try:
                WorkBench(driver).jump_home()  # 在工作台提示上点击跳过
            except:
                self.logger.info("进入工工作台后，跳过按钮没有出现")
            try:

                # 进入工作台查看是否显示素材文案
                sucai_text = WorkBench(driver).work_material_text()
                self.logger.info("进入工作台获取到的素材名称:%s" % sucai_text)
                WorkBench(driver).save_btn()
                self.close_handle()
            except:
                self.logger.error("进入模版失败")
                self.screenshot_new("07进入工作台失败02")  # 截图
                self.close_handle()
            try:
                assert str(sucai_text).strip() == "素材"
            except Exception as e:
                SendDingTalk().sendDingTalkMsg("测试首页点击模板进入工作台失败 i = " + str(i))
                raise e

    # ====================================================================
    # 在模板列表，点击翻页功能
    # ====================================================================
    def tempList_page(self):
        self.page_down(5000)
        # 开始执行翻页功能
        nextPageList = self.getElements(HomePageElement.nextPageElement)  # 返回nextPageElement元素列表，用于循环
        self.logger.info("获取到总页数:%d" % len(nextPageList))
        # 如果nextPageList返回的列表大于1，则点击第二页与最后一页，下一页，上一页
        if nextPageList.__len__() > 1:
            self.click(HomePageElement.lastPageBtn)  # 点击翻页的最后一页
            self.sleep(3)
            self.click(HomePageElement.firstPageBtn)  # 点击翻页的第一页
            self.sleep(3)
            self.click(HomePageElement.nextPageBtn)  # 点击下一页按钮
            self.sleep(3)
            self.click(HomePageElement.upPageBtn)  # 点击上一页按钮
            self.sleep(3)
        else:
            self.logger.info("进入模板列表翻页小于等于一页")

    # ====================================================================
    # 在首页点击模版分类按钮--Banner下的
    # ====================================================================

    # 模板分类下的右滑按钮
    def right_slip(self):
        self.click(HomePageElement.right_btn_element)  # 点击右滑按钮
        self.sleep()

    # 测试点击各个模板分类
    def test_temp_class(self):
        class_xpath = ('xpath', "//div[@id='sence-list-box']/div[1]/div[1]/div")
        num = len(self.getElements(class_xpath))
        for i in range(1, num, 2):
            try:
                if i in [5, 9, 13, 17, 21]:
                    # 当循环到第6,10,14,18个分类时点击右滑按钮，否则小屏幕无法点击后面的分类
                    self.logger.info("开始执行右滑操作i=%d" % i)
                    self.right_slip()
                if i == 1:
                    text = self.getText(HomePageElement.elementText_element)
                    self.logger.info("开始在首页点击模板分类%s按钮" % text)
                    self.click(HomePageElement.elementText_element)
                    self.sleep(3)
                    self.window(-1)  # 切换到新窗口
                    # 当i=1是 是开始作图，跳转到https://www.isheji.com/design
                    # 进入到该页面，定位第一个分类"新媒体配图"
                    urlInfo = url['url']['testUrl']
                    domain = self.getUrl()
                    if urlInfo + "design" in domain:
                        text = self.getText(HomePageElement.new_media_element)
                        self.logger.info("进入到/design页面获取到的内容%s" % text)
                        print(str(text).strip())
                        assert str(text).strip() == "新媒体配图"
                else:
                    elementText = ('xpath', "//div[@id='sence-list-box']/div[1]/div[1]/div[" + str(i) + "]/a/div[2]/h6")
                    text = self.getText(elementText)
                    self.logger.info("开始在首页点击模板分类%s按钮" % text)
                    self.click(elementText)
                    self.sleep(3)
                    self.window(-1)  # 切换到新窗口
                    # 点击开始作图跳转的页面不是模板列表，都是模板分类，所以只有循环到2的时候 才能进行翻页
                    if i in [3, 7]:
                        urlInfo = url['url']['testUrl']
                        domain = self.getUrl()
                        if urlInfo + "template" in domain:
                            self.tempList_page()
            except Exception as e:
                self.logger.error("点击各个模板分类方法出现了异常信息：%s" % repr(e))
                SendDingTalk().sendDingTalkMsg("测试首页下各个分类下的模板失败")
                raise e
            self.logger.info("开始关闭打开的图片模板列表页")
            print(self.driver.window_handles, "111111111111111111111111")
            self.close_handle()
            print(self.driver.window_handles, "222222222222222222222222")

    # ====================================================================
    # 在首页顶部导航，点击个人VIP Tab
    # ====================================================================

    # 在导航点击个人VIP菜单
    def clickPersonalVip(self):
        try:
            self.ptclick(HomePageElement.cvip_element)
        except Exception as e:
            self.ptclick(HomePageElement.per_vip_element)

    # 测试在导航点击个人VIP
    def test_click_per_vip(self):
        try:
            self.logger.info("==========开始在爱设计首页顶部导航点击个人VIP菜单")
            self.clickPersonalVip()
            self.sleep(2)
            urlInfo = url['url']['testUrl']
            domain = self.getUrl()
            self.sleep(2)
            self.home_button()
            assert urlInfo + "/vip" in domain
        except Exception as e:
            self.logger.error('在首页顶部导航点击个人VIP菜单异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("在首页顶部导航点击个人VIP菜单失败")
            raise e

    # 测试悬浮到导航的个人VIP菜单开通VIP
    def test_open_per_vip_floating_layer(self, driver):
        self.logger.info("开始测试悬浮到导航的个人VIP菜单【开通VIP】按钮")
        user = PersonalVip(driver).getUserVip()
        print("函数内user",user)
        self.sleep()
        # iframe
        # iframe_body = ("xpath", "//iframe[@id='login-iframe']")
        # self.switch_iframe(iframe_body)
        # 鼠标浮到导航菜单--VIP菜单
        # self.move_to_stay(HomePageElement.vip_element)
        move_ready = ("xpath", HomePageElement.vip_element)
        self.mouse_hover(move_ready)
        print("悬浮？")
        self.sleep(2)
        # 将鼠标浮到个人VIP菜单，点击开通会员按钮
        self.ptclick(HomePageElement.open_vip_btn)

        if user[0] == 1 and user[1] == 2:
            value = PersonalVip(driver).errorTips()
            try:
                assert value == "已是终身会员"
            except Exception as e:
                self.logger.error("终身会员悬浮到导航的个人VIP菜单,点击开通VIP异常%s" % repr(e))
                SendDingTalk().sendDingTalkMsg("终身会员悬浮到导航的个人VIP菜单,点击开通VIP失败")
        else:
            value = PersonalVip(driver).getPayMoney()
            PersonalVip(driver).closePayFrame()
            if value != None:
                try:
                    assert float(value) > 0
                except Exception as e:
                    self.logger.error("用户悬浮到导航的个人VIP菜单,点击开通VIP失败%s" % repr(e))
                    SendDingTalk().sendDingTalkMsg("用户悬浮到导航的个人VIP菜单,点击开通VIP失败")
                    raise e
        # self.out_of_iframe()

    # 测试悬浮到导航的个人VIP菜单点击详细特权
    def test_privilege_detail_floating_layer(self):
        self.logger.info("开始测试悬浮到导航的个人VIP菜单点击详细特权")
        # self.move_to_stay(HomePageElement.vip_element)
        move_ready = ("xpath", HomePageElement.vip_element)
        self.mouse_hover(move_ready)
        self.sleep(1)
        self.ptclick(HomePageElement.detail_element)  # 点击详情特权
        self.sleep(2)
        urlInfo = url['url']['testUrl']
        print("urlInfo", urlInfo)
        domain = self.getUrl()
        print(domain)
        self.home_button()
        try:
            assert urlInfo + "/vip?order_t=select" in domain
        except Exception as e:
            self.logger.error("用户悬浮到导航的个人VIP菜单,点击详细特权%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("用户悬浮到导航的个人VIP菜单,点击详细特权失败")
            raise e

    # 在首页点击导航的企业解决方案菜单
    def test_click_ent_vip(self, driver):
        try:
            self.click(HomePageElement.enterprise_vip)
            self.sleep(2)
            self.window(-1)
            EnterpriseVipPage(driver).safe()
            self.sleep(2)
            self.window(-1)
            # text = EnterpriseVipPage(driver).getQiyeVipContent()
            url = self.getUrl()
            assert  url == "https://qiye.isheji.com/"
            self.close_handle()
        except Exception as e:
            self.logger.error("用户在首页点击导航的企业解决方案菜单异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("用户在首页点击导航的企业解决方案菜单失败")
            raise e

    # 在首页悬浮到导航的企业解决方案菜单，点击查看详情
    def test_click_ent_flayer_detail(self, driver):
        try:
            self.mouse_hover(HomePageElement.enterprise_vip)  # 鼠标滑动到企业解决方案菜单上
            self.sleep(2)
            self.click(HomePageElement.enterprise_vip_flayer_detail)
            self.window(0)
            url = self.getUrl()
            assert  url == "https://qiye.isheji.com/"
            self.back()
            self.sleep(2)
        except Exception as e:
            self.logger.error("用户在首页悬浮到导航的企业解决方案菜单，点击查看详情异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("用户在首页悬浮到导航的企业解决方案菜单，点击查看详情失败")
            raise e

    # 在首页悬浮到导航的企业解决方案菜单，点击查看详情按钮
    def test_click_ent_flayer_detailBtn(self):
        try:
            # self.move_to_stay(HomePageElement.enterprise_vip_element)
            move_ready = ("xpath", HomePageElement.enterprise_vip_element)
            self.mouse_hover(move_ready)
            self.sleep(2)
            self.click(HomePageElement.enterprise_vip_flayer_detailBtn)
            self.sleep()
            self.window(0)
            url = self.getUrl()
            assert url in "https://qiye.isheji.com/"
            self.back()
            self.sleep(2)
        except Exception as e:
            self.logger.error("用户在首页悬浮到导航的企业解决方案菜单，点击查看详情按钮异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("用户在首页悬浮到导航的企业解决方案菜单，点击查看详情失败")
            raise e

    # 点击导航的合作菜单
    def test_click_cooperation_menu(self):
        try:
            self.mouse_hover(HomePageElement.more_button_element)
            self.click(HomePageElement.cooperation_element)
            self.sleep(2)
            self.window(0)
            urlInfo = url['url']['testUrl']
            domain = self.getUrl()
            if urlInfo + "/cooperation" in domain:
                text = self.getText(CooperationElement.add_service_btn_element)  # 申请成为服务商按钮
                assert str(text).strip() == "申请成为服务商"
        except Exception as e:
            self.logger.error("用户在导航点击合作菜单异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("用户在导航点击合作菜单失败")
            raise e

    # 点击导航的API菜单
    def test_click_api_menu(self):
        self.mouse_hover(HomePageElement.more_button_element)
        self.click(HomePageElement.api_menu_element)
        self.sleep()
        self.window(0)
        urlInfo = url['url']['testUrl']
        domain = self.getUrl()
        if urlInfo + "/apipage" in domain:
            text = self.getText(ApiElement.api_introduce_element)
            self.home_button()  # 返回到首页
            try:
                text_ral = str(text).strip()
                assert text_ral == "API简介"
            except Exception as e:
                self.logger.error("用户在导航点击API菜单异常%s" % repr(e))
                SendDingTalk().sendDingTalkMsg("用户在导航点击API菜单失败")
                raise e

    # 创意热店
    def test_act_ideamall(self):
        try:
            self.click(HomePageElement.idea_button_element)
            self.sleep()
            self.window(-1)
            # 断言左上角字符串
            actual = self.getText(IdeaMall.mall_title_element)
            expect = '爱设计创意商品'
            self.assert_text(expect, actual)
            url = self.getUrl()
            if 'https://idea.isheji.com' in url :
                SendDingTalk().sendDingTalkMsg("创意热店在线上环境")
            else:
                SendDingTalk().sendDingTalkMsg(f'创意热店地址：{url}')
            self.close_handle()
        except Exception as e:
            self.logger.error('失败：创意热店--进入失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：创意热店--进入失败")
            raise e

    # 测试点击顶部导航的版权站菜单
    def test_click_copyright_menu(self, driver):
        # 进入版权站
        # 悬浮更多
        more_button = ("xpath", "//body/div/header/div[@class='header']/div[@class='head-right']/ul/li[@class='menu-more']/a[1]")
        self.mouse_hover(more_button)
        self.click(HomePageElement.sucaiku_element)
        self.sleep(2)
        self.window(-1)
        url = self.getUrl()
        try:
            assert "https://sc.isheji.com" in url
            self.close_handle() # 关闭多余窗口
        except Exception as e:
            self.close_handle()  # 关闭多余窗口
            self.logger.error("用户在左侧导航的版权图片菜单异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("用户在左侧导航的版权图片菜单失败")
            raise e

    # =======================================
    # 首页左侧导航菜单
    # =======================================

    # 智能扣图
    def test_act_aiCutoutPic(self):
        try:
            self.click(HomePageElement.ai_buckle_menu_element)
            self.sleep(2)
            self.window(0)
            urlInfo = url['url']['testUrl']
            domain = self.getUrl()
            if urlInfo + "/cutout/index" in domain:
                actual = self.getText(AiCutoutPicElement.ai_cutout_title_element)
                self.logger.info('进入智能抠图页面%s' % domain)
                self.assert_text("智能抠图", actual)
        except Exception as e:
            self.logger.error('失败：智能抠图--未进入智能抠图%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：未进入智能抠图页面")
            raise e

    # 365编辑器
    def test_act_editor(self):
        try:
            self.click(HomePageElement.editor_menu_element)
            self.window(0)
            url = self.getUrl()
            self.logger.info('进入365编辑器页面%s' % url)
            assert url == "https://www.365editor.com/?f=bz&k=/f=isheji"
            self.back()
        except Exception as e:
            self.logger.error('失败：进入365编辑器页面失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：进入365编辑器页面失败")
            raise e

    # -------------------  下面代码需要挪位置
    def selfVIP(self):
        # self.move_to_stay("//div[@class='img-icon right_icon2']")
        move_ready = ("xpath", "//div[@class='img-icon right_icon2']")
        self.mouse_hover(move_ready)
        gr_vip = ('xpath', "//a[@class='gr-vip']//img[@class='btn-img']")
        self.click(gr_vip)

    def close_retain(self):
        '''关闭会员挽留弹窗'''
        try:
            try:
                x_button = ('xpath', "//span[contains(@class,'iconfont icon-no close_button')]")
                self.click(x_button)
                try:
                    refuse = ('xpath', "//div[@class='close-btn']")
                    self.click(refuse)
                    self.logger.info('关闭会员挽留弹窗')
                except:
                    self.logger.info('没有会员挽留弹窗')
            except Exception as e:
                self.logger.error('关闭会员挽留弹窗失败')
                raise e
        except:
            self.logger.info('没有挽留弹窗')

    def info_retain(self):
        '''进入会员挽留弹窗'''
        try:
            try:
                x_button = ('xpath', "//span[contains(@class,'iconfont icon-no close_button')]")
                self.click(x_button)
                info = ('xpath', "//div[@class='active']")
                self.click(info)
                self.logger.info('关闭会员挽留弹窗')
                x_button = ('xpath', "//span[contains(@class,'iconfont icon-no close_button')]")
                self.click(x_button)
            except Exception as e:
                self.logger.error('进入会员挽留弹窗失败')
                raise e
        except:
            self.logger.info('没有挽留弹窗')

    def new_my_design(self):
        """新建模板后退出"""
        try:
            self.sleep()
            add_button = ("xpath", "//div[@class='btn-box cover-image']")
            self.click(add_button)
            wide = ("xpath", "//input[@placeholder='宽']")
            self.write(wide, "4433")
            high = ("xpath", "//input[@placeholder='高']")
            self.write(high, "2266")
            start_design_button = ("xpath", "//div[@class='dialog-inner']//button")
            self.click(start_design_button)
            self.window(-1)
            try:
                self.jump_work()
            except Exception as e:
                self.logger.error('进入工作台没有跳过按钮')
                raise e
            self.preservation()
            self.close_and_window()
            self.sleep()
        except Exception as e:
            self.logger.error('失败：首页新的新建设计进入工作台%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：首页新的新建设计进入工作台")
            raise e
        finally:
            self.refresh()

    def today_time(self):###
        now_date = time.strftime("%Y-%m-%d")
        now_data_list = now_date.split("-")
        return now_data_list

    def verification_time(self):
        try:
            last_time = ("xpath", "//div[@class='design-block-item swiper-slide-next']/div[@class='design-detail']")
            last_time_str = self.getText(last_time)
            asster_str = "最后编辑于{}年{}月{}日".format(self.today_time()[0], self.today_time()[1], self.today_time()[2])
            self.logger.info(f"获取到的时间{last_time_str}")
            self.logger.info(f"生成后的时间{asster_str}")
            assert last_time_str == asster_str
        except Exception as e:
            self.logger.error('失败：首页新的新建设计创建模板%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：首页新的新建设计创建模板")
            raise e