# 专题推荐更多页面
class SpecialmoreElement:
    zt_first_pic_xpath = ('xpath',"//div[@id='coryright-image-list']/div[1]")
    pic_coll_alt = ('xpath', "//div[@id='coryright-image-list']/div[1]//img[@alt='']") # 获取属性
    pic_coll_btn = ('xpath', "//div[@id='coryright-image-list']/div[1]/div//img") # 收藏按钮
    yangtu_element_attr = ('xpath',"//div[@id='coryright-image-list']/div[1]/a/img")
    xs_download_btn = ('xpath',"//div[@id='coryright-image-list']/div[1]//div[1]/div[2]") # 相似图片按钮
    pic_list_xpath = ('xpath',"//div[@class='search-list autoscroll-box']/div[2]/div[1]/div") # 图片列表
    zt_download_btn = ('xpath',"//div[@id='coryright-image-list']/div[1]//div[contains(text(),'样图下载')]") # 样图下载