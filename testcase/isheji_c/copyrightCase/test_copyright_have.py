from pages.isheji_c.copyrightPage.copyrightPic import Copyright
from pages.basePage import Action
from pages.isheji_c.loginPage import Exit_Load
from pages.isheji_c.loginPage import LoginPage
from common.readLog import Log


# ====================================================================
# 测试版权图片用户有下载份额
# 该用户未终身VIP，并且有份额
# ====================================================================

class TestCopyrightPic:
    '''有企业且有份额'''
    log = Log(__name__)
    logger = log.getLog()

    def test_get_url(self, driver):
        '''验证进入素材库首页功能'''
        # 系统回到首页，然后退出登录,重新登录新的账号
        Action(driver).transfer_url("")
        Action(driver).sleep()
        Exit_Load(driver).exit_action()
        Action(driver).sleep()
        # 再次登录
        self.logger.info("开始切换账号")

        Action(driver).appoint_url(LoginPage(driver).swith_longVip_online, LoginPage(driver).swith_longVip_test)

        Action(driver).sleep()

        Action(driver).transfer_url("/sucai")

    def test_download_pic(self, driver):
        '''验证在版权图片页，下载样图'''
        Copyright(driver).test_download_pic()
        Action(driver).sleep()

    def test_see_similar_pic(self, driver):
        '''验证在版权图片页，查看相似图片'''
        Copyright(driver).test_see_similar_pic()
        Action(driver).sleep()

    def test_collect(self, driver):
        '''验证在版权图片收藏图片'''
        Copyright(driver).test_collect()
        Action(driver).sleep()

    def test_sure_rename_folder(self, driver):
        '''验证在版权图片收藏文件夹新加收藏夹'''
        Copyright(driver).test_sure_rename_folder()
        Action(driver).sleep()