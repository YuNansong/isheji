from common.getYaml import url
from common.getYaml import userinfo
from common.sendDingTalk import SendDingTalk
from pages.basePage import Action
from common.readLog import Log


class UserCore(Action):
    log = Log(__name__)
    logger = log.getLog()

    def user_head_portrait(self):
        '''点击账号设置'''
        try:
            head_portrait = ("xpath", "//img[@class='head-image']")
            self.mouse_hover(head_portrait)
            username_set = ('xpath', "//li[@class='myaccount']//a//span")
            self.click(username_set)
        except Exception as e:
            self.logger.error('测试个人中心点击账号设置异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("测试个人中心点击账号设置失败")
            raise e

    def assert_online_username(self):
        '''断言账户昵称线上'''
        namenick = ('xpath', "//div[@id='account']//div[3]//p//span")
        actual = self.getText(namenick)
        actual = int(actual)
        username = userinfo['userinfo']['online']['vipUser']['username']
        expect = username
        self.assert_text(expect, actual)

    def assert_test_username(self):
        '''断言账户昵称测试'''
        namenick = ('xpath', "//div[@id='account']//div[3]//p//span")
        actual = self.getText(namenick)
        actual = int(actual)
        username = userinfo['userinfo']['test']['vipUser']['username']
        expect = username
        self.assert_text(expect, actual)

    def nickname(self):
        '''断言账户昵称'''
        try:
            self.appoint_url(self.assert_online_username, self.assert_test_username)
        except Exception as e:
            self.logger.error('测试个人中心验证账户昵称异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("测试个人中心验证账户昵称失败")
            raise e

    def assert_user_security_online(self):
        '''账户安全、验证手机号：线上'''
        user_safe = ('xpath', "//div[@class='menu-content']//p[2]")
        self.click(user_safe)
        self.sleep()
        pthono = ('xpath', "//div[@id='information']//div[1]//p[2]/span")
        actual = self.getText(pthono)
        username = userinfo['userinfo']['online']['vipUser']['username']
        expect = str(username)
        self.assert_text(expect, actual)

    def assert_user_security_test(self):
        '''账户安全、验证手机号：测试'''
        user_safe = ('xpath', "//div[@class='menu-content']//p[2]")
        self.click(user_safe)
        self.sleep()
        pthono = ('xpath', "//div[@id='information']//div[1]//p[2]/span")
        actual = self.getText(pthono)
        username = userinfo['userinfo']['test']['vipUser']['username']
        expect = str(username)
        self.assert_text(expect, actual)

    def user_security(self):
        '''账户安全、验证手机号'''
        try:
            self.appoint_url(self.assert_user_security_online, self.assert_user_security_test)
        except Exception as e:
            self.logger.error('测试个人中心验证进入账户安全列表异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("测试个人中心验证进入账户安全列表失败")
            raise e

    def my_order(self):
        '''我的订单'''
        try:
            my_order = ('xpath', "//div[@class='menu-content']/p[3]")
            self.click(my_order)
            self.sleep(2)
            order = ('xpath', "//div[@id='order']//li[1]/p[1]")
            actual = self.getText(order)
            print(actual, '========================')
            actual = str(actual)
            expect = '2022'
            self.assert_in_abnormal(expect, actual)
        except Exception as e:
            self.logger.error('测试个人中心验证进入我的订单列表异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("测试个人中心验证进入我的订单列表失败")
            raise e

    def apply_invoice(self):
        '''申请发票'''
        try:
            my_author = ('xpath', "//div[@class='menu-content']/p[4]")
            self.click(my_author)
            self.sleep(2)
            moner_path = ('xpath', "//div[@id='record']//div[1]//div[2]//span[2]")
            moner_text = self.getText(moner_path)
            moner_str = moner_text.strip()
            money_float = float(moner_str)
            assert money_float > 0
        except Exception as e:
            self.logger.error('申请发票金额异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("申请发票金额异常")
            raise e

    def my_authorzation(self):
        '''我的授权--空记录'''
        try:
            my_author = ('xpath', "//div[@class='menu-content']/p[4]")
            self.click(my_author)
            self.sleep(2)
            record = ('xpath', "//div[@id='downdemo' and @style='']/div/p")
            actual = self.getText(record)
            expect = '还没有授权记录'
            self.assert_text(expect, actual)
        except Exception as e:
            self.logger.error('测试个人中心验证进入我的授权列表异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("测试个人中心验证进入我的授权列表失败")
            raise e

    def my_authorzation_download(self):
        '''我的授权--有记录'''
        my_author = ('xpath', "//div[@class='menu-content']/p[4]")
        self.click(my_author)
        self.sleep(2)
        try:
            authorzation = ('xpath', "//div[@id='downdemo' and @style='']/div[1]/div[1]/ul/li[1]/p[last()]/a")
            schrodinger = self.getText(authorzation)
            if schrodinger == '获取':
                self.click(authorzation)
                # qiye_name = ('xpath', "//input[@placeholder='请输入企业名称']")
                # self.write(qiye_name, '自动化测试输入企业名称')
                # xinyong_code = ('xpath', "//input[@placeholder='请输入统一社会信用代码']")
                # self.write(xinyong_code, "reawaqaqaqar")
                # talk_phono = ('xpath', "//input[@placeholder='请输入联系电话']")
                # self.write(talk_phono, "13213213213")
                # email_path = ('xpath', "//input[@placeholder='请输入邮箱地址']")
                # self.write(email_path, 'test@test.com')
                up_give = ('xpath', "//button[@class='el-button el-button--primary']//span")
                self.click(up_give)
                self.sleep()
            if schrodinger == '下载':
                self.click(authorzation)
        except Exception as e:
            self.logger.error('测试个人中心验证进入我的授权列表下载图片异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("测试个人中心验证进入我的授权列表下载图片失败")
            raise e

    def sample_drawing_dowload(self):
        '''样图下载'''
        try:
            sample_drawing = ('xpath', "//div[@class='menu-content']//p[5]")
            self.click(sample_drawing)
            try:
                next_page = ('xpath', "//button[@class='btn-next']//span")
                self.click(next_page)
                self.logger.info('个人中心验证进入样图下载列表点击下一页按钮')
            except:
                downlod_user = ('xpath', "//div[@id='downdemo' and @style='']/div[1]/div[1]/ul/li[1]/p[1]")
                actual = self.getText(downlod_user)
                expect = '132'
                self.assert_in_abnormal(expect, actual)
                self.logger.info('账号管理-样图下载：只有一页信息')
        except Exception as e:
            self.logger.error('测试个人中心验证进入样图下载列表异常%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("测试个人中心验证进入样图下载列表失败")
            raise e
        self.home_button()
