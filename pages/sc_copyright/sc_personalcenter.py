import random
import time
from common.readLog import Log
from common.sendDingTalk import SendDingTalk
from model.scModel.homeModel import HomeModel
from model.scModel.perCenterModel import PerCenterModel

# 个人中心
class PersonalCenter(HomeModel,PerCenterModel):
    log = Log(__name__)
    logger = log.getLog()

    def cancal_button(self):
        #订单中心取消按钮
        cancal = ('xpath', "//tr[1]//td[8]//div[1]//button[2]")
        self.click(cancal)
        enter_button = ('xpath', "//button[contains(@class,'el-button el-button--default el-button--small el-button--primary')]")
        self.click(enter_button)

    def click_order(self):
        '''进入订单中心'''
        self.click_img()
        order_center = ('xpath', "//li[2]//div[1]//span[2]")
        self.click(order_center)
        self.window(-1)
        self.sleep()
        try:
            # #获取所有订单
            order_id_xpath = ('xpath', "//div[@class='el-table__body-wrapper is-scrolling-left']/table/tbody/tr[1]/td[1]/div")
            order_id = self.getText(order_id_xpath)
            assert order_id != ""

            # paths = ('xpath', "//div[@class='el-table__body-wrapper is-scrolling-left']/table/tbody/tr")
            # nub_list = len(self.getElements(paths))
            # #循环订单
            # order = 1
            # while nub_list > order:
            #     is_pay = ('xpath', "//tr[@class='el-table__row'][1]/td[4]/div")
            #     pay_text = self.getText(is_pay)
            #     pay = pay_text.strip()
            #     if pay == '未支付':
            #         # self.cancal_button() # 已取消该功能
            #         order += 1
            #     if pay == '已支付':
            #         break
        except Exception as e:
            self.logger.error('失败：订单中心订单号断言失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：订单中心订单号断言失败")
            raise e

    def buy_month_vip(self):###
        '''月会员订单'''
        try:
            person_vip = ('xpath', "//div[@class='header-right']//a[1]")
            self.click(person_vip)
            self.window(-1)
            #月会员展示价格
            month_vip1 = ('xpath', "//div[@class='team-item'][3]/div[2]/span[2]")
            str_vip1 = self.getText(month_vip1)
            float_vip1 = float(str_vip1)
            int_flat1 = int(float_vip1)
            #点击立即购买
            buy_button = ('xpath', "//div[@class='banquan-btn banquan-btn3']")
            self.click(buy_button)
            #选择栏的价格
            month_vip2 = ('xpath', "//li[@class='payContent-card-price card-selected']/section/span")
            str_vip2 = self.getText(month_vip2)
            float_vip2 = float(str_vip2)
            int_flat2 = int(float_vip2)
            self.sleep(2)
            self.close_and_window()
            self.sleep()
            assert int_flat1 == int_flat2
        except Exception as e:
            self.logger.error('失败：购买会员价格异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：购买会员价格异常")
            raise e


    def person_vip_order_validation(self):
        '''验证订单中心添加/取消订单'''
        try:
            #点击个人VIP
            self.buy_month_vip()
            #返回订单中心刷新页面
            self.refresh()
            #取消订单
            cancel_button = ('xpath', "//tr[1]//td[8]//div[1]//button[2]")
            self.click(cancel_button)
            enter_button = ('xpath', "//button[contains(@class,'el-button el-button--default el-button--small el-button--primary')]")
            self.click(enter_button)
            cancel_tips = ('xpath', "//p[contains(@class,'el-message__content')]")
            actual = self.getText(cancel_tips)
            expect = '订单已取消'
            assert actual == expect
        except Exception as e:
            self.logger.error('失败：订单中心取消订单%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：订单中心取消订单")
            raise e

    def assert_success(self):
        '''添加成功提示'''
        try:
            success_tips = ('xpath', "//div[contains(@class,'el-message el-message--success')]")
            expect = '被授权方添加成功'
            tips_text = self.getText(success_tips)
            actual = tips_text.strip()
            assert expect == actual
        except Exception as e:
            self.logger.error('失败：订单中心添加被授权方断言失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：订单中心添加被授权方断言失败")
            raise e

    def assert_delete(self):
        '''删除成功提示'''
        try:
            delete_tips = ('xpath', "//div[contains(@class,'el-message el-message--success')]")
            expect = '被授权方删除成功'
            tips_text = self.getText(delete_tips)
            actual = tips_text.strip()
            assert expect == actual
        except Exception as e:
            self.logger.error('失败：订单中心删除被授权方断言失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：订单中心删除被授权方断言失败")
            raise e

    def management_authorization(self):
        '''管理授权方点击'''
        authorization_button = ('xpath', "//tr[1]//td[8]//div[1]//button[1]//span[1]")
        self.click(authorization_button)
        self.sleep(2)
        # 输入被授权方姓名
        name_input = ('xpath', "//input[contains(@placeholder,'输入企业名称/个人姓名')]")
        self.write(name_input, '姓名')
        # 输入纳税人识别号/身份证号
        id_input = ('xpath', "//input[contains(@placeholder,'输入纳税人识别号/身份证号')]")
        self.write(id_input, '130126130126130126')
        # 添加操作
        add_button = ('xpath', "//span[contains(@class,'add')]")
        self.click(add_button)
        self.assert_success()
        self.sleep()
        # 删除操作
        del_button = ('xpath', "//span[contains(@class,'del')]")
        self.click(del_button)
        self.assert_delete()
        self.sleep()
        # 确定按钮
        enter_button = ('xpath', "//div[contains(@class,'banquan-btn')]")
        self.click(enter_button)

    def download_record(self):
        '''进入下载记录'''
        download_record_button = ('xpath', "//div[@class='personal']/nav/ul/li[3]/a")
        self.click(download_record_button) # 点击下载记录
        self.sleep(5)
        try:
            download_record_sign = ('xpath', "//div[@class='title']//p")
            sign_tips = self.getText(download_record_sign)
            actual = sign_tips.strip()
            expect = '下载记录'
            assert actual == expect
        except Exception as e:
            self.logger.error('失败：进入下载记录断言失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：进入下载记录断言失败")
            raise e

    def get_today_date(self):
        '''获取今天的日期'''
        today_str = time.strftime('%Y.%m.%d', time.localtime(time.time()))
        today_list = today_str.split('.')
        res = today_list[2].startswith('0')
        if res == True:
            today_num = today_list[2].replace('0', '')
            return today_num
        else:
            return today_list[2]

    def positoning_data(self):
        '''上个月时间'''
        today_num = self.get_today_date()
        for week in range(2, 8):
            for day in range(1, 8):
                select_today = ('xpath',
                                "//div[@class='el-picker-panel__content']/table[@class='el-date-table']/tbody/tr[" + str(
                                    week) + "]/td[" + str(day) + "]/div/span")
                today_str = str(self.getText(select_today))
                def_str = str(today_num)
                if today_str == def_str:
                    self.click(select_today)

    def standard_time(self):
        '''获取今天的日期'''
        today_str = time.strftime('%Y.%m.%d', time.localtime(time.time()))
        today_standard = today_str.replace('.', '-')
        return today_standard

    def select_time(self):
        '''筛选筛选时间'''
        try:
            # 点击下载时间
            star_time_button = ('xpath', "//input[@placeholder='下载开始时间']")
            self.click(star_time_button)
            # 点击上个月
            last_month = (
            'xpath', "//button[@class='el-picker-panel__icon-btn el-date-picker__prev-btn el-icon-arrow-left']")
            self.click(last_month)
            self.sleep()
            self.positoning_data()
            self.sleep()
            #输入下载结束时间
            end_time = ('xpath', "//input[@placeholder='下载结束时间']")
            input_end_time = self.standard_time()
            self.write(end_time, input_end_time)
            self.sayok(end_time)
        except Exception as e:
            self.logger.error('失败：筛选下载时间%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：筛选下载时间")
            raise e

    def find_picture_id(self):
        '''获取ID后搜索'''
        list_num = ""
        try:
            self.refresh()
            self.sleep(5)
            download_record_button = ('xpath', "//a[contains(text(),'下载记录')]")
            self.click(download_record_button)
            self.sleep(5)
            first_id = ('xpath', "//tbody/tr[1]/td[1]/div/div[2]/div[2]")
            picture_id = self.getText(first_id)
            id = picture_id.strip()
            self.logger.info("在下载记录获取到的图片ID: %s" % id)
            #搜索图片ID
            input_path = ('xpath', "//input[contains(@placeholder,'搜索图片ID')]")
            self.write(input_path, id)
            self.sayok(input_path)
            self.sleep()
            picture_list = self.driver.find_elements('xpath', "//tr[contains(@class,'el-table__row')]")
            list_num = len(picture_list)
            assert list_num == 1
        except Exception as e:
            self.logger.error(f'失败：通过ID搜索图片,预期结果为1，实际结果为{list_num}%s' % repr(e))
            SendDingTalk().sendDingTalkMsg(f"失败：通过ID搜索图片,预期结果为1，实际结果为{list_num}")
            raise e

    def download_again(self):
        '''验证重新下载功能'''
        try:
            i = 0
            while i < 3:
                self.sleep(2)
                # 重新下载
                download_again_button = ('xpath',"//div[@class='collect content']//tbody/tr[1]/td[last()]//span[contains(text(),'重新下载')]")
                self.click(download_again_button)
                #重新下载提示
                self.sleep(1)
                try:
                    downloading = ('xpath', "//p[@class='el-message__content']")
                    tips = self.getText(downloading)
                except:
                    tips = ""

                if tips == "":
                    i += 1
                    continue
                if tips != "":
                    break
                assert str(tips).strip() == '您已下载过该原图，为您免费重复下载'
        except Exception as e:
            self.logger.error(f'失败：在下载记录重新下载原图%s' % repr(e))
            SendDingTalk().sendDingTalkMsg(f"失败：在下载记录重新下载原图")
            raise e

    def all_of_the_order_operation(self):
        '''验证订单中心操作'''
        self.click_order()

    def downd_test(self):
        '''筛选下载时间'''
        self.download_record()
        self.select_time()

    def download_authorization(self):
        '''下载授权书'''
        try:
            input_box = ('xpath', "//input[@placeholder='搜索图片ID']")
            self.clear(input_box)
            magnifier_button = ('xpath', "//div[@class='search-input']//img")
            self.click(magnifier_button)
            download_button = ('xpath', "//div[@class='collect content']//tbody/tr[1]/td[last()]//span[contains(text(),'下载授权书')]")
            self.click(download_button)
            try:
                success_tips = ('xpath', "//p[@class='el-message__content']")
                success = self.getText(success_tips)
                tips = '授权书下载完成'
                assert success == tips
            except:
                # 下载授权书输入被授权方企业名称
                select_enterprise = ('xpath', "//div[@class='collect-input']/input")
                self.clear(select_enterprise)
                self.write('自动化测试', select_enterprise)
                self.sleep(2)
                download_button = ('xpath', "//div[contains(@class,'active')]")
                self.click(download_button)
                success_tips = ('xpath', "//p[contains(@class,'el-message__content')]")
                success = self.getText(success_tips)
                tip = success.strip()
                expect_tips = '授权书下载完成'
                assert tip == expect_tips
        except Exception as e:
            self.logger.error('失败：下载授权书失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：下载授权书失败")
            raise e
    # 切换团队身份
    def test_change_team(self):
        self.close_handle()
        self.change_team()

    # 切换个人身份
    def test_change_personal(self):
        self.close_handle()
        self.change_per()

    def batch_authorization(self):
        '''验证批量授权功能'''
        try:
            a = 0
            success_tips = ""
            tips = ['授权书下载完成','所选素材都已经获取过授权证书了']
            # #点击右侧下载记录
            self.act_account_center() # 进入到下载记录页面
            self.click_all_auth()
            self.sleep(1)
            self.select_all_button()
            self.sleep(1)
            self.download_auth_button()
            self.sleep(1)
            self.select_enterprise()
            while a < 3:
                self.sure_download()
                self.sleep(1)
                success_tips = self.get_tips()
                if success_tips == "":
                    a = a+1
                else:
                    break
            self.click_x_button()
            self.sleep(1)
            self.click_cancel_button()
            assert success_tips in tips
        except Exception as e:
            self.logger.error('失败：批量下载授权书%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("批量下载授权书")
            raise e

    def into_invoice(self):
        '''发票中心企业'''
        try:
            invoice = ('xpath', "//div[@class='personal']/nav/ul/li[5]/a[contains(text(),'发票')]")
            self.click(invoice)
            self.sleep(2)
            path = ('xpath', "//div[@class='personal']//li[4]//span[1]")
            path_text = self.getText(path)
            assert str(path_text).strip() == "竟园"
        except Exception as e:
            self.logger.error('失败：申请发票企业断言%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：申请发票企业断言")
            raise e

    def invoice_person(self):
        '''发票中心个人'''
        try:
            person_button = ('xpath', "//div[@class='info']//div[2]")
            self.click(person_button)
            path = ('xpath', "//div[@class='personal']//li[4]//span[1]")
            path_text = self.getText(path)
            assert str(path_text).strip() == "测试"
        except Exception as e:
            self.logger.error('失败：申请发票个人断言%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：申请发票个人断言")
            raise e

    def apply_for_invoice(self):
        self.into_invoice()
        self.invoice_person()

    def account_information(self):
        '''账户信息'''
        try:
            account_path = ('xpath', "//div[@class='personal']/nav/ul/li[4]/a[contains(text(),'信息')]")
            self.click(account_path)
            self.sleep(2)
            sign_button = ('xpath', "//div[@class='caozuo r']/div[@class='blue']")
            sign = self.getText(sign_button)
            assert str(sign).strip() == "前往修改账号"
            self.close_handle()
        except Exception as e:
            self.logger.error('个人身份未进入账户信息%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("个人身份未进入账户信息")
            raise e

    def add_file_name(self):
        '''文件夹命名'''
        folderId = random.randint(0, 9999)
        add_file_xpath = ('xpath', "//span[@class='icon-Add iconfont']")
        self.click(add_file_xpath)
        input_coll_folder_name = ('xpath', "//input[@placeholder='新建文件夹名称']")
        self.clear(input_coll_folder_name)
        self.write(input_coll_folder_name, "收藏夹" + str(folderId))
        self.sleep(0.5)
        sure_btn = ('xpath',"//div[@class='collect-inner add']//div[contains(text(),'确定')]")
        self.click(sure_btn)

    def del_ent_material_folder(self):
        '''进入企业素材删除文件夹'''
        try:
            self.ent_mertal()
            self.sleep(2)
            num = self.get_folder_num()
            self.add_file_name() # 首先新建一个空文件夹
            for i in range(1,num):
                conteng_nmb = ('xpath', "//ul[@class='folder']/li["+str(i)+"]/span")
                conteng_text = self.getText(conteng_nmb)
                foler_xpath = ('xpath', "//ul[@class='folder']/li["+str(i)+"]/div")
                print("===",conteng_text)
                if conteng_text.startswith('0') == False:
                    continue
                elif conteng_text.startswith('0') == True:
                    self.mouse_hover(foler_xpath)
                    three_sgin = ('xpath', "//ul[@class='folder']/li["+str(i)+"]/div/div[@class='more']")
                    self.click(three_sgin)
                    del_button = ('xpath', "//div[@class='caozuo']//div[2]")
                    self.click(del_button)
                    self.sleep(1)
                    sure_button = ('xpath', "//button[@class='el-button el-button--default el-button--small el-button--primary ']")
                    self.click(sure_button)
                    self.sleep(1)
                    break
        except Exception as e:
            self.logger.error('失败：删除企业素材文件%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：删除企业素材文件")
            raise e

    def into_member(self):###
        '''进入成员管理，添加成员'''
        try:
            menber_button = ('xpath', "//nav//a[contains(text(),'成员管理')]")
            self.click(menber_button)
            self.sleep(2)
            member_text = ('xpath', "//div[@class='collect content']//p")
            sgingo = self.getText(member_text)
            assert sgingo == '成员管理'
        except Exception as e:
            self.logger.error('失败：进入成员管理%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：进入成员管理")
            raise e

    def del_member(self):###
        '''删除成员'''
        try:
            del_button = ('xpath', "//button[@class='el-button el-button--danger el-button--mini']//span")
            self.click(del_button)
            enter_button = ('xpath', "//button[contains(@class,'el-button el-button--default el-button--small el-button--primary')]")
            self.click(enter_button)
            tip = ('xpath', "//p[@class='el-message__content']")
            tips = self.getText(tip)
            assert tips == '成员删除成功'
        except Exception as e:
            self.logger.error('失败：删除成员%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：删除成员")
            raise e

    def add_merber(self, role):###
        try:
            # 点击添加成员按钮
            add_button = ('xpath', "//div[@class='r']//div")
            self.click(add_button)
            # 账号名称
            username = ('xpath', "//input[@placeholder='请输入账号名称']")
            self.write(username, '13188133423')
            #手机号
            phone = ('xpath', "//input[@placeholder='手机号']")
            self.write(phone, '13188133423')
            #角色
            member = ('xpath', "//input[@placeholder='请选择']")
            self.click(member)
            self.sleep()
            #选择身份
            if role == '管理员':
                role_click1 = ('xpath', "//div[@class='el-scrollbar']/div[1]/ul/li[2]")
                self.click(role_click1)
            if role == '设计师':
                role_click2 = ('xpath', "//div[@class='el-scrollbar']/div[1]/ul/li[3]")
                self.click(role_click2)
            if role == '成员':
                sole_click3 = ('xpath', "//div[@class='el-scrollbar']/div[1]/ul/li[4]")
                self.click(sole_click3)
            #样图配额
            # young_to_mub = ('xpath', "//input[@placeholder='请输入样图下载配额']")
            # self.write(young_to_mub, "1")
            #原图配额
            # orgind_mub = ('xpath', "//input[@placeholder='原图配额']")
            # self.write(orgind_mub, '1')
            add_to_button = ('xpath', "//button[@class='user-btn']")
            self.click(add_to_button)
            tip = ('xpath', "//div[@class='el-message el-message--success']")
            tips = self.getText(tip)
            self.sleep(2)
            self.del_member()
            assert tips == '成员添加成功'
        except Exception as e:
            self.logger.error(f'失败：添加{role}身份成员失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg(f"失败：添加{role}身份成员失败")
            raise e

    def member_management(self):
        #进入成员管理
        try:
            self.into_member()
            self.add_merber('管理员')
            self.sleep(1)
            self.add_merber('设计师')
            self.sleep(1)
            self.add_merber('成员')
            self.sleep(1)
            self.close_handle()
        except Exception as e:
            self.close_handle()
            self.logger.error('添加成员失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg(f"添加成员失败")
            raise e
