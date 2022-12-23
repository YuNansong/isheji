from common.sendEmail import SendMail
import pytest

if __name__ == '__main__':
    date_str = '版权站执行用例结果'
    pytest.main([f'--report={date_str}.html',
                 '--title=爱设计版权站自动化测试报告',
                 '--tester=测试组',
                 '--desc=如有未通过用例，可查看详细信息：查看详情',
                 '-s',

                 './testcase/sc_copyright/test_sc_login.py',  # 登录
                 './testcase/sc_copyright/test_sc_center_team.py',  # 个人中心--团队
                 './testcase/sc_copyright/test_sc_home.py',  # 首页
                 './testcase/sc_copyright/test_sc_specialmore.py',  # 专题推荐--更多页
                 './testcase/sc_copyright/test_sc_pic.py',  # 图片
                 './testcase/sc_copyright/test_sc_music.py',  # 音乐
                 './testcase/sc_copyright/test_sc_design.py',  # 设计
                 './testcase/sc_copyright/test_sc_video.py',  # 视频
                 './testcase/sc_copyright/test_sc_exempt.py',  # 免抠元素
                 './testcase/sc_copyright/test_sc_ppt.py',  # PPT
                 './testcase/sc_copyright/test_sc_pic_favorites.py',  # 收藏夹
                 './testcase/sc_copyright/test_sc_center_per.py',  # 个人中心--个人

                 # 以下测试用例使用135账号测试
                 './testcase/sc_copyright/test_sc_loginOut.py',  # 退出登录切换账号
                 './testcase/sc_copyright/test_sc_vip.py',  # VIP
                 './testcase/sc_copyright/test_sc_pic_per.py',  # 个人身份--图片
                 './testcase/sc_copyright/test_sc_music_per.py',  # 个人身份--音乐
                 './testcase/sc_copyright/test_sc_design_per.py',  # 个人身份--设计
                 './testcase/sc_copyright/test_sc_video_per.py',  # 个人身份--视频
                 './testcase/sc_copyright/test_sc_exempt_per.py',  # 个人身份--免抠元素
                 './testcase/sc_copyright/test_sc_ppt_per.py',  # 个人身份--PPT
                 ])

    mail = SendMail()
    mail.sendmail()
