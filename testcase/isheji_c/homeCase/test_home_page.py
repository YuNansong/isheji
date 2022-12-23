from pages.isheji_c.homePage.homePage import HomePage
import time
# ======================================================
# 爱设计首页功能
# https://www.isheji.com
# 使用VIP账号运行
# ======================================================
class TestHomePage:

    def test_retain(self, driver):
        '''验证会员挽留弹窗'''
        HomePage(driver).selfVIP()
        HomePage(driver).close_retain()
        time.sleep(2)
        HomePage(driver).selfVIP()
        HomePage(driver).info_retain()

    def test_get_search_tips(self, driver):
        '''验证首页Banner搜索处的默认提示'''
        HomePage(driver).test_get_search_tips()

    def test_home_banner_search(self, driver):
        '''验证首页Banner处搜索功能'''
        HomePage(driver).test_home_banner_search()
        time.sleep(2)

    def test_click_index_temp(self, driver):
        '''从首页点击模板进入工作台,并保存模板'''
        HomePage(driver).test_click_index_temp(driver)
        time.sleep(2)

    def test_home_temp_class(self, driver):
        '''验证在首页点击各个模板分类及模板列表翻页功能'''
        HomePage(driver).test_temp_class()
        time.sleep(2)

    # ==================================
    # 测试首页顶部导航
    # ==================================

    # 测试顶部导航个人VIP
    def test_click_per_vip(self, driver):
        '''验证在首页顶部导航点击【个人VIP】功能'''
        HomePage(driver).test_click_per_vip()
        time.sleep(2)

    def test_open_per_vip_floating_layer(self, driver):
        '''验证在首页悬浮到个人VIP菜单点击【立即开通】功能'''
        HomePage(driver).test_open_per_vip_floating_layer(driver)
        time.sleep(2)

    def test_privilege_detail_floating_layer(self, driver):
        '''验证在首页悬浮到个人VIP菜单点击【详情特权】功能'''
        HomePage(driver).test_privilege_detail_floating_layer()
        time.sleep(2)

    # @pytest.mark.skip(reason="在企业运行页面执行")
    def test_click_ent_vip(self, driver):
        '''验证在首页顶部导航点击【企业解决方案】功能'''
        HomePage(driver).test_click_ent_vip(driver)
        time.sleep(2)

    def test_click_ent_flayer_detail(self, driver):
        '''在首页悬浮到导航的企业解决方案菜单，点击查看详情链接'''
        HomePage(driver).test_click_ent_flayer_detail(driver)
        time.sleep(2)

    def test_click_ent_flayer_detailBtn(self, driver):
        '''在首页悬浮到导航的企业解决方案菜单，点击查看详情按钮'''
        HomePage(driver).test_click_ent_flayer_detailBtn()
        time.sleep(2)

    def test_click_cooperation_menu(self, driver):
        '''验证在首页导航点击【合作】菜单'''
        HomePage(driver).test_click_cooperation_menu()
        time.sleep(2)

    def test_click_api_menu(self, driver):
        '''验证在首页导航点击【API】菜单'''
        HomePage(driver).test_click_api_menu()
        time.sleep(2)

    def test_click_mall_menu(self, driver):
        '''验证在首页导航点击【创意热店】菜单'''
        HomePage(driver).test_act_ideamall()
        time.sleep(2)


    def test_click_copyright_menu(self, driver):
        '''验证在首页点击顶部导航【版权站】菜单'''
        HomePage(driver).test_click_copyright_menu(driver)
        time.sleep(2)
    # ==================================
    # 测试首页左侧导航
    # ==================================
    def test_click_aiBuckle_menu(self, driver):
        '''验证在首页点击左侧导航【智能扣图】菜单'''
        HomePage(driver).test_act_aiCutoutPic()
        time.sleep(2)

    def test_click_editor_menu(self, driver):
        '''验证在首页点击左侧导航【365编辑器】菜单'''
        HomePage(driver).test_act_editor()
        time.sleep(2)

    # def test_new_my_design(self, driver):
    #     """验证在首页新需求的新建模板后退出"""
    #     HomePage(driver).new_my_design()
    #     time.sleep(2)
    #
    # def test_verification_time(self, driver):
    #     """验证新创建的模板的时间"""
    #     HomePage(driver).verification_time()
    #     time.sleep(2)