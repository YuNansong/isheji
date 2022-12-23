from pages.isheji_c.copyrightPage.copyrightPic import Copyright
from pages.basePage import Action
from common.readLog import Log


# ============================
#    版权素材页面用例  VIP用户执行
# ============================
class TestCopyrightPic:

    log = Log(__name__)
    logger = log.getLog()

    def test_act_banquan(self, driver):
        '''验证访问版权素材首页功能'''
        self.logger.info("开始执行版权图片素材用例/sucai.html")
        Copyright(driver).test_act_banquan()
        Action(driver).sleep()

    # def test_search_pic(self, driver):
    #     '''验证在版权图片页面，以上传图片进行搜图功能'''
    #     Copyright(driver).test_serach_pic()
    #     Action(driver).sleep()

    # @pytest.mark.skip(reason="加载太慢")
    # def test_search_pic_url(self, driver):
    #     '''验证在版权图片页面，以图片Url进行搜图功能'''
    #     Copyright(driver).test_search_pic_url()
    #     Action(driver).sleep()

    def test_banquan_search(self, driver):
        '''验证在版权页面，banner处筛选功能'''
        Copyright(driver).test_banquan_search()
        Action(driver).sleep()

    def test_download_pic(self, driver):
        '''验证在版权图片样图页，下载样图'''
        Copyright(driver).test_download_pic()
        Action(driver).sleep()

    def test_search_commposition(self, driver):
        '''验证在版权图片页面，按构图筛选功能'''
        Copyright(driver).test_search_commposition()
        Action(driver).sleep(1)

    def test_search_color(self, driver):
        '''验证在版权图片页面，按色彩筛选功能'''
        Copyright(driver).test_search_color()
        Action(driver).sleep(1)

    def test_search_race(self, driver):
        ''' 验证在版权图片页面，按种族筛选功能 '''
        Copyright(driver).test_search_race()
        Action(driver).sleep(1)

    def test_search_age(self, driver):
        '''验证在版权图片页面，按年龄筛选功能'''
        Copyright(driver).test_search_age()
        Action(driver).sleep(1)

    def test_search_number_of_people(self, driver):
        '''验证在版权图片页面，按人数筛选功能'''
        Copyright(driver).test_search_number_of_people()
        Action(driver).sleep(1)

    def test_search_sex(self, driver):
        '''验证在版权图片页面，按性别筛选功能'''
        Copyright(driver).test_search_sex()
        Action(driver).sleep(1)

    def test_search_format(self, driver):
        '''验证在版权图片页面，按图片格式筛选功能'''
        Copyright(driver).test_search_format()
        Action(driver).sleep(1)

    def test_click_right_collect(self, driver):
        '''验证在版权图片列表，点击右上角收藏按钮'''
        Copyright(driver).test_qiye_right_collect()
        Action(driver).sleep(1)
