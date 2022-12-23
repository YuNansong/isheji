import random
from model.entModel.entIndexModel import EntIndexModel
from common.path import vcg
from common.readLog import Log
from common.sendDingTalk import SendDingTalk


# ======================================================
# 爱设计版权素材库首页
# https://www.isheji.com/sucai
# ======================================================

class Copyright(EntIndexModel):
    log = Log(__name__)
    logger = log.getLog()

    # 点击热门推荐中的美食
    def click_pic_class(self):
        element = ('xpath', "//div[@data-keyword='美食']/div")
        self.ptclick(element)
        self.sleep(8)
        self.window(-1)

    # 以图片进行搜索图
    def search_for_pictures_with_pictures(self):
        camera = ('xpath', "//div[@class='search-img']//img")  # 定位相机按钮
        self.click(camera)
        self.sleep()

    # 上传图片功能
    def upload_pictures(self):
        inputElement = ('xpath', "//input[@name='file']")
        self.write(inputElement, vcg)

    # 按图片URL搜索
    def search_pic_url(self):
        inputElement = ('xpath', "//div[@class='el-dialog__body']/div[1]/div/input")
        picUrl = "http://photo-static-api.fotomore.com/creative/vcg/400/new/VCG211127896711.jpg"
        self.write(inputElement, picUrl)


    # 点击搜索按钮
    def click_searchBtn(self):
        self.sleep()
        searchBtn = ('xpath', "//div[@class='el-dialog__body']/div[1]/div[1]/div[1]/div/img")
        self.click(searchBtn)

    # ======================================================
    # 爱设计版权素材库搜索结果页
    # https://www.isheji.com/team/photo/search?search
    # ======================================================

    # 搜索图片后跳转到搜索结果页，获取搜索到的图片个数
    def getSearchResult(self, key=""):
        self.window(-1)
        self.sleep(5)
        try:
            self.sleep()
            searchResultElement = ('xpath', "//div[@class='search-response']/span")
            resultValue = self.getText(searchResultElement)
        except:
            self.refresh()
            self.sleep(15)
            searchResultElement = ('xpath', "//div[@class='search-response']/span")
            resultValue = self.getText(searchResultElement)
        num = resultValue[1:-3]
        value = str(num).replace(",", "")
        self.sleep(1)
        self.logger.info("在版权图片页面搜索【%s】得到的搜索个数：%s" % (key, value))
        return int(value)

    # 获取图片列表图片个数
    def get_pic_num(self):
        pic_xpath = ('xpath',"//div[@id='coryright-image-list']/div")
        pic_num = len(self.getElements(pic_xpath))
        return int(pic_num)

    # 鼠标悬停
    def download_hover(self):
        try:
            self.move_to_stay(
                "//main[@class='app-main photo-search-main']/div[@id='coryright-image-list']/div[1]/img[1]")
            self.sleep()
        except:
            SendDingTalk().sendDingTalkMsg("版权图片--鼠标悬浮到图片上失败")

    # 验证在版权图片样图页，下载样图
    def download_pic(self):
        try:
            downloadBtn = ('xpath', "//div[@id='coryright-image-list']/div[1]/div[2]/div[1]")  # 图片上的样图下载按钮
            self.click(downloadBtn)
            self.sleep(1)
            try:
                # 如果用户无团队，或者团队无配额是无法下载图片的，则会有错误提示，否则可以下载
                tipsElement = ('xpath', "//p[@class='el-message__content']")
                # 获取提示信息
                tip = self.getText(tipsElement)
                self.logger.info("下载样图获取到的tip:%s" % tip)
            except:
                tip = ""  # 如果真可以下载，则无法获取
        except:
            self.logger.error("没有获取到下载样图按钮")
        return tip

    # 版权图片列表，查看相似图片
    def see_similar(self):
        similarBtn = ('xpath', "//div[@id='coryright-image-list']/div[1]/div[2]/div[2]")  # 图片上的查找相似图片按钮
        self.click(similarBtn)

    # 版权图片列表，收藏素材
    def collect_pic_btn(self):
        collectBtn = ('xpath', "//div[@id='coryright-image-list']/div[1]/div[2]/div[5]")  # 图片上的收藏图片按钮
        self.click(collectBtn)

    # 在收藏夹页面获取收藏按钮属性
    def getCollectAttr(self):
        collectBtn = ('xpath', "//div[@class='move-main']/div[1]/div[2]")  # 选择收藏夹的收藏按钮
        attr = self.getElementAttr(collectBtn, 'class')
        return attr

    # 在收藏夹页面获取收藏文本值
    def getCollectText(self):
        collectBtn = ('xpath', "//div[@class='move-main']/div[1]/div[2]")  # 选择收藏夹的收藏按钮
        return self.getText(collectBtn)

    # 在收藏夹页面点击收藏按钮
    def click_collect(self):
        collectBtn = ('xpath', "//div[@class='move-main']/div[1]/div[2]")  # 选择收藏夹的收藏按钮
        self.ptclick(collectBtn)

    # 新建收藏文件夹
    def add_collect_folder(self):
        addBtn = ('xpath', "//button[contains(text(),'新建收藏夹')]")  # 选择收藏夹的收藏按钮
        self.ptclick(addBtn)

    def rename_folder(self):
        name = "新文件夹" + str(random.randint(0, 1000))
        rename = ('xpath', "//input[@id='addCollectInput']")  # 输入新的文件名称
        self.clear(rename)
        self.sleep(1)
        self.write(rename, name)
        self.sleep(2)
        # 点击确定按钮
        sure_btn = ('xpath', "//div[@class='add-collect-btn']")
        self.ptclick(sure_btn)

    # 确定输入文件夹名称
    def sure_rename_folder(self):
        flag = False
        tip = ""
        folderList = ('xpath', "//div[@class='move-main-item']")
        folderNum = len(self.getElements(folderList))
        while flag == False:
            try:
                self.rename_folder()  # 输入文件夹名称
                self.sleep(1)
                tipsElement = ('xpath', "//p[@class='el-message__content']")
                tip = self.getText(tipsElement)
            except:
                tip = ""
            print("------------", tip)
            if tip == "该收藏夹名字已被使用，请更换收藏夹名字":
                flag = False
            else:
                flag = True
        newfolderNum = len(self.getElements(folderList))
        num = int(newfolderNum) - int(folderNum)
        # print("---------",num)
        # if num >= 1:
        #     folderNameElement = ('xpath',"//div[@class='move-main-item'][last()]/div[1]/p[1]")
        #     folderName = self.getText(folderNameElement)
        # return folderName
        return num

    # 构图
    def search_commposition(self, i):
        goutu = ('xpath', "//div[@class='search-module']/section/div[1]/div[2]/span[" + str(i) + "]")
        name = self.getText(goutu)
        self.click(goutu)
        self.sleep()
        return name

    # 色彩
    def search_color(self, i):
        color = ('xpath', "//div[@class='search-module']/section/div[2]/div[2]/span[" + str(i) + "]")
        self.getText(color)
        self.click(color)
        self.sleep()

    # 种族
    def search_race(self, i):
        race = ('xpath', "//div[@class='search-module']/section/div[3]/div[2]/span[" + str(i) + "]")
        name = self.getText(race)
        self.click(race)
        self.sleep()
        return name

    # 年龄
    def search_age(self, i):
        age = ('xpath', "//div[@class='search-module']/section/div[4]/div[2]/span[" + str(i) + "]")
        name = self.getText(age)
        self.click(age)
        self.sleep()
        return name

    # 人数
    def search_number_of_people(self, i):
        num = ('xpath', "//div[@class='search-module']/section/div[5]/div[2]/span[" + str(i) + "]")
        name = self.getText(num)
        self.click(num)
        self.sleep()
        return name

    # 性别
    def search_sex(self, i):
        sex = ('xpath', "//div[@class='search-module']/section/div[6]/div[2]/span[" + str(i) + "]")
        name = self.getText(sex)
        self.click(sex)
        self.sleep()
        return name

    # 格式
    def search_format(self, i):
        geshi = ('xpath', "//div[@class='search-module']/section/div[7]/div[2]/span[" + str(i) + "]")
        name = self.getText(geshi)
        self.click(geshi)
        self.sleep()
        return name

    # 在版权图片列表https://www.isheji.com/sucai页面输入关键字
    def search_key(self, key):
        inputElement = ('xpath', "//input[@type='text']")
        self.write(inputElement, key)
        self.sayok(inputElement)
        self.sleep()
        self.window(-1)

    # =======================================
    # 执行用例的方法
    # =======================================
    def test_act_banquan(self):
        # 进入版权站
        self.click_manage()
        self.click_ent_banquan()
        tiyan_assert = ('xpath', "//div[@class='act-btn-item act-btn-create']")
        actual = self.getText(tiyan_assert)
        assert actual == "立即体验"
        self.click(tiyan_assert)
        self.window(-1)

    # 以图片搜索为例
    def test_serach_pic(self):
        self.logger.info("==========开始验证以图片搜索是否正确")
        try:
            self.search_for_pictures_with_pictures()  # 图片搜索
            self.upload_pictures()  # 上传图片
            self.sleep(7)
            # 断言，在搜索结果页验证搜索结果个数
            num = self.getSearchResult()
            self.sleep(2)
            self.close_and_window()
        except:
            self.close_and_window()
            num = 0
        try:
            assert num > 0
        except Exception as e:
            self.logger.error("测试在版权图片以图片搜索断言异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试在版权图片以图片搜索失败")
            raise e

    def test_search_pic_url(self):
        self.logger.info("==========开始验证以图片URL搜索是否正确")
        self.refresh()
        self.sleep(2)
        try:
            self.search_for_pictures_with_pictures()
            self.logger.info("==========开始验证以图片URL搜索是否正确")
            self.search_pic_url()
            self.logger.info("==========输入URL完成")
            self.sleep(2)
            self.click_searchBtn()
            self.logger.info("==========点击搜索完成")
            self.sleep(15)
            num = self.getSearchResult()
            self.sleep(2)
            self.close_and_window()
        except:
            self.close_and_window()
            num = 0
        try:
            assert num > 0
        except Exception as e:
            self.logger.error("测试在版权图片以图片URL搜索断言异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试在版权图片以图片URL搜索失败")
            raise e

    # 在版权图片列表https://www.isheji.com/sucai页面搜索
    def test_banquan_search(self):
        self.logger.info("==========开始验证版权图片列表搜索是否正确")
        self.refresh()
        key = "人物"
        try:
            self.search_key(key)
            # 在搜索结果页面获取搜索到的图片个数
            self.sleep(7)
            num = self.getSearchResult(key)
            self.sleep(2)
            self.close_and_window()
        except:
            self.close_and_window()
            num = 0
        try:
            assert num > 0
        except Exception as e:
            self.logger.error("测试在版权图片搜索关键词结果断言异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试在版权图片以关键词搜索失败")
            raise e

    # 测试下载样图
    def test_download_pic(self):
        self.logger.info("==========开始验证下载样图是否正确")
        tipsList = ["您没有下载样图的额度，请联系创建者", "您没有下载样图的额度，请联系销售", ""]
        try:
            self.click_pic_class()  # 在版权图片页面热门推荐点击美食
            self.sleep()
            self.download_hover()  # 将鼠标悬浮到第一个图片上
            self.sleep(2)
            tip = self.download_pic()
            assert tip in tipsList
        except Exception as e:
            self.logger.error("测试在版权图片下载样图异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试下载样图用例失败")
            assert False

    # 测试在版权图片查找相似图片
    def test_see_similar_pic(self):
        self.logger.info("==========开始验证查找相似图片是否正确")
        try:
            self.download_hover()  # 将鼠标悬浮到第一个图片上
            self.sleep(2)
            self.see_similar()
            self.window(-1)
            self.sleep(5)
            value = self.getSearchResult("查找相似")
            self.close_and_window()
            assert value > 0
        except Exception as e:
            self.logger.error("测试在版权图片查找相似图片异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试查找相似图片用例失败")
            assert False

    # 测试在版权图片上收藏图片
    def test_collect(self):
        try:
            self.sleep(3)
            self.download_hover()  # 将鼠标悬浮到第一个图片上
            self.collect_pic_btn()
            attr = self.getCollectAttr()
            self.sleep(2)
            if attr == "item-right active":
                self.click_collect()
            elif attr == "item-right":
                self.click_collect()
                self.sleep(2)
                self.click_collect()
            self.sleep(2)
            text = self.getCollectText()
            self.logger.info("收藏按钮：%s" % text)
        except Exception as e:
            self.logger.error("测试在版权图片上收藏图片异常%s" % repr(e))

        try:
            assert str(text).strip() == "取消收藏"
        except Exception as e:
            self.logger.error("测试在版权图片上收藏图片断言异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试在版权图片上收藏图片失败")
            assert False

    # 测试在版权图片新增收藏夹
    def test_sure_rename_folder(self):
        try:
            self.add_collect_folder()  # 点击新加收藏夹
            self.sleep(2)
            num = self.sure_rename_folder()
            assert num == 1
            # SendDingTalk().sendDingTalkMsg("测试在版权图片新增收藏夹成功")
        except:
            SendDingTalk().sendDingTalkMsg("测试在版权图片新增收藏夹失败")

        all_handles = self.driver.window_handles
        self.logger.info("all_handles%s" % all_handles)
        if len(all_handles) > 1:
            self.close_and_home_page()
        self.close_and_home_page()
        self.home_button()

    def rightCollect(self):
        collectBtn = ('xpath', "//div[@class='head-right']/div[1]")
        self.ptclick(collectBtn)

    # 按【构图】的分类搜索
    def test_search_commposition(self):
        self.logger.info("==========开始验证按【构图】的分类搜索是否正确")
        try:
            for i in range(1, 5):
                name = self.search_commposition(i)
                value = self.getSearchResult(name)
                assert value > 0
        except Exception as e:
            self.logger.error("测试在版权图片按【构图】的分类搜索异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试在版权图片上按【构图】的分类搜索失败")
            raise e

    # 按【色彩】的分类搜索
    def test_search_color(self):
        self.logger.info("==========开始验证按【色彩】的分类搜索是否正确")
        self.refresh()
        try:
            for i in range(1, 9):
                self.search_color(i)
                self.sleep(2)
                value = self.getSearchResult()
                assert value > 0
        except Exception as e:
            self.logger.error("测试在版权图片按【色彩】的分类搜索异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试在版权图片上按【色彩】的分类搜索失败")
            raise e

    # 按【种族】的分类搜索
    def test_search_race(self):
        self.logger.info("==========开始验证按【种族】的分类搜索是否正确")
        self.refresh()
        try:
            for i in range(1, 9):
                name = self.search_race(i)
                value = self.getSearchResult(name)
                assert value > 0
        except Exception as e:
            self.logger.error("测试在版权图片按【种族】的分类搜索异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试在版权图片上按【种族】的分类搜索失败")
            raise e

    # 按【年龄】的分类搜索
    def test_search_age(self):
        self.logger.info("==========开始验证按【年龄】的分类搜索是否正确")
        self.refresh()
        try:
            for i in range(1, 8):
                name = self.search_age(i)
                value = self.getSearchResult(name)
                assert value > 0
        except Exception as e:
            self.logger.error("测试在版权图片按【年龄】的分类搜索异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试在版权图片上按【年龄】的分类搜索失败")
            raise e

    # 按【人数】的分类搜索
    def test_search_number_of_people(self):
        self.logger.info("==========开始验证按【人数】的分类搜索是否正确")
        try:
            for i in range(1, 7):
                name = self.search_number_of_people(i)
                value = self.getSearchResult(name)
                assert value > 0
        except Exception as e:
            self.logger.error("测试在版权图片按【人数】的分类搜索异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试在版权图片上按【人数】的分类搜索失败")
            raise e

    # 按【性别】的分类搜索
    def test_search_sex(self):
        self.logger.info("==========开始验证按【性别】的分类搜索是否正确")
        self.refresh()
        try:
            for i in range(1, 4):
                name = self.search_sex(i)
                value = self.getSearchResult(name)
                assert value > 0
        except Exception as e:
            self.logger.error("测试在版权图片按【性别】的分类搜索异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试在版权图片上按【性别】的分类搜索失败")
            raise e

    # 按【格式】的分类搜索
    def test_search_format(self):
        self.logger.info("==========开始验证按【格式】的分类搜索是否正确")
        self.refresh()
        try:
            for i in range(1, 6):
                name = self.search_format(i)
                value = self.getSearchResult(name)
                pic_num = self.get_pic_num()
                if pic_num > 0:
                    assert value > 0
                else:
                    assert value == 0
        except Exception as e:
            self.logger.error("测试在版权图片按【格式】的分类搜索异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试在版权图片上按【格式】的分类搜索失败")
            raise e
        self.sleep(1)

    # 在版权图片列表点击右上角收藏
    def test_right_collect(self):
        try:
            self.rightCollect()
            self.sleep(3)
            self.window(-1)
            url = self.getUrl()
            self.logger.info("在版权图片列表点击右上角收藏按钮后获取到的地址为%s" % url)
            assert "/team/photo/collect" in url
            self.sleep(2)
            self.close_handle()
        except Exception as e:
            self.logger.error("在版权图片列表点击右上角收藏按钮异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试在版权图片列表点击右上角收藏按钮功能失败")
            raise e
    # [企业]在版权图片列表点击右上角收藏
    def test_qiye_right_collect(self):
        try:
            self.rightCollect()
            self.sleep(3)
            self.window(-1)
            url = self.get_qiye_url()
            self.logger.info("在版权图片列表点击右上角收藏按钮后获取到的地址为%s" % url)
            assert "collect.html" in url
            self.sleep(2)
            self.close_handle()
        except Exception as e:
            self.logger.error("在版权图片列表点击右上角收藏按钮异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试在版权图片列表点击右上角收藏按钮功能失败")
            raise e
