from common.getYaml import url
from common.sendDingTalk import SendDingTalk
from element.ent.entHomeElement import EntHomeElement
from model.entModel.entIndexModel import EntIndexModel
class QiyeHomePage(EntIndexModel):

    # 测试访问爱设计企业首页
    urlInfo = url['url']['qiyeUrl']
    def test_act_qiye_home(self):
        try:
            try:
                self.click_ent_vip()
                self.window(-1)
            except:
                self.transfer_qiye_url()
            # try:
            #     self.click_gaoji() # 处理高级
            # except:
            #     self.logger.info("没有展示高级按钮")
            self.sleep(2)
            text = self.getText(EntHomeElement.context_xpath)
            assert str(text).strip() == "内容流转全链路解决方案"
            self.sleep(2)
        except Exception as e:
            self.logger.info("访问企业首页出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试访问企业首页失败")
            raise e

    # 测试在爱设计企业首页点击体验按钮
    def test_click_tiyan_btn(self):
        try:
            # 点击轮播图
            # 点击第二张轮播图
            self.click(EntHomeElement.lunbotu_xpath)
            self.sleep(0.5)
            self.click(EntHomeElement.tiyan_xpath)
            self.window(-1)
            url = self.get_qiye_url()
            assert url == self.urlInfo+'/contact'
            # 关闭contact页面
            self.window(-1)
            self.close_and_window()
        except Exception as e:
            self.logger.info("在爱设计企业首页点击体验按钮异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试在爱设计企业首页点击体验按钮失败")
            raise e

    # 测试在爱设计企业首页点击资源采买按钮
    def test_click_ziyuancaimai(self):
        try:
            self.click(EntHomeElement.ziyuancaimai_xpath)
            self.sleep(2)
            text = self.getText(EntHomeElement.ziyuancaimai_text_xpath)
            print("text:",text)
            assert str(text).strip() == "智能创意供给"
        except Exception as e:
            self.logger.info("测试在爱设计企业首页点击资源采买按钮出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试在爱设计企业首页点击资源采买按钮失败")
            raise e

# 测试在爱设计企业首页点击智能创意按钮
    def test_click_zhinengchuangyi(self):
        try:
            self.click(EntHomeElement.zhinengchuangyi_xpath)
            self.sleep(2)
            text = self.getText(EntHomeElement.zhinengchuangyi_text_xpath)
            assert str(text).strip() == "智能内容生产"
        except Exception as e:
            self.logger.info("测试在爱设计企业首页点击只能创意按钮出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试在爱设计企业首页点击只能创意按钮失败")
            raise e

# 测试在爱设计企业首页点击内容管理按钮
    def test_click_neirongguanli(self):
        try:
            self.click(EntHomeElement.neirongguanli_xpath)
            text = self.getText(EntHomeElement.neirongguanli_text_xpath)
            assert str(text).strip() == "智能内容管理"
        except Exception as e:
            self.logger.info("测试在爱设计企业首页点击内容管理按钮出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试在爱设计企业首页点击内容管理按钮失败")
            raise e

# 测试在爱设计企业首页点击内容分发按钮
    def test_click_neirongfenfa(self):
        try:
            self.click(EntHomeElement.neirongfenfa_xpath)
            self.sleep(2)
            text = self.getText(EntHomeElement.neirongfenfa_text_xpath)
            assert str(text).strip() == "智能内容分发"
        except Exception as e:
            self.logger.info("测试在爱设计企业首页点击内容分发按钮出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试在爱设计企业首页点击内容分发按钮失败")
            raise e

