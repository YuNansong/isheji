from pages.basePage import Action
from pages.isheji_c.homePage.user_core import UserCore


class TestUserCenter:

    def test_my_authorzation(self, driver):
        '''验证个人中心进入我的授权--无记录功能'''
        Action(driver).transfer_url()
        Action(driver).sleep()
        UserCore(driver).user_head_portrait()
        Action(driver).sleep()
        UserCore(driver).my_authorzation_download()
        Action(driver).sleep()