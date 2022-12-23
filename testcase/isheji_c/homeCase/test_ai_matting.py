from common.readLog import Log
from pages.basePage import Action
from pages.isheji_c.homePage.ai_matting import AiMatting


class TestAiMatting:
    log = Log(__name__)
    logger = log.getLog()

    def test_fointo_and_input(self, driver):
        '''进入智能抠图'''
        AiMatting(driver).get_into_matting()
        Action(driver).sleep()

    def test_uploadImg(self, driver):
        '''验证上传图片功能'''
        AiMatting(driver).uploadImg()
        Action(driver).sleep()

    def test_experience(self, driver):
        '''验证体验样图功能'''
        AiMatting(driver).experience()
        Action(driver).sleep()

    def test_background_change(self, driver):
        '''验证更换背景功能'''
        AiMatting(driver).background_change()
        Action(driver).sleep()

    def test_download_back(self, driver):
        '''验证下载功能'''
        AiMatting(driver).download_back()
        Action(driver).sleep()

    def test_unseen_action(self, driver):
        '''验证上一步下一步和调整大小功能'''
        AiMatting(driver).unseen_action()
        Action(driver).sleep()
