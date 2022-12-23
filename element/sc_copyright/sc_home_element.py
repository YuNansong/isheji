class SCHomePageElement:
    # 登录&退出登录

    loginBtn_element = ('xpath', "//div[@class='login-btn r']")  # 首页的登录按钮
    loginOut_element = ('xpath', "//span[contains(text(),'退出登录')]")  # 退出登录菜单
    head_img = ('xpath', "//div[@class='login-info r']")  # 头像

    # 热门推荐
    first_pic = ('xpath', "//div[@class='hot-recom']/ul/li[1]/a")
    first_pic_num_xpath = ('xpath', "//div[@class='hot-recom']/ul/li[1]/a//p")
    pic_list_xpath = ('xpath', "//div[@id='coryright-image-list']/div")

    # 视频素材
    first_video_xpath = ('xpath', "//div[@id='video']/div[2]/ul/li[1]/div")
    video_name_xpath = ('xpath', "//div[@class='right']/div[1]//h1[@class='h1']")
    video_id_xpath = ('xpath', "//div[@class='right']/div[1]//ul[@class='ul-box']/li[1]/span[2]")
    close_xpath = ('xpath', "//button[@aria-label='Close']")
    coll_btn_xpath = ('xpath', "//div[@id='video']/div[2]/ul/li[1]/div//img")  # 视频收藏按钮

    # 图片素材
    first_img_xpath = ('xpath', "//div[@id='img']/div[2]/ul/li[1]/div")
    img_name_xpath = ('xpath', "//div[@class='img-detail']/div[2]//h1[@class='h1']")
    img_id_xpath = ('xpath', "//div[@class='img-detail']//ul[@class='info']/li[1]/span[1]")
    down_load_yangtu_xpath = ('xpath', "//div[@id='img']/div[2]/ul/li[1]/div/div/div[1]")
    # 平面模板
    first_temp_xpath = ('xpath', "//div[@id='plane']/div[2]/ul/li[1]/div")
    temp_name_xpath = ('xpath', "//div[@class='right']/div[1]//h1[@class='h1']")
    temp_id_xpath = ('xpath', "//div[@class='music-detail']//ul[@class='ul-box']/li[1]/span[2]")

    # PPT模板
    first_ppt_xpath = ('xpath', "//div[@id='ppt']/div[2]/ul/li[1]/div")
    ppt_name_xpath = ('xpath', "//div[@class='img-detail']/div[2]//h1[@class='h1']")
    ppt_id_xpath = ('xpath', "//div[@class='img-detail']/div[2]//ul[@class='info']/li[1]/span")

    # 免抠元素
    first_exempt_xpath = ('xpath', "//div[@id='exempt']/div[2]/ul/li[1]/div")
    exempt_name_xpath = ('xpath', "//div[@class='img-detail']/div[2]//h1[@class='h1']")
    exempt_id_xpath = ('xpath', "//div[@class='img-detail']/div[2]//ul[@class='info']/li[1]/span")

    # 专题推荐
    hot_pic_class_element = ('xpath', "//div[@class='temp-zt']/div/div/div")  # 热门图集分类
    zt_more_btn_element = ('xpath', "//div[@class='recommend']")  # 专题推荐--查看更多
    pic_download_btn = ('xpath',
                        "//div[@class='temp-zt-box']//div[@class='img-material']/ul/li[2]//div[@class='cardiconbox iconbox-down']")  # 下载样图
    zt = ('xpath', "//div[@class='temp-zt']/div/div/div[1]//p")

    apply_title_element = ('xpath', "//div[@class='downdemo-inner']/div[1]")  # 下载成功
    closed_alert = ('xpath', "//div[@class='banquan-close']")  # 关闭弹框
    # 收藏图片
    coll_folder = ('xpath', "//ul[@class='collect-list']/li[1]")  # 在点击收藏弹窗的提示框，选择收藏夹
    pic_coll_btn = ('xpath', "//div[@id='coryright-image-list']/div[2]/div/div[3]/img")  # 判断是否已收藏，固定收藏第2张图片

    sure_btn_element = ('xpath', "//div[@class='active']")  # 弹框的确定按钮
    succ_tips_element = ('xpath', "//div[@class='el-message el-message--success']")  # 收藏成功提示

    # 相似图片
    similar_pic_btn = ('xpath', "//div[@id='img']/div[2]/ul/li[1]/div/div[1]/div[2]/span")  # 相似图片按钮

    # 搜索
    search_input_element = ('xpath', "//div[@class='hc-search home-border']//input")  # 搜索输入框
    search_btn_element = ('xpath', "//div[@class='search img l imgT']")  # 搜索按钮
    search_result_element = ('xpath', "//div[@class='search-title']/span")  # 搜索结果页的搜索关键字