# 测试在爱设计企业首页点击数据管理按钮
    def test_click_shujuguanli(self):
        try:
            self.click(EntHomeElement.shujuguanli_xpath)
            self.sleep(2)
            text = self.getText(EntHomeElement.shujuguanli_text_xpath)
            assert str(text).strip() == "智能数据管理"
        except Exception as e:
            self.logger.info("测试在爱设计企业首页点击数据管理按钮出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试在爱设计企业首页点击数据管理按钮失败")
            raise e

    # 测试在爱设计企业首页下滑到底部查看内容
    def test_view_footer(self):
        try:
            self.page_down(5000)
            # contact 页面下的提交按钮
            self.click(EntHomeElement.footer_xpath)
            self.sleep(2)
            self.window(-1)
            url = self.get_qiye_url()
            assert "contact" in url
            assert self.getText(EntHomeElement.submit_btn_xpath) == "提交"
            self.sleep(1)
            self.window(-1)
            self.close_and_window()
        except Exception as e:
            self.logger.info("测试在爱设计企业首页下滑到底部查看内容出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试在爱设计企业首页下滑到底部查看内容失败")
            raise e

    # 测试在爱设计企业首页导航点击ConTech
    def test_click_contech(self):
        try:
            self.click(EntHomeElement.conTech_xpath)
            url = self.get_qiye_url()
            if url == self.urlInfo+"/contech":
                # 获取页面的内容
                text = self.getText(EntHomeElement.conTech_context_xpath)
                assert text == "中国移动互联网流量红利见顶，"
                self.page_down(5000) # 下滑到底部测试
                neirong = self.getText(EntHomeElement.neirong_xpath)
                assert neirong == "内容创意智能解决方案"
        except Exception as e:
            self.logger.info("测试在爱设计企业首页导航点击ConTech出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试在爱设计企业首页导航点击ConTech失败")
            raise e

    # 测试在爱设计企业首页导航点击产品
    def click_chanpin(self):
        try:
            self.click(EntHomeElement.chanpin_xpath)
            self.sleep(2)
        except Exception as e:
            self.logger.info("测试在爱设计企业首页导航点击产品出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试在爱设计企业首页导航点击产品失败")
            raise e

    # 测试在爱设计企业首页导航点击解决方案
    def click_jiejufangan(self):
        try:
            self.click(EntHomeElement.jiejufangan_xpath)
            self.sleep(2)
        except Exception as e:
            self.logger.info("测试在爱设计企业首页导航点击解决方案出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试在爱设计企业首页导航点击解决方案失败")
            raise e

    # 测试在爱设计企业首页导航点击产品下的菜单
    def test_click_chanpin_supply(self):
        try:
            for i in range(1,6):
                self.click_chanpin()
                select_menu_xpath = ('xpath',"//body/ul//div[@class='second-box']/li["+str(i)+"]")
                self.click(select_menu_xpath)
                self.sleep(2)
                supply_url = self.get_qiye_url()
                if i == 1:
                    assert supply_url == self.urlInfo+"/supply"
                if i == 2:
                    assert supply_url == self.urlInfo+"/output"
                if i == 3:
                    assert supply_url == self.urlInfo+"/manage"
                if i == 4:
                    assert supply_url == self.urlInfo+"/fission"
                if i == 5:
                    assert supply_url == self.urlInfo+"/data"
        except Exception as e:
            self.logger.info("测试在爱设计企业首页导航点击产品下的菜单出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试在爱设计企业首页导航点击产品下的菜单失败")

    # 测试在爱设计企业首页导航点击解决方案下的菜单
    def test_click_jieju_changjing(self):
        try:
            for i in range(2,6):
                self.click_jiejufangan()
                a = ('xpath',"//body/ul[2]/div[2]/div[1]/li["+str(i)+"]")
                self.click(a)

                if i == 2:
                    private_url = self.get_qiye_url()
                    assert private_url == self.urlInfo+"/private"

                if i == 3:
                    private_url = self.get_qiye_url()
                    assert private_url == self.urlInfo+"/purchase"

                if i == 4:
                    private_url = self.get_qiye_url()
                    assert private_url == self.urlInfo+"/brand"

                if i == 5:
                    private_url = self.get_qiye_url()
                    assert private_url == self.urlInfo+"/marketing"

            for j in range(2,7):
                self.click_jiejufangan()
                a1 = ('xpath',"//body/ul[2]/div[2]/div[2]/li["+str(j)+"]") # ul[2]需要点击产品后才为ul[2]
                self.click(a1)
                self.sleep(2)
                if j == 2:
                    private_url = self.get_qiye_url()
                    assert private_url == self.urlInfo+"/finance"

                if j == 3:
                    private_url = self.get_qiye_url()
                    assert private_url == self.urlInfo+"/education"

                if j == 4:
                    private_url = self.get_qiye_url()
                    assert private_url == self.urlInfo+"/chain"

                if j == 5:
                    private_url = self.get_qiye_url()
                    assert private_url == self.urlInfo+"/retail"

                if j == 6:
                    private_url = self.get_qiye_url()
                    assert private_url == self.urlInfo+"/network"
        except Exception as e:
            self.logger.info("测试在爱设计企业首页导航点击解决方案下的菜单出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试在爱设计企业首页导航点击解决方案下的菜单失败")
            raise e

    # 测试在爱设计企业首页导航点击开放者平台菜单
    def test_open_dev(self):
        try:
            self.click(EntHomeElement.open_menu_xpath)
            self.sleep(2)
            open_url = self.get_qiye_url()
            if open_url == self.urlInfo+"/platform":
                text = self.getText(EntHomeElement.api_xpath)
                assert text == "爱设计智能API接入平台"
        except Exception as e:
            self.logger.info("测试在爱设计企业首页导航点击开放者平台菜单出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试在爱设计企业首页导航点击开放者平台菜单失败")
            raise e

    # 测试在爱设计企业首页导航点击客户案例菜单
    def test_custom_manage(self):
        try:
            self.click(EntHomeElement.custom_xpath)
            self.sleep(2)
            open_url = self.get_qiye_url()
            if open_url == self.urlInfo+"/case":
                custome_succ_xpath = ('xpath',"//div[@class='case']/div[1]/div[1]")
                self.getText(custome_succ_xpath)
        except Exception as e:
            self.logger.info("测试在爱设计企业首页导航点击客户案例菜单出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试在爱设计企业首页导航点击客户案例菜单失败")
            raise e

    # 测试在爱设计企业首页导航点击关于我们菜单
    def test_about(self):
        try:
            self.click(EntHomeElement.about_xpath)
            self.sleep(2)
        except Exception as e:
            self.logger.info("测试在爱设计企业首页导航点击关于我们菜单出现异常%s"% repr(e))
            SendDingTalk().sendDingTalkMsg("测试在爱设计企业首页导航点击关于我们菜单失败")
            raise e