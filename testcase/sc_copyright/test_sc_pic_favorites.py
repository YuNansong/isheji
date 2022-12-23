"""
Author  : Milo
Time    : 2022/3/2 11:41
Desc    : 版权站收藏夹的测试用例
"""
from pages.sc_copyright.sc_favoritesPage import FavoritesPage

class TestFavorites:

    def test_add_coll_folder(self,driver):
        '''版权站新增【图片】收藏夹'''
        FavoritesPage(driver).choice_type(1)
        FavoritesPage(driver).test_add_coll_folder()

    def test_rename_folder(self,driver):
        '''版权站重命名【图片】收藏夹'''
        FavoritesPage(driver).test_rename_folder()

    def test_view_folder_pic(self,driver):
        '''版权站查看【图片】收藏夹中有图片'''
        FavoritesPage(driver).test_view_folder_pic(driver)

    def test_view_folder_no_pic(self,driver):
        '''版权站查看【图片】收藏夹中无图片'''
        FavoritesPage(driver).test_view_folder_no_pic()

    def test_folder_move_pic(self,driver):
        '''版权站在【图片】收藏夹中移动图片'''
        FavoritesPage(driver).folder_move_pic(driver)

    def test_folder_delete_pic(self,driver):
        '''版权站在【图片】收藏夹中删除图片'''
        FavoritesPage(driver).test_folder_delete_pic(driver)

    def test_batch_move_pic(self,driver):
        '''版权站在【图片】收藏夹中批量移动图片'''
        FavoritesPage(driver).test_batch_move_pic(driver)

    def test_batch_delete_pic(self,driver):
        '''版权站在【图片】收藏夹中批量删除图片'''
        FavoritesPage(driver).test_batch_delete_pic(driver)

    def test_remove_folder(self,driver):
        '''版权站移除【图片】收藏夹'''
        FavoritesPage(driver).test_remove_folder()