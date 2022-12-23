class EntIndexElement:
    qiye_vip_xpath = ('xpath',"//div[@class='header-right']/div[contains(text(),'企业VIP')]")

    head_img_xpath = ('xpath',"//div[@class='figure']")
    logout_xpath = ('xpath',"//span[contains(text(),'退出登录')]")

    manageMenu_xpath = ('xpath',"//span[contains(text(),'管理') and @aria-haspopup='list']") # 右上角顶部管理菜单
    brandManage_xpath = ('xpath',"//ul[@x-placement='bottom-end']//span[contains(text(),'品牌管理')]") # 右上角顶部品牌管理
    memberManage_xpath = ('xpath',"//ul[@x-placement='bottom-end']//span[contains(text(),'成员管理')]") # 成员管理
    dataStatistice_xpath = ('xpath',"//ul[@x-placement='bottom-end']//span[contains(text(),'数据统计')]") # 数据统计
    entsucai_xpath = ('xpath',"//ul[@x-placement='bottom-end']//span[contains(text(),'企业素材')]") # 企业素材
    enttemp_xpath = ('xpath',"//ul[@x-placement='bottom-end']//span[contains(text(),'企业模板')]") # 企业模板
    banquan_xpath = ('xpath',"//ul[@x-placement='bottom-end']//span[contains(text(),'版权图片')]") # 版权图片
    homemanage_xpath = ('xpath',"//ul[@x-placement='bottom-end']//span[contains(text(),'首页管理')]") # 首页管理
    mydesign_xpath = ('xpath',"//ul[@x-placement='bottom-end']//span[contains(text(),'我的设计')]") # 我的设计
    mycoll_xpath = ('xpath',"//ul[@x-placement='bottom-end']//span[contains(text(),'我的收藏')]") # 我的收藏
    tempCenter_xpath = ('xpath',"//ul[@x-placement='bottom-end']//span[contains(text(),'模板中心')]") # 模板中心
    newdesign_xpath = ('xpath',"//ul[@x-placement='bottom-end']//span[contains(text(),'新建设计')]") # 模板中心

    entVip_xpath = ('xpath',"//div[@class='vip-item']") # 首页导航--企业VIP