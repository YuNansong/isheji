from common.sendEmail import SendMail
import pytest
'''运行线上之前跟郝政说一下'''
if __name__ == '__main__':
    date_str = '爱设计执行用例结果'
    pytest.main([f'--report={date_str}.html',
                 '--title=爱设计C端-PC端自动化测试结果',
                 '--tester=测试组',
                 '--desc=如有未通过用例，可查看详细信息：查看详情',
                 '-s',
                 './testcase/isheji_c/homeCase/test_not_logged_in.py',  # 未登录调取登录弹窗
                 './testcase/isheji_c/loginCase/test_login.py',
                 './testcase/isheji_c/homeCase/test_user_core.py',  # 个人中心#1
                 './testcase/isheji_c/homeCase/test_notice.py',  # 消息通知#1
                 './testcase/isheji_c/tempCenterCase/test_temp_special.py',  # 热门精选1
                 './testcase/isheji_c/tempCenterCase/test_temp_preview.py',  # 模版预览 # 企业的预览#1
                 './testcase/isheji_c/homeCase/test_subscribe_account.py',  # 保存模版至公众号1
                 './testcase/isheji_c/homeCase/test_home_page.py',  # 首页操作1
                 './testcase/isheji_c/creativeMallCase/test_creative_mall.py',  # 创意热店1
                 './testcase/isheji_c/homeCase/test_cooperation.py',  # 服务商招募2
                 './testcase/isheji_c/homeCase/test_new_media_page.py',  # 新媒体落地页1
                 # #'./testcase/isheji_c/homeCase/test_poster_home.py',  # 海报落地页
                 './testcase/isheji_c/vipCase/test_personal_vip.py',  # 个人会员1
                 './testcase/isheji_c/tempCenterCase/test_temp_center.py',  # 模版中心1
                 # #'./testcase/isheji_c/homeCase/test_ai_matting.py',  # 智能抠图
                 './testcase/isheji_c/homeCase/test_left_search.py',  # 左上角搜索1
                 # './testcase/isheji_c/homeCase/test_my_design.py',  # 我的设计
                 # './testcase/isheji_c/tempCenterCase/test_picture_designer.py',  # 设计师：图片创作  # 上传文件
                 # # './testcase/isheji_c/tempCenterCase/test_video_creation.py',  # 设计师：视频创作#已下架
                 # './testcase/isheji_c/tempCenterCase/test_workbench.py',  # 工作台：左侧按钮 # 编辑器

                 # './testcase/isheji_c/vipCase/test_long_vip.py',  # 验证VIP（账号为终身VIP）
                 #
                 './testcase/isheji_c/tempCenterCase/test_workbench_ordinary.py',  # 普通账号验证模版付费项
                 './testcase/isheji_c/homeCase/test_right_nav.py',  # 右侧导航
                 ])
    mail = SendMail()
    mail.sendmail()