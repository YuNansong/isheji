from common.sendDingTalk import SendDingTalk
from pages.basePage import Action
from common.readLog import Log


# =======================================
# 爱设计版权素材库介绍页
# https://misheji.wxbjq.top/team/photo
# =======================================

class PhotoPage(Action):
    log = Log(__name__)
    logger = log.getLog()

    # 获取立即体验按钮文本值
    def getExperienceText(self):
        try:
            tiyan_assert = ('xpath', "//div[@class='act-btn-item act-btn-create']")
            actual = self.getText(tiyan_assert)
            return actual
        except Exception as e:
            self.logger.error('失败:获取立即体验按钮文本值%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:获取立即体验按钮文本值")
            raise e

    # 测试点击版权图片介绍页面的立即体验按钮
    def copyright_experience(self):
        try:
            tiyan = ('xpath', "//div[@class='act-btn-item act-btn-create']")  # 定位立即体验按钮
            self.click(tiyan)
            self.sleep()
            self.window(-1)
        except Exception as e:
            self.logger.error('失败:测试点击版权图片介绍页面的立即体验按钮%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:测试点击版权图片介绍页面的立即体验按钮")
            raise e

    # 在版权图片热门推荐列表，点击右滑按钮
    def right_slide(self):
        try:
            right = ('xpath', "//span[@class='iconfont icon-Unfold1']")
            self.click(right)
        except Exception as e:
            self.logger.error('失败:在版权图片热门推荐列表，点击右滑按钮%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:在版权图片热门推荐列表，点击右滑按钮")
            raise e

    # 在立即体验页面https://www.isheji.com/sucai 获取元素
    def get_copyright_experience_view_attr(self):
        try:
            food_text = ('xpath', "//div[4]//p[1]")
            text = self.getText(food_text)
            return text
        except Exception as e:
            self.logger.error('失败:在立即体验页面https://www.isheji.com/sucai 获取元素%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:在立即体验页面https://www.isheji.com/sucai 获取元素")
            raise e

    # =======================================================
    # 在素材库首页https://www.isheji.com/team/photo 执行测试用例
    # =======================================================

    # 在素材库首页点击升级按钮
    def test_click_upgrade(self):
        try:
            upgradeElement = ('xpath', "//div[@class='upgrade-btn']")
            self.click(upgradeElement)
            self.sleep(1)
            upgradeText = ('xpath', "//p[@class='upgrade-text']")
            text = self.getText(upgradeText)
            self.sleep(1)
            # 关闭二维码弹框
            closedBtn = ('xpath', "//button[@class='el-dialog__headerbtn']")
            self.ptclick(closedBtn)
            assert str(text).strip() == "微信扫码联系客服获得升级"
        except Exception as e:
            self.logger.error('失败:在素材库首页点击升级按钮%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:在素材库首页点击升级按钮")
            raise e

    # 验证在素材库首页，点击立即体验按钮跳转页面是否正确
    def test_click_copyright_experience(self):
        try:
            self.logger.info("==========开始验证在版权图片中心，点击立即体验按钮跳转页面是否正确")
            self.copyright_experience()  # 点击立即体验
            self.sleep()
            self.right_slide()  # 执行右滑按钮
            text = self.get_copyright_experience_view_attr()
            self.appoint_url(self.assert_text("美食", text), self.assert_text("美妆", text))
        except Exception as e:
            self.logger.error('失败:验证在素材库首页，点击立即体验按钮跳转页面是否正确%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:验证在素材库首页，点击立即体验按钮跳转页面是否正确")
            raise e
