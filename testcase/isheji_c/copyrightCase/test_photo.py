from pages.isheji_c.copyrightPage.photoPage import PhotoPage
from pages.basePage import Action
from common.readLog import Log


# =======================================
# 执行爱设计版权素材库介绍页用例
# https://misheji.wxbjq.top/team/photo
# =======================================
class TestPhoto:
    log = Log(__name__)
    logging = log.getLog()

    def test_jump_url(self, driver):
        '''验证访问版权图片素材库首页'''
        self.logging.info("开始访问素材介绍页/team/photo")
        Action(driver).transfer_url("/team/photo")
        Action(driver).sleep()

    def test_click_upgrade(self, driver):
        '''验证访版权图片素材库首页点击升级按钮'''
        PhotoPage(driver).test_click_upgrade()
        Action(driver).sleep()

    def test_click_copyright_experience(self, driver):
        '''验证访版权图片素材库首页，点击立即体验按钮跳转页面是否正确'''
        PhotoPage(driver).test_click_copyright_experience()
        Action(driver).sleep()
