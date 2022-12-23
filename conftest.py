import time
import platform
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from common.getYaml import url
from common.sendDingTalk import SendDingTalk
from common.readLog import Log
from common.path import drivers_path
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

log = Log(__name__)
logger = log.getLog()

@pytest.fixture(scope='session', autouse=True)
def driver():
    # desired_capabilities = DesiredCapabilities.CHROME
    # desired_capabilities["pageLoadStrategy"] = "none"
    urlInfo = url['url']['testUrl']
    # 指定chromedriver 路径
    driver = ""
    driver_path = ""
    try:
        osName = platform.system()
        if osName == "Windows":
            driver_path = Service(drivers_path+"\\"+"chromedriverw.exe")
            driver = webdriver.Chrome(service=driver_path)
        elif osName == "Darwin":
            driver_path = Service(r'/Users/zuoyixuan/Desktop/code/git/365sheji-autotest/drivers/chromedriver')
            driver = webdriver.Chrome(service=driver_path)
        else:
            logger.error("获取操作系统错误")
        driver.get(urlInfo)  # 启动浏览器
        driver.maximize_window()  # 最大化
        driver.implicitly_wait(4)  # 隐性等待
        yield driver
        time.sleep(2)
    except Exception as e:
        logger.error("启动谷歌浏览器失败，请查看原因 %s"%repr(e))
        SendDingTalk().sendDingTalkMsg("启动谷歌浏览器失败，请查看原因")