import random
from pages.basePage import Action
from common.readLog import Log
from common.sendDingTalk import SendDingTalk


# ======================================================
# 爱设计版权图片--收藏页面用例
# https://www.isheji.com/team/photo/collect
# ======================================================
class CopyrightPicColl(Action):
    log = Log(__name__)
    logger = log.getLog()

    # 获取目前存在的收藏夹个数
    def getFolderNum(self):
        folderList = ('xpath', "//ul[@class='collect-ul']/li")
        folderNum = len(self.getElements(folderList))
        self.logger.info("目前存在的收藏夹个数为:  %d" % folderNum)
        return folderNum

    def add_folder(self):
        addBtn = ('xpath', "//div[@class='collect-btn']")
        self.ptclick(addBtn)

    def inputFolderName(self):
        folderId = random.randint(0, 9999)
        inputText = ('xpath', "//div[@class='el-input']/input")
        self.clear(inputText)
        self.sleep(1)
        self.write(inputText, "收藏夹" + str(folderId))

    def getErrortips(self):
        tipsElement = ('xpath', "//p[@class='el-message__content']")
        tip = self.getText(tipsElement)
        return tip

    # 添加收藏夹
    def test_add_folder(self):
        flag = False
        try:
            # 获取目前收藏夹条数
            folderNum = self.getFolderNum()

            self.add_folder()  # 点击新建按钮
            self.sleep()
            while flag == False:
                try:
                    self.inputFolderName()  # 输入收藏夹名称
                    self.sleep()
                    self.add_folder()  # 为了保存
                    tip = self.getErrortips() #创建成功顶部的提示弹窗
                except:
                    tip = ""
                if tip == "该收藏夹名字已被使用，请更换收藏夹名字":
                    flag = False
                else:
                    flag = True
            self.sleep(2)
            newFolderNum = self.getFolderNum()
            num = int(newFolderNum) - int(folderNum)
            print(num)
            assert num == 1
        except Exception as e:
            self.logger.error("在版权图片收藏列表增加收藏夹异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在版权图片收藏列表增加收藏夹失败")
            raise e

    # 删除收藏夹
    def delete_btn(self):
        last_folder = "//ul[@class='collect-ul']/li[last()]"
        # 移动到最后一个收藏夹
        self.move_to_stay(last_folder)
        self.sleep(1)
        del_btn = ('xpath', "//ul[@class='collect-ul']/li[last()]/div")
        self.ptclick(del_btn)

    # 弹框的确定按钮
    def sure_btn(self):
        sureBtn = ('xpath', "//button[@class='confirm-btn active']")
        self.ptclick(sureBtn)

    # 删除收藏夹
    def test_delete_folder(self):
        try:
            folderNum = self.getFolderNum()
            if folderNum <= 1:
                self.test_add_folder()

            if folderNum >= 2:
                self.delete_btn()
                self.sleep(2)
                self.sure_btn()
            self.sleep(2)
            newFolderNum = self.getFolderNum()
            num = folderNum - newFolderNum
            self.logger.info("获取到最新的收藏夹数为：%d,%d" % (folderNum, newFolderNum))
            assert num == 1
        except Exception as e:
            self.logger.error("在版权图片收藏列表删除收藏夹异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在版权图片收藏列表删除收藏夹失败")
            raise e

    # 查看收藏夹中的内容
    def test_view_folder(self):
        try:
            imgListNum = 0
            folder = ('xpath', "//ul[@class='collect-ul']/li[1]")
            self.ptclick(folder)
            imgNumElement = ('xpath', "//ul[@class='collect-ul']/li[1]/p[2]")
            num = self.getText(imgNumElement)
            if num == "0":
                tipsElement = ('xpath', "//p[@class='data-null-desc']")
                tip = self.getText(tipsElement)
                assert tip == "收藏夹空空如也"
            else:
                imgListElement = ('xpath', "//div[@id='coryright-image-list']/div")
                imgList = self.getElements(imgListElement)
                imgListNum = len(imgList)
            assert int(num) == imgListNum
        except Exception as e:
            self.logger.error("在版权图片收藏列表查看收藏夹中图片异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在版权图片收藏列表查看收藏夹中图片失败")
            raise e

    # 修改收藏夹
    def test_update_folder(self):
        name = ""
        flag = False
        try:
            # 获取最后一个收藏位置
            folderNum = self.getFolderNum()
            if folderNum >= 2:
                self.sleep(2)
                last_folder = ('xpath', "//ul[@class='collect-ul']/li[last()]")
                self.double_click(last_folder)

                while flag == False:
                    try:
                        folderId = random.randint(1500, 3000)
                        renameFolder = ('xpath', "//ul[@class='collect-ul']/li[last()]/div/input")
                        self.clear(renameFolder)
                        self.sleep(1)
                        name = "收藏夹" + str(folderId)
                        self.write(renameFolder, name)
                        self.sleep(1)
                        self.add_folder()  # 为了保存数据
                        self.sleep(1)
                        tip = self.getErrortips()
                    except:
                        tip = ""

                    if tip == "该收藏夹名字已被使用，请更换收藏夹名字":
                        flag = True
                    else:
                        flag = True
            self.sleep(2)
            folderNameElement = ('xpath', "//ul[@class='collect-ul']/li[last()]/p")
            folderName = self.getText(folderNameElement)
            self.logger.info("获取到收藏夹名称%s,%s" % (folderName, name))
            assert folderName == name
        except Exception as e:
            self.logger.error("在版权图片收藏列表重命名收藏夹异常%s" % repr(e))
            SendDingTalk().sendDingTalkMsg("在版权图片收藏列表重命名收藏夹名称失败")
            raise e
