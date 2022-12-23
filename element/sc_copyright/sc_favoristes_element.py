
class FavoristesElement:

    coll_folder_element = ('xpath',"//div[@class='dropdown_area']/ul/li[1]/div/span[2]") # 在菜单上点击收藏夹
    folder_element = ('xpath',"//a[@href='/personal']") # 左侧菜单--收藏夹
    order_element = ('xpath',"//a[@href='/personal/order']") # 左侧菜单--订单列表
    empty_tips_element = ('xpath',"//div[@class='default-item nocollect']/p") # 收藏夹为空,获取提示信息
    add_element = ('xpath',"//div[@class='title']/div") # 添加收藏夹
    input_coll_folder_name = ('xpath',"//div[@class='collect-input']/input") # 输入收藏夹名称
    repeat_tips_element = ('xpath',"//div[@class='collect-input']/div") # 获取文件夹为空或者名字重复提示
    new_btn = ('xpath',"//div[@class='collect-btn']/div[1]") # 弹框上的点击新建文件夹
    sure_btn_element_xpath = ('xpath',"//div[contains(text(),'确定')]")
    folder_li_element = ('xpath',"//ul[@class='folder']/li") #收藏夹列表的文件夹个数

    folder_more_element = ('xpath',"//ul[@class='folder']/li[last()]//div[@class='more']") # 收藏夹的更多按钮
    rename_btn_element = ('xpath',"//ul[@class='folder']/li[last()]//div[@class='caozuo']/div[1]") # 收藏夹的重命名
    delete_btn_element = ('xpath',"//ul[@class='folder']/li[last()]//div[@class='caozuo']/div[2]") # 收藏夹的删除
    del_sure_btn_element = ('xpath',"//div[@class='el-message-box__btns']/button[2]")
    folder_name_element = ('xpath',"//ul[@class='folder']/li[last()]/p") # 收藏夹名字

    first_act_folder_element = ('xpath',"//ul[@class='folder']/li[@class='hasbox'][1]")
    first_no_act_folder_element = ('xpath',"//ul[@class='folder']/li[@class=''][1]")
    active_folder_element = ('xpath',"//ul[@class='folder']/li[@class='hasbox']") # 获取有图片的收藏夹个数
    active_folder_num_element = ('xpath',"//ul[@class='folder']/li[@class='hasbox']/span") # 获取收藏夹中的图片个数
    no_active_folder_element = ('xpath',"//ul[@class='folder']/li[@class='']") # 获取无图片的收藏夹个数
    pic_element = ('xpath',"//div[@class='data-scroll']/div/div/a") # 收藏夹中图片
    empty_pic_tips_element = ('xpath',"//div[@class='default-item nocollect']/p") # 收藏夹空的提示
    # 移动按钮
    first_pic = ('xpath',"//div[@class='data-scroll']/div/div[1]")
    move_btn_element = ('xpath',"//div[@class='data-scroll']/div/div[1]/div[2]/div[1]/img") # 移动按钮
    delete_pic_btn_element = ('xpath',"//div[@class='data-scroll']/div/div[1]/div[2]/div[2]/img") # 删除按钮
    first_pic_href_element = ('xpath',"//div[@class='data-scroll']/div/div[1]/a")
    folder_list_element = ('xpath',"//ul[@class='collect-list']/li")
    delete_succ_element = ('xpath',"//p[@class='el-message__content']")

    batch_move_btn = ('xpath',"//div[contains(text(),'移动')]") # 右上角移动按钮
    batch_delete_btn = ('xpath',"//div[contains(text(),'删除')]") # 右上角移动按钮
    last_folder_element = ('xpath',"//ul[@class='folder']/li[last()]") # 最后一个文件夹