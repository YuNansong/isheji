class NewDesignElement:
    custom_xpath = ('xpath',"//div[@class='create-item-header']/div[contains(text(),'自定义尺寸')]") # 自定义尺寸
    input_wide_xpath = ('xpath',"//div[@aria-label='自定义画布尺寸']//input[@placeholder='宽']") # 自定义尺寸--宽
    input_high_xpath = ('xpath',"//div[@aria-label='自定义画布尺寸']//input[@placeholder='高']") # 自定义尺寸--高
    start_design_xpath = ('xpath',"//button/span[contains(text(),'开始设计')]") # 自定义尺寸--高
