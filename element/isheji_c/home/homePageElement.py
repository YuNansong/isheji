
class HomePageElement:
    search_element = ('xpath', "//input[@id='template-search']") # 首页搜索输入框
    searchBtn_element =('xpath', "//div[@class='header-search']/div/span[contains(text(),'搜索')]") # 首页搜索按钮
    key_element =('xpath', "//div[@class='keyword']/span") # 搜索结果页，关键字
    nextPageElement =('xpath', "//ul[@class='el-pager']/a") # 用户获取一共多少页，用于循环
    firstPageBtn =('xpath',  "//ul[@class='el-pager']/a[1]")  # 翻页的第一个数字
    lastPageBtn = ('xpath', "//ul[@class='el-pager']/a[last()]")  # 翻页的最后一个数字
    upPageBtn =('xpath',  "//button[@class='btn-prev pagination-btn']")  # 上一页按钮
    nextPageBtn =('xpath', "//button[contains(text(),'下一页')]")  # 下一页按钮
    right_btn_element =('xpath', "//div[@class='swiper-button-next sence-list-next']/span") # 右滑按钮
    temp_class_element = ('xpath' ,"//div[@id='apptc']/div[@class='vertical']") # 首页模板分类，获取总数
    cvip_element =('xpath', "//a[contains(text(),'个人VIP')]") # 导航的个人vip 菜单
    vip_element = "//a[@class='vip header-vip']" # 导航的个人vip 菜单,用于悬浮
    per_vip_element =('xpath', "//ul[@id='menulist']/li[1]") # 导航的个人vip 菜单
    open_vip_btn =('xpath', "//a[@id='personVipButton']") # 导航的个人vip，浮框的开通会员按钮
    detail_element =('xpath', "//a[@class='vipDetail']") # 悬浮到导航的个人VIP菜单点击详细特权
    enterprise_vip = ('xpath', "//a[@id='jumpToCompanyVip']") # 导航的企业VIP菜单
    enterprise_vip_element = "//a[@id='jumpToCompanyVip']" # 导航的企业VIP菜单
    enterprise_vip_flayer_detail = ('xpath',"//div[@class='vip-content vip-company']/div[1]/div[2]/a")
    enterprise_vip_flayer_detailBtn = ('xpath',"//div[@class='vip-content vip-company']/div[1]/a")
    cooperation_element =('xpath', "//a[@class='cooperation']") # 顶部导航的合作菜单
    more_button_element = ('xpath', "//li[@class='menu-more']")
    api_menu_element = ('xpath', "//a[@class='apipage']") # 顶部导航的API菜单
    idea_button_element =('xpath', "//a[@class='idea']") # 顶部导航的创意热店菜单
    copyright_element = ('xpath', "//div[@id='main-content']/div[5]/div") # 左侧导航 企业素材库 ICON
    sucaiku_element =('xpath', "//a[@class='copyrightStation']") # 顶部版权站
    ai_buckle_menu_element = ('xpath',"//li[@class='block-item cutout-index']//span[@class='block-text']") # 左侧导航智能扣图菜单
    editor_menu_element =('xpath', "//li[@class='block-item ']/a[@class='identical']/span[2]") # 左侧导航365编辑器菜单

    # 登录&退出登录
    loginBtn_element =('xpath', "//div[@class='login-button']/div[1]") # 首页的登录按钮
    # vip弹框
    alert_element = ('xpath', "//p[@class='tishi']/span[1]")
    x_buttonA_element = ('xpath',  "//div[@class='img-box bz']/span[1]") # vip弹框不再提醒选项1
    x_buttonB_element =('xpath',  "//div[@class='img-box kait']/span") # vip弹框不再提醒选项2
    x_buttonC_element = ('xpath', "//div[@class='img-box peizhi']/span") # vip弹框不再提醒选项3
    x_buttonD_element =('xpath',  "//div[@class='img-box lz']/span") # vip弹框不再提醒选项4

    # 模板分类
    elementText_element = ('xpath', "//div[@id='sence-list-box']/div[1]/div[1]/div[1]/a/div[1]/h6") # 模板分类--开始作图
    new_media_element = ('xpath', "//section[@class='create-a-design']/section/div[1]/h3[1]") # design 页面的新媒体配图

