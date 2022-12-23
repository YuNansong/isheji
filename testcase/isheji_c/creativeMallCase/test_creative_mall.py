from common.getYaml import url
from pages.basePage import Action
from pages.isheji_c.creativeMallPage.creative_mall import CreativeMall


class TestCreativeMall:

    def test_act_mall(self, driver):
        '''验证进入创意热店功能'''
        urlInfo = url['url']['testUrl']
        if urlInfo == "https://misheji.wxbjq.top":
            driver.get("https://v1-isj-idea.wxbjq.top/")
        elif urlInfo == "https://www.isheji.com":
            driver.get("https://idea.isheji.com/")
        Action(driver).sleep()

    def test_find_key_word(self, driver):
        '''验证创意热店搜索功能'''
        CreativeMall(driver).find_key_word()
        Action(driver).sleep()

    def test_screen(self, driver):
        '''验证创意热店筛选后点击'''
        CreativeMall(driver).screen()
        Action(driver).sleep()

    def test_recommend(self, driver):
        '''验证创意热店立即询价'''
        CreativeMall(driver).recommend()
        Action(driver).sleep()

    def test_right_top_seach(self, driver):
        '''验证创意热店右上角搜索'''
        CreativeMall(driver).right_top_seach()
        Action(driver).sleep()
