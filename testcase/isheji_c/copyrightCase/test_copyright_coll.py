from pages.isheji_c.copyrightPage.copyrightPicColl import CopyrightPicColl
from pages.basePage import Action


# ======================================================
# 爱设计版权图片--收藏页面用例
# https://www.isheji.com/team/photo/collect
# ======================================================
class TestCopyrightPicColl:

    def test_act_collect(self, driver):
        '''访问版权图片收藏列表'''
        Action(driver).transfer_url("/team/photo/collect")
        Action(driver).sleep(2)

    def test_add_folder(self, driver):
        '''访问版权图片收藏列表添加收藏夹'''
        CopyrightPicColl(driver).test_add_folder()
        Action(driver).sleep(2)

    def test_update_folder(self, driver):
        '''访问版权图片收藏列表重命名收藏夹'''
        CopyrightPicColl(driver).test_update_folder()
        Action(driver).sleep(2)

    def test_view_folder(self, driver):
        '''访问版权图片收藏列表查看收藏夹中的图片'''
        CopyrightPicColl(driver).test_view_folder()
        Action(driver).sleep(2)

    def test_delete_folder(self, driver):
        '''访问版权图片收藏列表删除收藏夹'''
        CopyrightPicColl(driver).test_delete_folder()
        Action(driver).sleep(2)
