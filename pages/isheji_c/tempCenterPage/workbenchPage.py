from common.sendDingTalk import SendDingTalk
from common.path import jepg
from common.readLog import Log
from element.isheji_c.workbench.workbenchElement import WorkBenchElement
from model.entModel.entIndexModel import EntIndexModel
from pages.basePage import Action


class WorkBench(EntIndexModel):
    log = Log(__name__)
    logger = log.getLog()

    # 在工作台点击跳过按钮
    def jump_home(self):
        self.logger.info("进入工作台点击跳过按钮")
        self.refresh()
        self.click(WorkBenchElement.experience_now)
        # self.click(WorkBenchElement.jump_btn_element)
        self.sleep(1)

    # 在工作台点击保存按钮
    def save_btn(self):
        self.logger.info("在工作台点击保存按钮")
        self.click(WorkBenchElement.save_btn_element)

    # 获取模板ID
    def get_temp_id(self):
        temp_id_xpath = ('xpath', "//div[@class='i-design-canvas']")
        temp_id = self.getElementAttr(temp_id_xpath, 'id')
        return temp_id

    # 在工作台页面获取素材按钮元素
    def work_material_text(self):
        sucai_text = self.getText(WorkBenchElement.sucai_btn_element)
        sucai = sucai_text.strip()
        return sucai

    # 企业端进入模板中心
    def test_act_temp_center(self):
        self.click_manage()
        self.click_temp_center()

    def info_workbench(self):
        # 首页选中某个模板
        self.ptclick(WorkBenchElement.temp_element)
        self.sleep()
        self.window(-1)
        try:
            self.jump_home()
        except:
            self.logger.info("进入工作台跳过按钮没有出现")
            self.sleep(1)

    def test_qiye_info_workbench(self):
        # 首页选中某个模板
        self.ptclick(WorkBenchElement.qiye_temp_element)
        self.sleep()
        self.window(-1)
        try:
            self.jump_home()
        except:
            self.logger.info("进入工作台跳过按钮没有出现")
            self.sleep(1)

    def asser_moner_isture(self):
        '''验证收款的金额和要支付的金额是否一致'''
        try:
            self.sleep(3)
            buy_money = ('xpath', "//li[@class='isj-pay-content-card-price isj-pay-content-card-selected']//span")
            parameter1 = self.getText(buy_money)
            self.sleep(1)
            pay_money = ('xpath', "//span[@class='isj-pay-amount-paid-price']")
            parameter2 = self.getText(pay_money)
            self.assert_text(parameter1, parameter2)
            self.sleep(1)
            x_button = (
                'xpath', "//i[@class='iconfont-isj icon-isj-login-close close_button']")
            self.click(x_button)
            self.retention_window()
        except Exception as e:
            self.logger.error('失败:收款的金额和要支付的金额不一致或获取信息失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:收款的金额和要支付的金额不一致或获取信息失败")
            raise e

    # ====================================================================
    # 测试进入工作台页面, 保存模板并下载模板
    # ====================================================================
    def test_download_temp(self, driver):
        try:
            self.save_btn()  # 保存模板
            self.ptclick(WorkBenchElement.downloadBtn_element)  # 点击工作台右上角的下载按钮
            self.sleep(2)
            self.ptclick(WorkBenchElement.download_btn_dialog_element)  # 点击工作台右上角的下载按钮弹窗的浮层出现的下载按钮
            self.sleep(10)
            self.screenshot_new("下载模板成功")
            downloadSuccTip = self.getText(WorkBenchElement.download_ast_element)
            self.assert_text(downloadSuccTip, "作品下载成功")
            self.logger.info("在工作台页面下载图片成功提示:%s" % downloadSuccTip)
            # 关两次页面
            self.close_handle()
        except Exception as e:
            self.logger.error("在工作台操作下载，下载按钮出现异常%s" % repr(e))
            self.close_handle()

    # =====================================
    # 普通用户点击精选模板用于测试非vip功能
    # =====================================
    # 普通用户点击精选模板用于测试非vip功能
    def test_act_workbench(self):
        '''点击精选模版'''
        self.sleep(2)
        try:
            muban_class = ('xpath', "//div[@id='apptc']/div[@class='vertical']")  # 所有模板行
            muban_class_num = len(self.getElements(muban_class))  # 所有模板行数
            self.logger.info("获取到的模板分类为%d" % muban_class_num)
            for j in range(1, muban_class_num + 1):  # 循环所有分类的模板
                vipfree_ele = ('xpath',"//div[@id='apptc']/div[@class='vertical'][" + str(j) + "]/div[2]//div[@class='item-vipfree']")
                vipfree_num = len(self.getElements(vipfree_ele))  # 得到免费的个数
                # 获取首页元素
                eleList = ('xpath', "//div[@id='apptc']/div[@class='vertical'][" + str(j) + "]/div[2]/div[1]/div[1]/div")  # 每个模板分类的第一个模板
                num = len(self.getElements(eleList))  # 获取一行有多少个模板，用于找免费标签
                if num != vipfree_num:
                    for i in range(1, num + 1):
                        ele = ('xpath', "//div[@id='apptc']/div[@class='vertical'][" + str(j) + "]/div[2]/div[1]/div[1]/div[" + str(i) + "]/div[@class='item-vipfree']")  # 找到免费的标签
                        new_num = len(self.getElements(ele))  # 获取一个列表的长度
                        if i == 6:
                            right_button = ('xpath', "//div[@id='apptc']/div[@class='vertical'][" + str(j) + "]/div[2]/div[2]")  # 右滑功能
                            self.click(right_button)  # 点击右滑按钮，展示更多的模板
                        if new_num == 0:
                            vip_mode = ('xpath', "//div[@id='apptc']/div[@class='vertical'][" + str(j) + "]/div[2]/div[1]/div[1]/div[" + str(i) + "]")
                            self.click(vip_mode)
                            break
                        elif new_num > 0:
                            continue
                    break
                else:
                    continue
        except:
            self.logger.info("进入工作台抛出了异常，进入指定的模板url")
            self.appoint_url(
                self.transfer_url("/designworkbench.html?mode=2&from=1&tid=59086&ckey=mobile-poster&nature=user"),
                self.transfer_url("/designworkbench.html?mode=2&from=1&tid=36960&ckey=e-commerce-poster&nature=user"))
        self.sleep(8)
        self.window(-1)
        try:
            self.jump_work()
            # self.jump_home()
        except:
            self.logger.info("进入工作台跳过按钮没有出现")
            self.sleep(1)

    def test_watermark_button_value(self):
        '''断言风险按钮:水印'''
        try:
            self.logger.info("进入工作台点击[移除水印，畅享高清模板]按钮")
            self.sleep(2)
            actual = self.getText(WorkBenchElement.watermark_element)
            expect = '移除水印，畅享高清模板'
            self.assert_text(expect, actual)
        except Exception as e:
            self.logger.error('失败:工作台页面断言风险按钮:水印%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:工作台页面断言风险按钮:水印")
            raise e

    def test_click_watermark(self):
        '''水印支付价格断言'''
        try:
            self.logger.info("进入工作台点击[移除水印，畅享高清模板]按钮，获取弹框的价格")
            waterMark_text = self.getText(WorkBenchElement.watermark_element)
            if str(waterMark_text).strip() == '移除水印，畅享高清模板':
                self.click(WorkBenchElement.watermark_element)
                self.asser_moner_isture()
        except Exception as e:
            self.logger.error('失败:工作台页面水印支付价格断言%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:工作台页面水印支付价格断言")
            raise e

    def test_get_risk_button_value(self):
        '''风险提示按钮断言'''
        try:
            self.logger.info("进入工作台点击【安全风险提示】按钮")
            risk_btn_value = self.getText(WorkBenchElement.risk_button_element)  # 当前存在版权风险
            print("risk_btn_value:>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",risk_btn_value)
            self.assert_text('当前存在版权风险', risk_btn_value)
        except Exception as e:
            self.logger.error('失败:工作台页面风险提示按钮断言%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:工作台页面风险提示按钮断言")
            raise e

    def test_click_riskButton(self):
        '''点击风险提示弹窗的支付页面价格'''
        try:
            risk_btn_value = self.getText(WorkBenchElement.risk_button_element)  # 当前存在版权风险
            if risk_btn_value == "当前存在版权风险":
                self.click(WorkBenchElement.risk_button_element)  # 当前存在版权风险
                self.asser_moner_isture()
        except Exception as e:
            self.logger.error('失败:工作台页面点击风险提示弹窗的支付页面价格%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:工作台页面点击风险提示弹窗的支付页面价格")
            raise e

    def test_get_upvip_button_value(self):
        '''升级VIP按钮'''
        try:
            self.logger.info("进入工作台点击升级VIP按钮")
            upvip_text = self.getText(WorkBenchElement.upvip_button_element)
            self.assert_text('开通会员', upvip_text)
        except Exception as e:
            self.logger.error('失败:工作台页面升级VIP按钮%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:工作台页面升级VIP按钮")
            raise e

    def test_click_upvip_button(self):
        '''升级VIP支付页面价格断言'''
        try:
            upvip_text = self.getText(WorkBenchElement.upvip_button_element)
            if str(upvip_text).strip() == "开通VIP":
                self.mouse_hover(WorkBenchElement.upvip_button_element)
                self.click(WorkBenchElement.open_VIP_button)
                self.asser_moner_isture()
        except Exception as e:
            self.logger.error('失败:工作台页面升级VIP支付页面价格断言%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:工作台页面升级VIP支付页面价格断言")
            raise e

    def test_download_upvip_temp(self):
        '''验证在工作台非会员用户下载VIP模板'''
        try:
            self.save_btn()
            try:
                self.click(WorkBenchElement.downloadBtn_element)
            except:
                self.click(WorkBenchElement.downloadBtn_element_other)
            self.sleep(1)
            vip_text = self.getText(WorkBenchElement.download_pay_button)
            if vip_text.strip() == '会员无水印下载':
                self.click(WorkBenchElement.download_pay_button)
                self.asser_moner_isture()
            self.preservation()
            self.close_handle()
        except Exception as e:
            self.logger.error('失败:工作台页面下载支付页面断言%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("失败:工作台页面下载支付页面断言")
            raise e

    # 工作台模板--我的收藏列表
    def template_my_collection(self):
        try:
            self.click(WorkBenchElement.template_element)  # 在工作台点击左侧模板按钮
            self.sleep(3)
            my_collection_name = self.getText(WorkBenchElement.my_collection_tab_element)  # 获取我的收藏tab元素
            if str(my_collection_name).strip() == '我的收藏':
                self.click(WorkBenchElement.my_collection_tab_element)
                self.sleep(2)
                try:
                    if self.getElementAttr(WorkBenchElement.no_template_element,
                                           'src') == "/new/image/workbench/no.png":
                        tips = self.getText(WorkBenchElement.empty_tips_element).strip()
                        self.logger.info("我的收藏列表提示信息：%s" % tips)
                        assert tips == "空空如也～"
                except:
                    tempNum = len(self.getElements(WorkBenchElement.my_collection_temp_list_element))
                    self.logger.info("我的收藏列表收藏的模板数为%d" % tempNum)
                    assert tempNum > 0
        except Exception as e:
            self.logger.error("工作台模板--我的收藏列表获取数据失败%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("工作台模板--我的收藏列表获取数据失败")
            raise e

    # 在工作台--模板--推荐模版列表，循环点击模板'''
    def test_template_while(self):
        self.click(WorkBenchElement.template_element)  # 在工作台点击左侧模板按钮
        self.sleep(2)
        try:
            for num in range(1, 5):
                # 现有模版ID
                template_id = self.getElementAttr(WorkBenchElement.template_path_element, "id")
                self.logger.info("获取到的模板ID为：%s" % template_id)
                # 点击模版
                template = ('xpath', "//section[@class='template-wrap']/ul/li[" + str(num) + "]")
                self.click(template)
                self.sleep(1)
                new_template_id = self.getElementAttr(WorkBenchElement.template_path_element, "id")
                self.logger.info("切换完新模板获取到的模板ID为：%s" % new_template_id)
                assert template_id != new_template_id
        except Exception as e:
            self.logger.error("工作台推荐模板列表切换模板失败%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("工作台推荐模板列表切换模板失败")
            raise e

    # 工作台素材--推荐列表
    def source_material_hot(self):
        try:
            self.click(WorkBenchElement.sucaiMenu_element)
            num = len(self.getElements(WorkBenchElement.hot_sucai_list_element))
            self.logger.info('工作台素材--推荐列表获取到的素材为%d' % num)
            if num > 0:
                shape_text = self.getText(WorkBenchElement.shape_element)
                assert shape_text.strip() == "查看全部"
            else:
                SendDingTalk().sendDingTalkMsg("工作台素材--推荐列表获取到的素材为0,请查看原因")
        except Exception as e:
            self.logger.error('工作台素材--推荐列表获取到的素材失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("工作台素材--推荐列表获取到的素材失败")
            raise e

    # 在素材推荐列表点击素材
    def test_click_hot_material(self):
        try:
            div_num = len(self.getElements(WorkBenchElement.temp_div_num_element))
            self.logger.info('在工作台获取到的div个数为%d' % div_num)
            self.click(WorkBenchElement.sucai_element)
            new_div_num = len(self.getElements(WorkBenchElement.temp_div_num_element))
            self.logger.info('在工作台添加素材后获取到的div个数为%d' % new_div_num)
            assert new_div_num > div_num
        except Exception as e:
            self.logger.error('在工作台素材推荐列表点击素材失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("在工作台素材推荐列表点击素材失败")
            raise e

    # 在素材推荐列表点击素材分类--查看全部
    def test_click_material_class(self):
        try:
            self.click(WorkBenchElement.sucai_class_element)
            if str(self.getText(WorkBenchElement.sucai_class_name_element)).strip() == "形状":
                sucai_num = len(self.getElements(WorkBenchElement.sucai_list_element))
                self.logger.info('在素材推荐列表点击素材分类--查看全部获取到的素材个数为%d' % sucai_num)
                assert sucai_num > 10
        except Exception as e:
            self.logger.error('在素材推荐列表点击素材分类--查看全部失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("在素材推荐列表点击素材分类--查看全部失败")
            raise e

    # 工作台素材--收藏列表
    def material_my_collection(self):
        try:
            self.click(WorkBenchElement.sucaiMenu_element)  # 在工作台点击左侧模板按钮
            my_collection_name = self.getText(WorkBenchElement.my_collection_tab_element)  # 获取我的收藏tab元素
            if str(my_collection_name).strip() == '收藏素材':
                self.click(WorkBenchElement.coll_sucai_tab_element)  # 点击收藏素材tab
                self.sleep(2)
                try:
                    if self.getElementAttr(WorkBenchElement.no_sucai_element, 'src') == "/new/image/workbench/no.png":
                        tips = self.getText(WorkBenchElement.empty_sucai_tips_element).strip()
                        self.logger.info("素材收藏列表提示信息：%s" % tips)
                        assert tips == "空空如也～"
                except:
                    tempNum = len(self.getElements(WorkBenchElement.sucai_list_element))
                    self.logger.info("我的收藏列表收藏的模板数为%d" % tempNum)
                    assert tempNum > 0
        except Exception as e:
            self.logger.error("工作台模板--我的收藏列表获取数据失败%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("工作台模板--我的收藏列表获取数据失败")
            raise e

    def words_written(self):
        '''点击文字，断言标题'''
        try:
            self.click(WorkBenchElement.words_button_element)  # 点击左侧文字按钮
            self.sleep(2)
            title = self.getText(WorkBenchElement.words_title_element)  # 获取文章列表内容
            self.logger.info("工作台页面点击文字获取到的内容：%s" % title)
            assert title.strip() == "点击添加标题"
        except Exception as e:
            self.logger.error("工作台页面点击左侧文字按钮失败%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("工作台页面点击左侧文字按钮失败")
            raise e

    # 点击背景
    def test_click_background(self):
        try:
            self.click(WorkBenchElement.baclground_button_element)
            self.sleep(2)
            actula = self.getText(WorkBenchElement.back_ass_element)
            assert actula.strip() == "图片背景"
        except Exception as e:
            self.logger.error("工作台页面点击背景失败%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("工作台页面点击背景失败")
            raise e

    def test_click_background_color(self):
        try:
            num = len(self.getElements(WorkBenchElement.background_picture_num))
            self.logger.info("工作台页面获取到的背景图个数为%d" % num)
            if num >= 1:
                left_src = self.getElementAttr(WorkBenchElement.background_picture_element, "work_url")
                self.logger.info("工作台页面点击背景--背景图获取到的值%s" % left_src)
                self.click(WorkBenchElement.background_picture_element)
                self.sleep(2)
                src = self.getElementAttr(WorkBenchElement.background_div_element, "src")
                self.logger.info("工作台获取到背景图的值%s" % src)
                assert src in left_src
        except Exception as e:
            self.logger.error("工作台页面点击背景--背景图失败%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("工作台页面点击背景--背景图失败")
            raise e

    # =====================================
    # 便捷模块，上传图片/二维码
    # =====================================

    # 便捷模块删除图片公共操作
    def delete_pic(self):
        self.move_to_stay(WorkBenchElement.pic_move_element)
        self.sleep(2)
        self.click(WorkBenchElement.more_btn_element)
        self.sleep(2)
        self.click(WorkBenchElement.del_btn_element)
        self.sleep(3)

    # 获取便捷模块列表下的图片列表
    def get_pic_num(self):
        self.sleep(2)
        pic_list = self.getElements(WorkBenchElement.pic_element)
        num = len(pic_list)
        self.logger.info("在工作台便捷模块获取到的图片个数为 %d 张" % num)
        return num

    # 便捷上传二维码
    def test_convenient_upload_pic(self):
        try:
            self.click(WorkBenchElement.convenient_button)
            self.sleep(2)
            num = self.get_pic_num()
            if num >= 9:  # 如果超过9个无法上传,先进行删除
                self.delete_pic()
            num = self.get_pic_num()  # 删除完后重新获取图片总张数
            self.write(WorkBenchElement.input_button, jepg)
            self.sleep(2)
            new_num = self.get_pic_num()
            getNum = new_num - num
            assert getNum == 1
        except Exception as e:
            self.logger.error('工作台便捷模块图片列表上传图片失败"%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("工作台便捷模块图片列表上传图片失败")
            raise e

    # 便捷删除图片
    def test_convenient_detele_pic(self):
        try:
            num = self.get_pic_num()
            if num > 0:
                self.delete_pic()
                new_num = self.get_pic_num()  # 获取新的图片总数，确认是否删除成功
                self.logger.info("在工作台便捷模块获取到的图片个数为 %d 张" % new_num)
                getNum = num - new_num
                assert getNum == 1
            else:
                self.logger.info("工作台便捷模块没有可删除的图片了")
        except Exception as e:
            self.logger.error("工作台便捷模块图片列表删除图片失败%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("工作台便捷模块图片列表删除图片失败")
            raise e

    # 生成二维码
    def test_create_qrcode(self):
        qrcode_url = "https://www.isheji.com"
        self.logger.info("在工作台便捷模块生成二维码")
        try:
            num = self.get_pic_num()
            if num >= 9:  # 如果超过9个无法上传,先进行删除
                self.delete_pic()
            self.click(WorkBenchElement.create_qrcode_element)
            self.sleep(1)
            self.clear(WorkBenchElement.input_qrcode_url_element)  # 清空文本框
            self.write(WorkBenchElement.input_qrcode_url_element, qrcode_url)  # 输入url
            self.sleep(3)
            self.click(WorkBenchElement.qrcode_color_btn)
            self.sleep(3)
            self.click(WorkBenchElement.qrcode_color)
            self.sleep(3)
            self.click(WorkBenchElement.create_qrcode_btn)
            self.sleep(3)
            new_num = self.get_pic_num()
            getNum = new_num - num
            assert getNum == 1
        except Exception as e:
            self.logger.error('工作台便捷模块生成二维码失败"%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("工作台便捷模块生成二维码失败")
            raise e

    # =====================================
    # 上传模块，上传图片
    # =====================================

    # 获取列表的图片数量
    def get_up_pic_num(self):
        self.sleep(2)
        pic_list = self.getElements(WorkBenchElement.up_pic_element)
        num = len(pic_list)
        return num

    # 获取已使用的空间
    def get_used_num(self):
        self.sleep(3)
        used_num_str = self.getText(WorkBenchElement.used_num_element)
        num = used_num_str[0:-1]
        unit = used_num_str[-1:]
        # 如果单位为G 则换算为M
        if unit == "G":
            total_num = float(num) * 1024
        else:
            total_num = float(num)
        self.logger.info("在工作台用户已占用空间%f" % total_num)
        return total_num

    # 获取用户总存储空间
    def get_user_total_upload_size(self):
        total_num_str = self.getText(WorkBenchElement.user_total_upload_size_element)
        num = total_num_str[0:-1]  # 数字
        unit = total_num_str[-1:]  # 单位
        # 如果单位为G 则换算为M
        if unit == "G":
            total_num = int(num) * 1024
        else:
            total_num = int(num)
        self.logger.info("在工作台用户总空间%s" % total_num_str)
        return total_num

    # 工作台图片列表上传图片
    def test_up_upload_pic(self):
        try:
            self.click(WorkBenchElement.upload_button_element)
            # 判断该用户是否还有存储空间
            used_num = self.get_used_num()
            total_num = self.get_user_total_upload_size()
            if used_num < total_num:
                num = self.get_up_pic_num()
                self.logger.info("在工作台上传模块获取到的图片个数为 %d 张" % num)
                self.write(WorkBenchElement.realy_input_button, jepg)
                self.sleep(5)
                new_num = self.get_up_pic_num()
                self.logger.info("在工作台上传模块获取到的图片新个数为 %d 张" % new_num)
                getNum = new_num - num
                if getNum == 0:
                    # 图片张数差额为0，有可能是上传失败，所以重新上传一次，然后对比存储大小
                    self.write(WorkBenchElement.realy_input_button, jepg)
                    new_used_num = self.get_used_num()
                    assert new_used_num > used_num
                else:
                    assert getNum == 1
            else:
                self.logger.error("工作台图片列表上传空间不足")
                SendDingTalk().sendDingTalkMsg("工作台图片列表上传空间不足")
        except Exception as e:
            self.logger.error('工作台图片列表上传图片失败"%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("工作台图片列表上传图片失败")
            raise e

    # 在图片列表 删除图片
    def test_up_delete_pic(self):
        try:
            used_num = self.get_used_num()  # 获取目前图片占用空间大小
            pic_num = self.get_up_pic_num()
            self.logger.info("在工作台上传模块获取到的图片个数为 %d 张" % pic_num)
            if pic_num > 0:
                self.move_to_stay(WorkBenchElement.first_picture)
                self.sleep(2)
                self.click(WorkBenchElement.delete_button)
                self.sleep(2)
                new_used_num = self.get_used_num()  # 删除完重新获取目前图片占用空间大小
                assert new_used_num < used_num
            else:
                self.logger.info("工作台上传模块图片列表没有可删除的图片了")
                SendDingTalk().sendDingTalkMsg("工作台上传模块图片列表没有可删除的图片了，请立即查看")
        except Exception as e:
            self.logger.error('工作台图片列表删除图片失败%s' % repr(e))
            SendDingTalk().sendDingTalkMsg("工作台图片列表删除图片失败")
            raise e

    def close_retain(self):
        '''关闭会员挽弹窗'''
        try:
            try:
                refuse = ('xpath', "//div[@class='close-btn']")
                self.click(refuse)
                self.logger.info('关闭会员挽弹窗')
            except Exception as e:
                self.logger.error('关闭会员挽弹窗失败')
                raise e
        except:
            self.logger.info('没有挽留弹窗')

    def info_retain(self):
        '''进入会员挽留弹窗'''
        try:
            try:
                info = ('xpath', "//div[@class='active']")
                self.click(info)
                self.logger.info('关闭会员挽弹窗')
                x_button = ('xpath', "//span[contains(@class,'iconfont icon-no close_button')]")
                self.click(x_button)
            except Exception as e:
                self.logger.error('进入会员挽弹窗失败')
                raise e
        except:
            self.logger.info('没有挽留弹窗')

    def get_collection_quantity(self):#########################
        """进入‘我的’获取收藏素材和模板的数量"""
        self.click(WorkBenchElement.my_button)
        self.click(WorkBenchElement.my_collection)
        all_collection = self.getElements(WorkBenchElement.material_collection)
        int_collection = len(all_collection)#获取到收藏素材的数量
        self.click(WorkBenchElement.my_collection_template)
        self.sleep()
        all_template = self.getElements(WorkBenchElement.template_set)
        int_template = (len(all_template))
        return int_collection, int_template

