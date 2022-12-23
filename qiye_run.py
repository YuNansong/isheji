from common.sendEmail import SendMail
import pytest

if __name__ == '__main__':
    date_str = '爱设计企业端执行用例结果'
    pytest.main([f'--report={date_str}.html',
                 '--title=爱设计企业端自动化测试结果',
                 '--tester=左艺轩',
                 '--desc=如有未通过用例，可查看详细信息：查看详情',
                 '-s',
                 './testcase/ent/test_ent_login.py', # 企业登录页面
                 './testcase/ent/test_my_brand.py',  # 品牌管理
                 './testcase/ent/test_business_member.py',  # 成员管理
                 './testcase/ent/test_data_statistics.py',  # 数据统计
                 './testcase/ent/test_ent_material.py',  # 企业素材
                 './testcase/ent/test_ent_temp.py',  # 企业模板
                 './testcase/ent/test_ent_newdesign.py',  # 新建设计
                 './testcase/ent/test_ent_mydesign.py', # 我的设计
                 './testcase/ent/test_ent_mycoll.py', # 我的收藏
                 './testcase/ent/test_homepage_manage.py',  # 企业：首页管理
                 './testcase/ent/test_ent_copyright.py', # 版权图片
                 './testcase/ent/test_temp_center.py', # 模板中心
                 './testcase/ent/test_temp_preview.py', # 模板预览页面
                 './testcase/ent/test_workbench.py', # 工作台
                 './testcase/ent/test_ent_home.py' # 企业ConTech页面
                 ])
    mail = SendMail()
    mail.sendmail()