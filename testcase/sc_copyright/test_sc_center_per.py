from pages.sc_copyright.sc_personalcenter import PersonalCenter
from pages.basePage import Action


class TestPersonConter:

    def test_change_per(self, driver):
        '''版权站-切换个人身份'''
        PersonalCenter(driver).test_change_personal()

    def test_order_operation(self, driver):
        '''验证进入订单中心功能'''
        PersonalCenter(driver).all_of_the_order_operation()
        Action(driver).sleep()

    # def test_person_vip_order_validation(self, driver):
    #     '''验证订单中心取消订单功能'''
    #     PersonalCenter(driver).person_vip_order_validation()
    #     Action(driver).sleep()

    def test_downd_test(self, driver):
        '''在下载记录页面通过下载时间进行筛选'''
        PersonalCenter(driver).downd_test()
        Action(driver).sleep()

    def test_find_picture_id(self, driver):
        '''在下载记录页面验证通过ID搜索图片功能'''
        PersonalCenter(driver).find_picture_id()
        Action(driver).sleep()

    def test_download_again(self, driver):
        '''在下载记录页面验证重新下载功能'''
        PersonalCenter(driver).download_again()
        Action(driver).sleep()

    def test_download_authorization(self, driver):
        '''在下载记录页面验证下载授权书功能'''
        PersonalCenter(driver).download_authorization()
        Action(driver).sleep()

    def test_apply_for_invoice(self, driver):
        '''验证申请发票页面是否正常'''
        PersonalCenter(driver).apply_for_invoice()
        Action(driver).sleep()

    def test_account_information(self, driver):
        '''验证进入账户信息功能'''
        PersonalCenter(driver).account_information()
        Action(driver).sleep()

    def test_change_team(self, driver):
        '''版权站-切换团队身份'''
        PersonalCenter(driver).test_change_team()