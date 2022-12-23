import time
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common.path import data_position
from common.getYaml import url
from common.readLog import Log
from common.path import screenshot_path
from common.interface import Interface
from common.sendDingTalk import SendDingTalk


class Action:
    log = Log(__name__)
    logger = log.getLog()

    def __init__(self, driver):
        self.driver = driver

    def appoint_url(self, func1, func2):
        urlInfo = url['url']['testUrl']
        if urlInfo == "https://www.isheji.com":
            func1()
        elif urlInfo == "https://misheji.wxbjq.top":
            func2()

    # 等待时间
    def sleep(self, wait=2):
        time.sleep(wait)

    # 截图
    def screenshot_new(self, filename):
        try:
            today_data = time.strftime("%Y-%m-%d", time.localtime())
            now_time = time.strftime("%H_%M_%S", time.localtime())
            isExists = os.path.exists(screenshot_path + "\\" + today_data)
            if not isExists:
                os.makedirs(screenshot_path + "\\" + today_data)
            self.driver.get_screenshot_as_file(
                screenshot_path + "\\" + today_data + "\\" + filename + "_" + now_time + '.png')
        except:
            self.logger.error("保存截图失败")

    # def decorate_screenshot(self):
    #     path = pictrue_path
    #
    #     def tear_screenshot(name):
    #         nonlocal path
    #         new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #         self.driver.get_screenshot_as_file(path + new_time + name + '.png')
    #         return path
    #
    #     return tear_screenshot

    # 切换到指定网址
    def transfer_url(self, path=''):
        urlInfo = url['url']['testUrl']
        status_code = Interface.getUrlStatus(urlInfo + path)
        if status_code == 200:
            self.driver.get(urlInfo + path)
        else:
            SendDingTalk().sendDingTalkMsg(url + "返回状态码为:" + str(status_code))
    # 访问url
    def act_url(self,url):
        self.driver.get(url)

    # 执行js代码
    def executeJs(self, jscode, element):
        self.driver.execute_script(jscode, element)

    # 滚动页面到元素显示
    def rollWeb(self, locator):
        el = self.driver.find_element(*locator)
        jscode = "arguments[0].scrollIntoView(false);"
        self.executeJs(jscode, el)
        self.sleep(1)

    # 浏览器后退
    def back(self):
        self.driver.back()
        self.sleep()

    # 刷新浏览器
    def refresh(self):
        self.driver.refresh()
        self.sleep()

    # 无token情况下返回url
    def get_current_url(self):
        url = self.driver.current_url
        return url

    # 获取当前窗口的Url
    def getUrl(self):
        url = self.driver.current_url
        status_code = Interface.getUrlStatus(url)
        if status_code == 200:
            return url
        else:
            SendDingTalk().sendDingTalkMsg(url + "返回状态码为:" + str(status_code))
            return url

    # 获取企业url当前窗口的Url
    def get_qiye_url(self):
        url = self.driver.current_url
        status_code = Interface.get_qiye_url_status(url)
        if status_code == 200:
            return url
        else:
            SendDingTalk().sendDingTalkMsg(url + "返回状态码为:" + str(status_code))
            return url

    # 切换到指定网址
    def transfer_qiye_url(self, path=''):
        urlInfo = url['url']['qiyeUrl']
        status_code = Interface.getUrlStatus(urlInfo + path)
        if status_code == 200:
            self.driver.get(urlInfo + path)
        else:
            SendDingTalk().sendDingTalkMsg(url + "返回状态码为:" + str(status_code))
        # 切换到指定网址

    # 由于企业域名比较特殊，所以重新定义了一个方法
    def act_qiye_url(self, path=''):
        urlInfo = url['url']['testUrl']
        status_code = Interface.getUrlStatus(urlInfo + path)
        if status_code == 200:
            self.driver.get(urlInfo + path)
        else:
            SendDingTalk().sendDingTalkMsg(url + "返回状态码为:" + str(status_code))

    def getText(self, locator):
        '''获取元素的文本信息'''
        text = self.driver.find_element(*locator).text
        return text

    # 获取元素属性
    def getElementAttr(self, locator, name):
        return self.driver.find_element(*locator).get_attribute(name)

    # 获取元素结果集
    def getElements(self, locator):
        return self.driver.find_elements(*locator)

    def getElement(self, locator):
        return self.driver.find_elements(*locator)

    # 获取元素坐标
    def getElementLocation(self, locator):
        ele =  self.driver.find_element(*locator)
        loc = ele.location
        return loc
    # 获取cookie
    def saveCookie(self):
        '''
          通过selenium自带get_cookies()方法获取到当前登录账号的cookie，然后存储到cookie.txt文件中
        '''
        cookieFile = data_position + "/cookie.txt"
        cookie = self.driver.get_cookies()
        self.logger.info("获取到的新cookie：%s" % cookie)
        value = ""
        with open(cookieFile, 'w') as f:
            for i in range(cookie.__len__()):
                f.write(cookie[i].get("name") + "=" + cookie[i].get("value") + ";")
        return value

    # =====================点击元素相关======================================================

    def switch_iframe(self, locator):
        '''进入iframe'''
        self.driver.switch_to.frame(self.driver.find_element(*locator))

    def out_of_iframe(self):
        '''退出iframe'''
        self.driver.switch_to.default_content()

    # 等待元素可以被点击
    def wait_element_clickable(self, locator, timeout=5):
        wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=0.2)
        el = wait.until(ec.element_to_be_clickable(locator))
        return el

    # 点击链接
    def wenzi(self, locator):
        self.driver.find_element_by_link_text(locator).click()

    # 普通点击
    def ptclick(self, locator):
        el = self.driver.find_element(*locator)
        # jscode = "arguments[0].setAttribute('style','background: yellow; border: 1px solid red;');"
        # self.executeJs(jscode, el)
        el.click()

    def xyleft_click(self, driver, x, y, left_click=True):
        '''移动到某个坐标'''
        if left_click:
            ActionChains(driver).move_by_offset(x, y).click().perform()
        else:
            ActionChains(driver).move_by_offset(x, y).context_click().perform()
            ActionChains(driver).move_by_offset(-x, -y).perform()  # 将鼠标位置恢复到移动前

    def move_to_element_with_offset(self, loc,xoffset=170,yoffset=160):
        '''
        拖动滚动条
        Usage:
        element = ("id","xxx")
        driver.move_to_element_with_offset(element, xoffset, yoffset)
        '''
        element = self.driver.find_element(*loc)
        # ActionChains(self.driver).click_and_hold(on_element=element).perform()
        ActionChains(self.driver).move_to_element_with_offset(to_element=element, xoffset=xoffset, yoffset=yoffset).click().perform()

    def click(self, locator):
        '''点击'''
        time.sleep(1)
        el = self.wait_element_clickable(locator)
        jscode = "arguments[0].setAttribute('style','background: yellow; border: 1px solid red;');"
        self.executeJs(jscode, el)
        action = ActionChains(self.driver)
        action.click(el).perform()
        time.sleep(2)

    def no_wait_click(self, locator):
        self.driver.find_element(*locator).click()

    def double_click(self, locator):
        '''双击'''
        el = self.wait_element_clickable(locator)
        action = ActionChains(self.driver)
        action.double_click(el).perform()

    def click_and_hold(self, locator):
        '''鼠标点击不松开'''
        action = ActionChains(self.driver)
        action.click_and_hold(*locator).perform()

    def move_to_stay(self, locator):
        '''鼠标悬停：需要xpath路径'''
        path = self.driver.find_element_by_xpath(locator)
        ActionChains(self.driver).move_to_element(path).perform()
        self.sleep(2)

    def mouse_hover(self, locator):
        '''鼠标悬停'''
        path = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(path).perform()
        self.sleep(2)

    def space_key(self, locator):
        '''空格'''
        self.driver.find_element(*locator).send_keys(Keys.SPACE)

    def preservation(self):
        '''工作台保存按钮'''
        saveBtn = ('xpath', "//div[@class='editor-file']//div[@class='save-icon']/div[@class='icon']")
        self.click(saveBtn)

    def write(self, locator, value):
        '''写入'''
        el = self.driver.find_element(*locator)
        el.send_keys(value)

    def clear(self, locator):
        '''清空输入框'''
        el = self.driver.find_element(*locator)
        el.clear()

    def sayok(self, locator):
        '''ENTER键'''
        time.sleep(1)
        self.driver.find_element(*locator).send_keys(Keys.ENTER)

    def page_down(self, number=10000):
        '''鼠标滚动'''
        self.driver.execute_script(f'window.scrollBy(0,{number})')  # 鼠标向下滑动，才会出现搜索框

    # 自定义滚动条
    def custom_scroll_bar(self,locator):
        target = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)


    # ==================对窗口操作===========================
    def window(self, mub):
        '''切换窗口'''
        self.driver.switch_to.window(self.driver.window_handles[mub])

    def switch_to_iframe(self, iframe_reference, timeout=30):
        '''切换iframe'''
        wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=0.2)
        wait.until(ec.frame_to_be_available_and_switch_to_it(iframe_reference))

    def closeWindow(self):
        self.driver.close()

    def close_and_window(self):
        '''关闭当前页面，返回上一页面'''
        winds = self.driver.window_handles
        winds_num = len(winds)
        if winds_num > 1:
            self.driver.close()
            self.window(-1)
        else:
            self.window(0)

    def close_handle(self):
        '''关闭当前页面，返回上一页面'''
        all_handles = self.driver.window_handles
        self.logger.info("all_handles%s" % all_handles)
        if len(all_handles) > 1:
            for i in range(0, len(all_handles)):
                if i == 0:
                    continue
                self.logger.info("handles:   %s" % all_handles[i])
                self.window(-1)
                self.driver.close()
        self.window(0)

    def close_and_home_page(self):
        '''关闭当前页面，回到第一页'''
        winds = self.driver.window_handles
        winds_num = len(winds)
        if winds_num > 1:
            self.window(-1)
            self.driver.close()
            self.window(0)
        else:
            self.window(0)

    def jump_work(self):
        '''工作台跳过按钮'''
        self.logger.info("进入工作台点击跳过按钮")
        # one_jump = ("xparth", "//button[@class='driver-next-btn']")
        # self.click(one_jump)
        # two_jump = ("xpath", "//button[@class='driver-next-btn']")
        # self.click(two_jump)
        # three_jump = ("xpath", "//button[@class='driver-next-btn']")
        # self.click(three_jump)
        # four_jump = ("xpath", "//button[@class='driver-next-btn']")
        # self.click(four_jump)
        self.refresh()
        self.sleep()
        try:
            experience_now = ("xpath", "//button[@class='ant-btn ant-btn-primary btn']")
            self.click(experience_now)
        except:
            self.logger.info("工作台未出现弹窗")
        # self.click(WorkBenchElement.jump_btn_element)
        # jump = ('xpath', "//div[@class='guidance-footer']/div[@class='jump']")
        # self.click(jump)
        time.sleep(1)

    def close_window(self):
        '''关闭浏览器'''
        self.driver.quit()

    def home_button(self):
        '''返回主页按钮，点击页面的Logo'''
        try:
            home_logo = ('xpath', "//img[@class='logo']")
            self.click(home_logo)
        except Exception as e1:
            try:
                home_logo = ('xpath', "//div[@class='header-logo']")
                self.click(home_logo)
            except Exception as e2:
                home_logo = ('xpath', "//div[@class='header-left']/a")
                self.click(home_logo)
        time.sleep(2)

    # ======================工作台页面的操作=============================================================
    def jump_home(self):
        self.logger.info("进入工作台点击跳过按钮")
        jump = ('xpath', "//div[@class='jump']")
        self.click(jump)
        time.sleep(1)

    def jump_after_home(self):
        jump = ('xpath', "//div[@class='guidance-footer']/div[@class='jump']")
        self.click(jump)
        time.sleep(1)
        self.driver.close()
        self.window(0)
        self.home_button()

    def collection_function(self):
        '''收藏按钮'''
        self.move_to_stay("//div[@id='waterfall']//div[1]//div[1]//img[1]")
        lov = ('xpath', "//div[@class='continer']//div[1]//div[1]//div[2]//span[1]")
        self.logger.info('收藏按钮')
        self.click(lov)
        time.sleep(1)

    def see_eye(self):
        '''查看模版按钮'''
        self.move_to_stay("//div[@id='waterfall']//div[1]//div[1]//img[1]")
        ies = ('xpath', "//div[@class='continer']//div[1]//div[1]//div[1]//a[1]//span[1]")
        self.click(ies)
        self.logger.info('查看')

    def next_page_button(self):
        '''下一页按钮'''
        self.flag = False
        hbnext_button = ('xpath', "//button[@class='btn-next']")
        value = self.getElementAttr(hbnext_button, "disabled")
        if value == None:
            self.click(hbnext_button)
            self.logger.info('点击下一页按钮')
            time.sleep(1)
            self.flag = True
        else:
            self.logger.info("只有一页数据，无法点击下一页")
            self.flag = False
        return self.flag

    def ast_next_page(self):
        '''尝试判断能否跳过用例'''
        nxpg = ('xpath', "//button[@class='btn-next']")
        return self.getElementAttr(nxpg, 'disabled')

    def previous_page_button(self):
        '''上一页按钮'''
        if self.next_page_button() == True:
            time.sleep(1)
            first_page = ('xpath', "//button[@class='btn-prev pagination-btn']")
            self.click(first_page)
            time.sleep(1)
        elif self.next_page_button() == False:
            time.sleep(1)

    def preview_template(self):
        '''预览模版'''
        use = ('xpath', "//div[@class='quick_use_btn']")
        self.click(use)
        time.sleep(1)

    def assert_text(self, expect, actual):
        '''断言元素与预期是否一致'''
        assert expect == actual

    def assert_in_abnormal(self, expect, actual):
        '''断言：预期结果在实际结果里'''
        assert expect in actual

    def assert_expect_url(self, expect):
        '''断言：存储的预期结果是否与真是结果一致'''
        actual = self.driver.current_url
        self.assert_in_abnormal(expect, actual)

    def element_url(self, expect_url):
        url = expect_url
        return url

    # # 尝试截图装饰器
    # def decorate_screenshot(self):
    #     path = pictrue_path
    #
    #     def tear_screenshot(name):
    #         nonlocal path
    #         new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #         self.driver.get_screenshot_as_file(path + new_time + name + '.png')
    #         return path
    #
    #     return tear_screenshot

    def keyboard_man(self, locator, key):
        '''键盘操作'''
        '''
        Keys.ENTER：回车键（Enter）
        Keys.SHIFT：大小写转换键（Shift）
        Keys.CONTROL：Control键（Ctrl）
        Keys.ALT：ALT键（Alt）
        Keys.ESCAPE：返回键（Esc）
        Keys.SPACE：空格键（Space）
        Keys.PAGE_UP：翻页键上（Page Up）
        Keys.PAGE_DOWN：翻页键下（Page Down）
        Keys.END：行尾键（End）
        Keys.HOME：行首键（Home）
        Keys.LEFT：方向键左（Left）
        Keys.UP：方向键上（Up）
        Keys.RIGHT：方向键右（Right）
        Keys.DOWN：方向键下（Down）
        Keys.INSERT：插入键（Insert）
        '''
        time.sleep(1)
        self.driver.find_element(*locator).send_keys(eval(key))  # 传一个字符串，eval()函数会把字符串两边的"去掉

    def retention_window(self):
        """放弃挽留弹窗"""
        try:
            abandon = ("xpath", "//div[@class='isj-pay-retaion-close-btn']")
            self.click(abandon)
        except Exception as e:
            self.logger.info("没有出现挽留弹窗")