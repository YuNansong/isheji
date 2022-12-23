from common.readLog import Log
from common.sendDingTalk import SendDingTalk
from model.scModel.musicModel import MusicModel
from model.scModel.vipModel import VIPModel
from model.scModel.commModel import CommModel

#===========================
#   音乐模块
#   2022-5-24
#   Milo
#==========================
class ScMusic(MusicModel,CommModel,VIPModel):

    log = Log(__name__)
    logger = log.getLog()

    def test_into_music(self):
        '''进入音乐模块'''
        try:
            self.click_music_menu()
            num = self.get_search_result()
            self.logger.info(f'进入音乐模块，搜索到{num}个音乐素材')
            assert num > 0
        except Exception as e:
            self.logger.error("失败：进入音乐%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：进入音乐")
            raise e


     # 在首页点击音乐，进入音乐详情
    def act_music_detail(self,driver):
        try:
            fst_msc = ('xpath', "//div[@class='zonggd']/div[1]")
            # loc = self.getElementLocation(fst_msc)
            # x = loc.get('x')
            # y = loc.get('y')
            # self.xyleft_click(driver,x+3,y+150) # 点击坐标
            self.mouse_hover(fst_msc)
            self.click(fst_msc)
            # self.move_to_element_with_offset(fst_msc) # 点击音乐模块的空白处进入音乐详情
            self.sleep(1)
            self.window(-1)
            # 第一个音乐的名称
            music_name = self.get_music_name()
            self.logger.info("在音乐详情页获取音乐名称 %s" %music_name)
            assert music_name != ""
        except Exception as e:
            self.logger.error("在首页点击音乐，进入音乐详情异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在首页点击音乐，进入音乐详情异常")
            raise e

    # 个人下载音乐--无权益
    def download_music_no_interests(self,driver):
        try:
            self.click_music_menu()
            self.act_music_detail(driver)
            self.sleep(2)
            self.window(-1)
            self.download_music_btn()
            self.sleep(1)
            final_price = self.get_alert_price()
            self.alert_close_btn()
            assert float(final_price) > 0
        except Exception as e:
            self.logger.error("个人点击下载音乐弹出支付弹框异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("个人点击下载音乐弹出支付弹框异常")
            raise e

    # 团队下载音乐--有权益
    def download_music_interests(self):
        self.download_music_btn()
        self.sleep(1)
        # 可以进下载记录获取

    def play_music(self):
        '''播放音乐'''
        try:
            play_button = ('xpath', "//div[@class='img-box']//div[@class='play-btn']//img")
            self.click(play_button)
            self.sleep(3)
            self.click(play_button)
            time_path = ('xpath', "//span[@class='start-time']")
            pass_time = self.getText(time_path)
            time_num = pass_time.split(':')
            int_time_num = time_num[1]
            self.logger.info(f'音乐播放了{int_time_num}')
            assert int(int_time_num) > 0
        except Exception as e:
            self.logger.error("失败：播放音乐%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：播放音乐")
            raise e
    # 在音乐详情点击收藏音乐
    def music_detail_coll(self):
        try:
            coll_btn = ('xpath', "//div[@class='top']/span[1]") # 收藏按钮
            attr = self.getElementAttr(coll_btn,'class')
            if attr == "collection yse":
                self.click(coll_btn) # 取消收藏
            try:
                self.click(coll_btn)
                title_xpath = ('xpath',"//div[@class='title']")
                title = self.getText(title_xpath)
                assert title == "添加至文件夹"
                self.collectDialog(self.get_folder_is_null())
            except:
                self.logger.error("在音乐详情页点击收藏按钮失败")
        except  Exception as e:
            self.logger.error("音乐详情页收藏失败%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("音乐详情页收藏失败")
            raise e

    # 个人身份 在音乐详情页，点击“单张购买”
    def test_music_detail_buy_vip(self):
        try:
            self.click_leaflet_meal()
            self.sleep(1)
            self.window(-1)
            vip_url = self.getUrl()
            self.close_handle()
            assert "solavip?type=2" in vip_url
        except Exception as e:
            self.logger.error("版权站-在音乐详情页，点击【单张购买】异常异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在音乐详情页，点击【单张购买】异常失败")
            raise e

    #  在音乐详情点击关键词
    def test_music_click_keyword(self):
        try:
            keyname = self.click_keyword()
            self.window(-1)
            key = self.get_input_key()
            assert keyname == key
        except Exception as e:
            self.logger.error("版权站-在音乐详情页点击关键词异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("版权站-在音乐详情页点击关键词失败")
            raise e
    # 在音乐详情点击推荐音乐'''
    def recommended_music(self,driver):
        try:
            self.sleep(2)
            two_music = ('xpath',"//div[@class='recommend']/h2")
            self.custom_scroll_bar(two_music)
            two_music_img = ('xpath',"//div[@class='recommend']/div[1]/div/div[2]//div[@class='play-bg']/img")
            self.mouse_hover(two_music)
            self.move_to_element_with_offset(two_music_img)
            self.window(-1)
            self.sleep(2)
            music_name = self.get_music_name()
            self.logger.info("推荐列表获取到的音乐名称 %s"% music_name)
            assert music_name !=""
        except Exception as e:
            self.logger.error("失败：进入音乐详情页断言%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("失败：进入音乐详情页断言")
            raise e

    # 清空音乐搜索输入框，重新输入关键词搜索
    def search_music(self):
        try:
            sc_text = "电子"
            self.clear_search_input()
            self.write_search_input(sc_text)
            self.click_search_btn()
            num = self.get_search_result()
            assert num > 0
            self.sleep(2)
        except Exception as e:
            self.logger.error("版权站-音乐列表搜索音乐异常:%s" % {e})
            SendDingTalk().sendDingTalkMsg("版权站-音乐列表搜索音乐异常")
    # 添加音乐到收藏
    def AddCollect(self):
        try:
            self.hover_music()
            self.sleep(1)

            # 1 如果没有弹窗，则取消收藏，如果弹窗了则为收藏
            try:
                self.click_coll_btn()
                title_xpath = ('xpath',"//div[@class='title']")
                title = self.getText(title_xpath)
                assert title == "添加至文件夹"
            except:
                self.click_coll_btn()
            self.sleep(2)
            self.collectDialog(self.get_folder_is_null())
        except Exception as e:
            self.logger.error("版权站-音乐列表点击收藏按钮异常:%s" % {e})
            SendDingTalk().sendDingTalkMsg("版权站-音乐列表点击收藏按钮异常")

    # 收藏音乐异常处理
    def collectDialog(self, num):
        try:
            if num == 0:
                # 没有收藏夹，创建,创建完成后点击第一个li
                # self.click_new_folder_btn()
                self.writh_folder_name()
                self.click_submmit()
                self.select_first_folder()
                self.click_submmit()
            else:
                self.select_first_folder()
                self.click_submmit()
                self.sleep(2)
        except Exception as e:
            self.logger.error("版权站-音乐搜索页点击添加收藏异常:%s" % {e})
            SendDingTalk().sendDingTalkMsg("版权站-音乐搜索页点击添加收藏异常")

    # 取消音乐收藏
    def CancelCollect(self):
        try:
            self.hover_music()
            self.click_coll_btn()
            self.sleep(2)
        except Exception as e:
            self.logger.error("版权站-音乐搜索页点击取消收藏异常:%s" % {e})
            SendDingTalk().sendDingTalkMsg("版权站-音乐搜索页点击取消收藏异常")

    # 在音乐列表播放音乐操作
    def test_musicList_play(self):
        try:
            self.musicList_play()
        except Exception as e:
            self.logger.error("版权站-音乐列表点击播放音乐播放异常:%s" % {e})
            SendDingTalk().sendDingTalkMsg("版权站-音乐列表点击播放音乐播放异常")

    # 在音乐列表暂停音乐操作
    def test_musicList_pause(self):
        try:
            self.musicList_pause()
        except Exception as e:
            self.logger.error("版权站-音乐列表点击暂停音乐播放异常:%s" % {e})
            SendDingTalk().sendDingTalkMsg("版权站-音乐列表点击暂停音乐播放异常")