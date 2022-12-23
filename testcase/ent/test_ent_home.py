'''
企业解决方案（conTech）
'''
from pages.entPage.entHomePage import QiyeHomePage
from pages.basePage import Action

class TestEntHome:

    def test_qiye_vip(self, driver):
        '''测试在首页点击企业VIP'''
        QiyeHomePage(driver).test_act_qiye_home()
        Action(driver).sleep(1)

    def test_click_tiyan_btn(self, driver):
        '''测试在企业介绍页面首页点击立即体验按钮'''
        QiyeHomePage(driver).test_click_tiyan_btn()
        Action(driver).sleep(1)

    def test_click_ziyuancaimai(self, driver):
        '''测试在企业介绍页面首页点击资源采买按钮'''
        QiyeHomePage(driver).test_click_ziyuancaimai()
        Action(driver).sleep(1)

    def test_click_zhinengchuangyi(self, driver):
        '''测试在企业介绍页面首页点击智能创意按钮'''
        QiyeHomePage(driver).test_click_zhinengchuangyi()
        Action(driver).sleep(1)

    def test_click_neirongguanli(self, driver):
        '''测试在企业介绍页面首页点击内容管理按钮'''
        QiyeHomePage(driver).test_click_neirongguanli()
        Action(driver).sleep(1)

    def test_click_neirongfenfa(self, driver):
        '''测试在企业介绍页面首页点击内容分发按钮'''
        QiyeHomePage(driver).test_click_neirongfenfa()
        Action(driver).sleep(1)

    def test_click_shujuguanli(self, driver):
        '''测试在企业介绍页面首页点击数据管理按钮'''
        QiyeHomePage(driver).test_click_shujuguanli()
        Action(driver).sleep(1)

    def test_view_footer(self, driver):
        '''测试在企业介绍页面首页查看底部footer'''
        QiyeHomePage(driver).test_view_footer()
        Action(driver).sleep(1)

    def test_click_contech(self, driver):
        '''测试在企业介绍页面点击ConTech按钮'''
        QiyeHomePage(driver).test_click_contech()
        Action(driver).sleep(1)

    def test_click_chanpin_supply(self, driver):
        '''测试在企业介绍页面点击产品下拉菜单--智能创意供给选项'''
        QiyeHomePage(driver).test_click_chanpin_supply()
        Action(driver).sleep(1)

    def test_click_jieju_changjing(self, driver):
        '''测试在企业介绍页面点击解决方案下拉菜单'''
        QiyeHomePage(driver).test_click_jieju_changjing()
        Action(driver).sleep(1)

    def test_open_dev(self, driver):
        '''测试在企业介绍页面点击解决方案下拉菜单'''
        QiyeHomePage(driver).test_open_dev()
        Action(driver).sleep(1)

    def test_custom_manage(self, driver):
        '''测试在企业介绍页面点击开放平台菜单'''
        QiyeHomePage(driver).test_custom_manage()
        Action(driver).sleep(1)

    def test_about(self, driver):
        '''测试在企业介绍页面点击客户案例下拉菜单'''
        QiyeHomePage(driver).test_about()
        Action(driver).sleep(1)
