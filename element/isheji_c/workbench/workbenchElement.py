class WorkBenchElement:
    sucai_btn_element = ('xpath',"//div[@class='editor-aside-navbar-list']//div[@class='editor-aside-navbar-list-item'][2]/div[2]")  # 工作台素材按钮
    save_btn_element = ('xpath',"//div[@class='save-box']//div//div[@class='icon']//*[local-name()='svg']")   # 工作台保存按钮
    downloadBtn_element =('xpath', "//div[@class='editor-header-plane__download']")   # 工作台右上角的下载按钮
    downloadBtn_element_other = ("xpath", "//div[@class='editor-header-plane__single']")
    download_btn_dialog_element = ('xpath',"//div[@class='download-btn-dialog']")   # 在工作台点击右上角的下载后弹窗浮层的下载按钮
    download_ast_element =('xpath', "//div[@class='title']")   # 在工作台下载图片成功
    jump_btn_element = ('xpath',"//div[@class='guidance-footer']/div[@class='jump']")   # 进工作台跳过引导按钮
    one_jump = ("xparth", "//div[@id='driver-popover-item']//span") #工作台第一个下一步
    two_jump = ("xpath", "//div[@id='driver-popover-item']//span") #工作台第二个下一步
    three_jump = ("xpath", "//div[@id='driver-popover-item']//span") # 工作台第三个下一步
    four_jump = ("xpath", "//div[@id='driver-popover-item']//span/button[@class='driver-next-btn']") # 工作台第四个下一步
    experience_now = ("xpath", "//div[@class='ant-modal-body']/button/span")#立即体验




    watermark_element = ('xpath', "//div[@class='editor-watermask']") # 水印
    risk_button_element = ('xpath', "//div[@class='editor-header-copyright-risk']")  # 风险提示
    upvip_button_element = ('xpath', "//div[@class='editor-header-vip-btn']")  # 开通VIP(悬浮）
    open_VIP_button = ("xpath", "//a[@class='isj-vip-content-button']")  # 开通VIP按钮
    download_pay_button = ('xpath', "//button[@class='ant-btn ant-btn-primary editor-download__vip']//span") # 下载（升级会员）

    template_element = ('xpath', "//div[@class='editor-aside-navbar-list']//div[@class='editor-aside-navbar-list-item'][1]") # 工作台左侧模板Btn



    my_button = ("xpath", "//div[@class='editor-aside-navbar-list']//div[@class='editor-aside-navbar-list-item'][6]")#工作台左侧，我的 按钮

    my_collection = ("xpath", "//div[@class='ant-tabs-nav-wrap']/div/div[2]/div")#我的按钮中的我的收藏
    material_collection = ("xpath", "//div[@class='vue-waterfall']/div") #我的按钮-我的收藏-素材（所有）
    my_collection_template = ("xpath", "//div[@class='editor-collect-tab']//div[@class='ant-tabs-nav-list']/div[@class='ant-tabs-tab']/div")#我的-我的收藏-模板
    template_set = ("xpath", "//div[@id='rc-tabs-15-panel-TEMPLATE']//div[@class='vue-waterfall-slot']")#我的-收藏-模板（所有）




    my_collection_tab_element = ('xpath', "//li[@class='tab-item hide']//li[@class='normal']") # 模板--我的收藏
    no_template_element =('xpath', "//section[@class='template-wrap']/ul[@class='no-template']/li/img") #模板--我的收藏 空的图片
    empty_tips_element = ('xpath', "//section[@class='template-wrap']/ul[@class='no-template']/li[2]/p") #模板--我的收藏 空的提示
    my_collection_temp_list_element = ('xpath', "//section[@class='template-wrap']/ul/li") #模板--我的收藏列表模板个数

    template_path_element = ('xpath', "//div[@id='content-wrap']/div[1]/div[2]/div[3]/div[1]/div[1]") # 工作台中间的模板

    sucaiMenu_element = ('xpath', "//span[@class='iconfont icon-sucai']") # 工作台左侧素材Btn
    hot_sucai_list_element = ('xpath',"//li[@tab_item='material']/section/div") # 素材list
    shape_element = ('xpath',"//li[@tab_item='material']/section/div[1]/div[1]/p[2]") # 素材list--形状
    coll_sucai_tab_element = ('xpath',"//li[@type='material_collect']") # 素材收藏tab
    no_sucai_element = ('xpath',"//section[@class='material-wrap']/ul[@class='no-template']/li/img") #素材--素材收藏 空的图片
    empty_sucai_tips_element = ('xpath',"//section[@class='material-wrap']/ul[@class='no-template']/li[2]/p") #素材--素材收藏 空的提示
    sucai_list_element = ('xpath',"//li[@tab_item='material']/section/ul[@type='material']/li") #素材--素材收藏列表模板个数
    temp_div_num_element = ('xpath',"//div[@class='i-design-canvas']//div") # 获取素材div个数
    hot_sucai_tab_element = ('xpath',"//li[@type='material_list']") # 热门素材tab
    sucai_element = ('xpath',"//li[@tab_item='material']/section/div[2]/div[2]/div[1]") # 在热门素材列表，点击某个素材
    sucai_class_element = ('xpath',"//li[@tab_item='material']/section/div[2]/div[1]/p[2]") # 在热门素材列表，点击某个素材分类的查看全部
    sucai_class_name_element = ('xpath',"//div[@class='material-wrap-type']/p") # 在热门素材列表，点击某个素材分类的查看全部,列表的title
    # 文字
    words_button_element = ('xpath', "//span[@class='iconfont icon-wenzi']") # 工作台左侧文字按钮
    words_title_element = ('xpath', "//button[@name='思源黑体-粗体']") # 文字列表，点击添加标题

    # 背景
    baclground_button_element = ('xpath', "//span[@class='iconfont icon-beijing']") # 工作台左侧背景按钮
    back_ass_element = ('xpath', "//ul[@id='tab-item-list']/li[@tab_item='background']/h6") # 背景列表的标题
    background_picture_num = ('xpath', "//div[@class='bg-imagelist-wrap']/div[1]/li") # 获取到总背景图个数
    background_picture_element = ('xpath', "//div[@class='bg-imagelist-wrap']/div[1]/li[4]/img") # 使用第4个背景图
    background_div_element = ('xpath',"//div[@class='inner-content']/div[last()]/div/img") # 在工作台查看背景是否为background_picture_element

    # 便捷
    convenient_button = ('xpath', "//nav[@id='tabList']//img") # 左侧便捷按钮
    input_button = ('xpath', "//input[@id='upload-qrcode-img']") # 上传图片按钮
    pic_element = ('xpath',"//ul[@id='qrcode-list-ul']/li") # 列表图片list
    pic_move_element = "//ul[@id='qrcode-list-ul']/li[1]" #列表第一个图片
    more_btn_element = ('xpath',"//ul[@id='qrcode-list-ul']/li[1]/div[@class='more']/span") # 图片的更多按钮
    del_btn_element = ('xpath',"//ul[@id='qrcode-list-ul']/li[1]//div[@class='delQrcode']") # 图片的删除按钮
    create_qrcode_element = ('xpath',"//div[@id='create-qrcode']") # 生成二维码
    input_qrcode_url_element = ('xpath',"//input[@id='qrcode-url-input']") # 输入url文本框
    qrcode_color_btn = ('xpath',"//button[@class='qrcode_color qrcode-btn']") # 选择颜色
    qrcode_color= ('xpath',"//div[@class='text-color-select qrcode-color-select']/ul[2]/li[6]") # 颜色面板 选择第1个
    create_qrcode_btn = ('xpath',"//button[@type='qrcode']") # 确认生成二维码
    # 上传模块
    upload_button_element = ('xpath', "//span[@class='iconfont icon-shangchuan']") # 左侧上传按钮
    up_pic_element = ('xpath',"//ul[@class='finished-upload-list']//li") # 列表中的图片
    realy_input_button = ('xpath', "//input[@id='upload-design-img']") # 上传模块
    first_picture = "//ul[@class='finished-upload-list']/div[1]/li[1]" # 上传模块的第一张图片
    delete_button = ('xpath', "//ul[@class='finished-upload-list']/div[1]/li[1]/div/span") # 删除图片按钮
    used_num_element =('xpath',  "//span[@class='used_num']") # 已使用大小
    user_total_upload_size_element =('xpath',  "//span[@class='user_total_upload_size']") #总大小 有可能是G为单位，有可能是M单位
    # 获取首页元素
    temp_element = ('xpath', "//div[@class='swiper-slide card swiper-slide159 swiper-slide-active']//div[@class='jbalert-box']")
    eleList = ('xpath', "//div[@id='apptc']/div[@class='vertical'][2]/div[2]/div[1]/div[1]/div")  # 首页改版后-专题定位
    right_button = ('xpath', "//div[@id='apptc']/div[@class='vertical'][2]/div[2]/div[2]") # 右滑功能

    # 进入企业模版
    qiye_temp_element = ('xpath', "//div[@class='content-container']/div[1]/div[1]/div[1]")

    # 右侧
    workbench_temp_size_xpath = ("xpath","//div[@class='size-view']/div[2]/span[1]")