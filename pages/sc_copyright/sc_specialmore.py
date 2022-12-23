from pages.sc_copyright.sc_homePage import SCHomePage
from common.sendDingTalk import SendDingTalk
from common.readLog import Log
from element.sc_copyright.sc_home_element import SCHomePageElement
from element.sc_copyright.sc_special_element import SpecialmoreElement
from model.scModel.favoritesModel import FavoritesModel
from model.scModel.specialModel import SpecialModel
from model.scModel.commModel import CommModel


class SpecialPage(FavoritesModel, SpecialModel, CommModel):
    log = Log(__name__)
    logger = log.getLog()

    def click_special(self):
        self.click(SCHomePageElement.zt)

    def click_specialmore(self):
        self.click(SCHomePageElement.zt_more_btn_element)
        self.sleep(3)
        self.window(-1)

    def test_act_special(self, driver):
        try:
            self.click_special()  # 1、从首页点击某个专题
            self.click_specialmore()  # 2、查看更多
            self.window(-1)
            # 获取 第一张图片属性，
            attr = self.zt_get_pic_alt()
            self.zt_click_first_pic()  # 在专题上点击第一张图片
            self.sleep(2)
            self.window(-1)
            name = self.zt_get_pic_name()
            assert attr == name
            self.close_handle()
        except Exception as e:
            self.logger.error("版权站-首页点击专题推荐异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-首页点击热门图集失败")
            raise e

    # 在专题页 收藏
    def test_special_coll(self, driver):
        try:
            self.click_specialmore()  # 2、查看更多
            self.window(-1)
            # 收藏第一张图片
            self.zt_hover_first_pic()
            self.sleep(1)
            alt = self.design_is_coll_pic(SpecialmoreElement.pic_coll_alt)
            if alt == False:  # 已收藏
                self.click(SpecialmoreElement.pic_coll_btn)
            self.sleep(2)
            alt = self.design_is_coll_pic(SpecialmoreElement.pic_coll_alt)
            tips = self.coll_material(alt, SpecialmoreElement.pic_coll_btn, driver)
            self.logger.info("获取到的收藏成功提示：%s" % tips)
            assert "素材已成功" in tips
        except Exception as e:
            self.close_handle()  # 关闭多余窗口
            self.logger.error("版权站-专题页-收藏图片异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-专题页-收藏图片失败")
            raise e

    # 专题页面相似图片
    def test_special_search_smiler(self, driver):
        try:
            self.zt_hover_first_pic()  # 悬浮到第一张图片上
            self.zt_click_xs_pic()  # 点击相似图片按钮
            self.sleep(3)
            self.window(-1)
            # 获取 图片个数
            pic_num = self.zt_get_xs_pic_list()
            self.close_handle()  # 关闭多余窗口
            assert pic_num > 0
        except Exception as e:
            self.close_handle()  # 关闭多余窗口
            self.logger.error("版权站-专题页-查看相似图片异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-专题页-查看相似图片失败")
            raise e

    # 点击某个专题下载样图--无下载额度
    def test_special_download(self, driver):
        try:
            self.click_special()  # 1、从首页点击某个专题
            self.click_specialmore()  # 2、查看更多
            self.zt_hover_first_pic()  # 悬浮到第一张图片上
            self.zt_click_yt_pic()  # 点击下载样图
            title = SCHomePage(driver).apply_title()
            assert title == "下载成功"
        except Exception as e:
            self.close_handle()  # 关闭多余窗口
            self.logger.error("版权站-专题页-无下载额度异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-专题页-无下载额度失败")
            raise e
