"""
Author  : Milo
Time    : 2022/3/2 11:41
Desc    : 版权站收藏夹的测试用例
"""
from pages.sc_copyright.sc_favoritesPage import FavoritesPage

class TestDesignFavorites:

    def test_add_coll_folder(self,driver):
        '''版权站选择【设计】收藏夹列表'''
        FavoritesPage(driver).choice_type(2)
        FavoritesPage(driver).test_add_coll_folder()

    def test_rename_folder(self,driver):
        '''版权站重命名【设计】收藏夹'''
        FavoritesPage(driver).test_rename_folder()

    def test_view_folder_pic(self,driver):
        '''版权站查看【设计】收藏夹中有模板'''
        FavoritesPage(driver).test_view_folder_pic(driver)

    def test_view_folder_no_pic(self,driver):
        '''版权站查看【设计】收藏夹中无模板'''
        FavoritesPage(driver).test_view_folder_no_pic()

    def test_folder_move_pic(self,driver):
        '''版权站在【设计】收藏夹中移动模板'''
        FavoritesPage(driver).folder_move_pic(driver)

    def test_folder_delete_pic(self,driver):
        '''版权站在【设计】收藏夹中删除模板'''
        FavoritesPage(driver).test_folder_delete_pic(driver)

    def test_batch_move_pic(self,driver):
        '''版权站在【设计】收藏夹中批量移动模板'''
        FavoritesPage(driver).test_batch_move_pic(driver)

    def test_batch_delete_pic(self,driver):
        '''版权站在【设计】收藏夹中批量删除模板'''
        FavoritesPage(driver).test_batch_delete_pic(driver)

    def test_remove_folder(self,driver):
        '''版权站移除【设计】收藏夹'''
        FavoritesPage(driver).test_remove_folder()