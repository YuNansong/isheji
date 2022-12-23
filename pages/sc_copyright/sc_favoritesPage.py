from common.sendDingTalk import SendDingTalk
from common.readLog import Log
from element.sc_copyright.sc_favoristes_element import FavoristesElement
from model.scModel.favoritesModel import FavoritesModel
from model.scModel.commModel import CommModel


class FavoritesPage(FavoritesModel, CommModel):
    log = Log(__name__)
    logger = log.getLog()

    # 查看收藏夹列表为空的提示
    def test_collFolder_list_empty(self, driver):
        try:
            self.click_img()  # 点击头像
            self.click_coll_folder()  # 在菜单上点击收藏夹
            self.sleep(1)
            self.window(-1)
            tips = self.get_default_tips()
            assert tips.strip() == "你还没有收藏哦，快去收藏吧"
        except Exception as e:
            self.logger.error("在版权站查看收藏夹列表为空的提示异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在版权站查看收藏夹列表为空的提示失败")
            raise e

    # 在收藏夹列表--选择素材类型
    def choice_type(self, i):
        try:
            self.click_img()  # 点击头像
            self.click_coll_folder()  # 在菜单上点击收藏夹
            self.sleep(1)
            self.window(-1)
            self.click_type(i)  # 选择设计tab
        except Exception as e:
            self.logger.error("在版权站收藏夹选择素材类型异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在版权站收藏夹选择素材类型失败")
            raise e

    # 图片--添加收藏夹测试用例
    def test_add_coll_folder(self):
        # 如果名字重复则重新创建
        try:
            # 获取目前收藏夹条数
            total_num = self.getFolderNum()

            self.create_folder()  # 点击新建收藏夹
            self.add_folder()

            newFolderNum = self.getFolderNum()
            num = int(newFolderNum) - int(total_num)

            if num == 0:
                self.logger.error("在版权站增加收藏夹无法增加，请立即查看")
                SendDingTalk().sendDingTalkMsg("在版权站增加收藏夹无法增加，请立即查看")
            assert num == 1
        except Exception as e:
            self.logger.error("在版权站增加收藏夹异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在版权站增加收藏夹失败")
            raise e

    # 重命名收藏夹
    def test_rename_folder(self):
        try:
            self.left_nav_folder()
            total_num = self.getFolderNum()
            if total_num == 0:
                self.create_folder()
                self.add_folder()

            if total_num >= 1:
                # 首先获取原来的名称
                name = self.getText(FavoristesElement.folder_name_element)  # 获取文件夹名称
                # 然后命名
                self.mouse_hover(FavoristesElement.last_folder_element)
                self.sleep(2)
                self.click(FavoristesElement.folder_more_element)  # 点击更多
                self.sleep(1)
                self.click(FavoristesElement.rename_btn_element)  # 点击重命名
                self.add_folder()
                self.sleep(1)
                new_name = self.getText(FavoristesElement.folder_name_element)
                assert new_name != name
        except Exception as e:
            self.logger.error("在版权站增加收藏夹异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在版权站增加收藏夹失败")
            raise e

    # 移除收藏夹
    def test_remove_folder(self):
        try:
            self.left_nav_folder()
            total_num = self.getFolderNum()
            if total_num < 2:
                self.create_folder()
                self.add_folder()

            if total_num >= 2:
                self.mouse_hover(FavoristesElement.last_folder_element)
                self.click(FavoristesElement.folder_more_element)
                self.sleep(1)
                self.click(FavoristesElement.delete_btn_element)
                self.sleep(1)
                self.click(FavoristesElement.del_sure_btn_element)
                new_num = self.getFolderNum()
                num = total_num - new_num
                assert num == 1
            else:
                self.logger.info("在版权站收藏夹个数为0无法删除")
                SendDingTalk().sendDingTalkMsg("在版权站收藏夹个数为0无法删除")
        except Exception as e:
            self.logger.error("在版权站删除收藏夹异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在版权站删除收藏夹失败")
            raise e

    # 获取有图片的收藏夹个数
    def get_active_folder_num(self):
        try:
            active_folder_num = len(self.getElements(FavoristesElement.active_folder_element))
        except:
            active_folder_num = 0
        return active_folder_num

    # 获取无图片的收藏夹个数
    def get_no_active_folder_num(self):
        try:
            no_active_folder_num = len(self.getElements(FavoristesElement.no_active_folder_element))
        except:
            no_active_folder_num = 0
        return no_active_folder_num

    # 获取收藏夹中图片个数
    def get_pic_num(self):
        try:
            pic_num = len(self.getElements(FavoristesElement.pic_element))
        except:
            pic_num = 0
        return pic_num

    # 返回到首页点击收藏图片
    def home_coll_pic(self, driver):
        from pages.sc_copyright.sc_homePage import SCHomePage
        self.window(0)
        SCHomePage(driver).test_coll_pic(driver)
        self.window(-1)
        self.left_nav_order()
        self.left_nav_folder()

    # 查看收藏夹，有数据
    def test_view_folder_pic(self, driver):
        try:
            pic_num = 0
            self.left_nav_folder()
            total_num = self.getFolderNum()
            # 判断收藏夹个数 如果空则创建
            if total_num == 0:
                self.create_folder()
                self.add_folder()

            # 判断收藏夹中有图片的个数 如果0个，则先收藏图片
            if self.get_active_folder_num() < 1:
                self.home_coll_pic(driver)

            # 判断收藏夹中有图片的个数 如果大于0个且有收藏的图片
            if self.get_active_folder_num() >= 1:
                self.click(FavoristesElement.first_act_folder_element)
                pic_num = self.get_pic_num()
                self.logger.info("在版权站查看到的图片个数为%d" % pic_num)
                assert pic_num > 0
                return pic_num
        except Exception as e:
            self.logger.error("在版权站查看有数据的收藏夹异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在版权站查看有数据的收藏夹失败")
            raise e

    # 查看收藏夹，无数据
    def test_view_folder_no_pic(self):
        tips = ""
        try:
            self.left_nav_folder()

            if self.get_no_active_folder_num() == 0:
                self.create_folder()
                self.add_folder()

            # 获取收藏夹是否有收藏的图片
            if self.get_no_active_folder_num() >= 1:
                self.click(FavoristesElement.first_no_act_folder_element)
                self.sleep(1)
                tips = self.getText(FavoristesElement.empty_pic_tips_element)
                assert tips == "你还没有收藏哦，快去收藏吧"
        except Exception as e:
            self.logger.error("在版权站查看空的收藏夹异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("测试在版权站查看空的收藏夹失败")
            raise e

    # 在收藏夹中移动图片
    def folder_move_pic(self, driver):

        try:
            attr1 = ""
            attr2 = ""
            name = ""
            attrList = []
            # 获取到图片个数
            pic_num = self.test_view_folder_pic(driver)
            self.logger.info("移动前图片pic_num:%d" % pic_num)

            if pic_num >= 1:
                # 移动按钮
                attr1 = self.getElementAttr(FavoristesElement.first_pic_href_element, "href")  # 获取到图片ID
                self.logger.info("移动完图片前href属性值:%s" % attr1)
                self.mouse_hover(FavoristesElement.first_pic)
                self.sleep()
                self.click(FavoristesElement.move_btn_element)
                self.sleep(1)
                # 选择收藏夹
                folder_num = len(self.getElements(FavoristesElement.folder_list_element))  # 返回收藏夹个数
                if folder_num < 2:
                    # 弹框上的新建文件夹
                    self.click_new_folder_btn()
                    self.sleep(2)
                    self.add_folder()

                self.sleep(2)
                self.logger.info("在弹框上获取到的收藏夹个数为%d" % folder_num)
                if folder_num >= 2:
                    # 循环遍历
                    for i in range(1, folder_num + 1):
                        folder_li_element = ('xpath', "//ul[@class='collect-list']/li[" + str(i) + "]")
                        folder_name_element = ('xpath', "//ul[@class='collect-list']/li[" + str(i) + "]/p")
                        attr = self.getElementAttr(folder_li_element, "class")
                        if attr != "noclick":
                            name = self.getText(folder_name_element)
                            self.click(folder_li_element)
                            self.logger.info("我选中的新文件夹为：%s" % name)
                            self.click_coll_sure_btn()
                            break
                new_pic_num = self.get_pic_num()
                num = pic_num - new_pic_num
                self.logger.info("移动完图片后图片相差num:%d" % num)
                if num == 0:
                    self.folder_move_pic(driver)
                if num == 1:
                    # 重新进入文件夹
                    self.left_nav_folder()  # 左侧菜单
                    folder_num = self.getFolderNum()
                    for i in range(1, folder_num + 1):
                        folder_element = ('xpath', "//ul[@class='folder']/li[" + str(i) + "]/p")
                        folder_name = self.getText(folder_element)
                        self.logger.info("移动完图片后选择文件夹:%s" % name)
                        if folder_name == name:
                            self.click(folder_element)
                            self.sleep(2)
                            for j in range(1, self.get_pic_num() + 1):
                                href_attr_element = ('xpath', "//div[@class='data-scroll']/div/div[" + str(j) + "]/a")
                                attrList.append(self.getElementAttr(href_attr_element, "href"))
                            self.logger.info("%s" % attrList)
                            assert attr1 in attrList
                            break
            else:
                self.logger.info("在版权站查看收藏夹中的图片个数为0")
        except Exception as e:
            self.refresh()
            self.logger.error("在版权站收藏夹中移动图片异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在版权站收藏夹中移动图片失败")
            raise e

    # 收藏夹中删除图片
    def test_folder_delete_pic(self, driver):
        try:
            # 获取到图片个数
            pic_num = self.test_view_folder_pic(driver)
            self.logger.info("删除前图片个数pic_num:%d" % pic_num)
            if pic_num >= 1:
                # 移动按钮
                attr1 = self.getElementAttr(FavoristesElement.first_pic_href_element, "href")  # 获取到图片ID
                self.mouse_hover(FavoristesElement.first_pic)
                self.sleep()
                self.click(FavoristesElement.delete_pic_btn_element)
                self.sleep(1)
                tips = self.getText(FavoristesElement.delete_succ_element)
                self.logger.info("删除图片成功后的提示:%s" % tips)
                if tips == "删除成功!":
                    new_pic_num = self.get_pic_num()
                    num = pic_num - new_pic_num
                    assert num == 1
            else:
                self.logger.error("要删除的收藏夹中的图片个数为0")
                SendDingTalk().sendDingTalkMsg("要删除的收藏夹中的图片个数为0")
        except Exception as e:
            self.logger.error("在版权站收藏夹中删除图片异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在版权站收藏夹中删除图片失败")
            raise e

    # 收藏夹中批量移动图片
    def test_batch_move_pic(self, driver):
        try:
            self.left_nav_folder()
            # 先获取有2个以上的图片的收藏夹
            if self.get_active_folder_num() < 1:
                # 进行收藏图片
                self.home_coll_pic(driver)

            if self.get_active_folder_num() >= 1:
                flag = True
                for pic_n in range(1, self.get_active_folder_num() + 1):
                    active_folder_num_element = (
                    'xpath', "//ul[@class='folder']/li[@class='hasbox'][" + str(pic_n) + "]/span")
                    picNumText = self.getText(active_folder_num_element)
                    num = int(picNumText[0:-3])
                    if num < 2:
                        flag = False
                        continue
                    else:
                        flag = True
                        break
                if flag == False:
                    self.home_coll_pic(driver)
                    flag = True

                if flag == True:
                    for i in range(1, self.get_active_folder_num() + 1):
                        active_folder_num_element = (
                        'xpath', "//ul[@class='folder']/li[@class='hasbox'][" + str(i) + "]/span")
                        picNumText = self.getText(active_folder_num_element)
                        num = picNumText[0:-3]
                        self.logger.info("num：%s" % num)
                        if int(num) < 2:
                            continue
                        elif int(num) >= 2:
                            self.click(active_folder_num_element)
                            # 开始移动
                            self.mouse_hover(FavoristesElement.first_pic)
                            self.sleep(2)
                            for j in range(1, 3):  # 移动2张
                                pic_check_btn = (
                                'xpath', "//div[@class='data-scroll']/div/div[" + str(j) + "]/div[@class='check-btn']")
                                self.click(pic_check_btn)
                                self.sleep(1)
                            # 点击批量移动按钮
                            self.click(FavoristesElement.batch_move_btn)
                            self.sleep(1)
                            # 选择收藏夹
                            folder_num = len(self.getElements(FavoristesElement.folder_list_element))  # 返回收藏夹个数
                            if folder_num < 2:
                                # 弹框上的新建文件夹
                                self.click_new_folder_btn()
                                self.sleep(2)
                                self.add_folder()

                            self.sleep(2)
                            self.logger.info("在弹框上获取到的收藏夹个数为%d" % folder_num)
                            if folder_num >= 2:
                                # 循环遍历
                                for i in range(1, folder_num + 1):
                                    folder_li_element = ('xpath', "//ul[@class='collect-list']/li[" + str(i) + "]")
                                    folder_name_element = ('xpath', "//ul[@class='collect-list']/li[" + str(i) + "]/p")
                                    attr = self.getElementAttr(folder_li_element, "class")
                                    if attr != "noclick":
                                        name = self.getText(folder_name_element)
                                        self.click(folder_li_element)
                                        self.logger.info("我选中的新文件夹为：%s" % name)
                                        self.click_coll_sure_btn()
                                        break
                        break
        except Exception as e:
            self.logger.error("在版权站收藏夹中批量移动图片异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在版权站收藏夹中批量移动图片失败")
            raise e

    # 收藏夹中批量删除图片
    def test_batch_delete_pic(self, driver):
        try:
            self.left_nav_folder()
            # 先获取有2个以上的图片的收藏夹
            if self.get_active_folder_num() < 1:
                # 进行收藏图片
                self.home_coll_pic(driver)

            if self.get_active_folder_num() >= 1:
                flag = True
                for pic_n in range(1, self.get_active_folder_num() + 1):
                    active_folder_num_element = (
                    'xpath', "//ul[@class='folder']/li[@class='hasbox'][" + str(pic_n) + "]/span")
                    picNumText = self.getText(active_folder_num_element)
                    num = int(picNumText[0:-3])
                    if num < 2:
                        flag = False
                        continue
                    else:
                        flag = True
                        break
                if flag == False:
                    self.home_coll_pic(driver)
                    flag = True

                if flag == True:
                    for i in range(1, self.get_active_folder_num() + 1):
                        active_folder_num_element = (
                        'xpath', "//ul[@class='folder']/li[@class='hasbox'][" + str(i) + "]/span")
                        picNumText = self.getText(active_folder_num_element)
                        num = picNumText[0:-3]
                        self.logger.info("num：%s" % num)
                        if int(num) < 2:
                            continue
                        elif int(num) >= 2:
                            self.click(active_folder_num_element)
                            pic_num = self.get_pic_num()
                            # 开始移动
                            self.mouse_hover(FavoristesElement.first_pic)
                            self.sleep(2)
                            for j in range(1, 3):  # 删除2张
                                pic_check_btn = (
                                'xpath', "//div[@class='data-scroll']/div/div[" + str(j) + "]/div[@class='check-btn']")
                                self.click(pic_check_btn)
                                self.sleep(1)
                            # 点击批量删除按钮
                            self.click(FavoristesElement.batch_delete_btn)
                            self.sleep(1)
                            # 点击弹框的确定按钮
                            self.click(FavoristesElement.del_sure_btn_element)
                            # 重新获取收藏夹中的图片个数
                            self.sleep(2)
                            new_pic_num = self.get_pic_num()
                            num = pic_num - new_pic_num
                            assert num == 2
                        break
        except Exception as e:
            self.logger.error("在版权站收藏夹中批量删除图片异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在版权站收藏夹中批量删除图片失败")
            raise e
