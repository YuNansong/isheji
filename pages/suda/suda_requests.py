# -*- coding: utf-8 -*-
from common.sendDingTalk import SendDingTalk
from config.suda_url import suda_url
from common.path import suda_path
from pages.suda.expect import *
from common.readLog import Log
from pages.suda.suda_login import sign
import requests
import time

'''v271苏打接口文档'''


class SudaApi():
    log = Log(__name__)
    logger = log.getLog()

    # 图片搜索
    def picture_find(self):
        url = suda_url + '/api/suda/iframe/photo/search'
        head = {
            "Content-Type": "application/json",
            "Authorization": "Bearer dSVDzqeIrw9prDjPqMQoqL0JewQfR2diMCd24LQ8",
            "api-key": "61b87025c1e51"
        }
        body = {
            "page": 1,
            "pagesize": 10,
            "keyword": "领取",
            "sign": sign
        }
        res = requests.request(method='get', url=url, headers=head, params=body)
        response = res.json()
        try:
            assert response['message'] == expect_picture_find['message']
        except AssertionError as err:
            self.logger.error(f'苏打接口报错：图片搜索请求失败:{url}%s' % repr(err))
            SendDingTalk().sendDingTalkMsg(f"苏打接口报错：图片搜索请求失败:{url}")
            raise err

    def Visual_pictures_800px_resources(self):
        # 视觉图片800px资源
        url = suda_url + '/api/suda/iframe/photo/detail'
        head = {
            "Content-Type": "application/json",
            "Authorization": "Bearer dSVDzqeIrw9prDjPqMQoqL0JewQfR2diMCd24LQ8",
            "api-key": "61b87025c1e51"
        }
        body = {
            "pic_id": "VCG41N1361360323",
            "sign": sign
        }
        res = requests.request(method='get', url=url, headers=head, params=body)
        response = res.json()
        try:
            assert response == expect_Visual_pictures_800px_resources
        except AssertionError as err:
            self.logger.error(f'苏打接口报错：视觉图片800px资源:{url}%s' % repr(err))
            SendDingTalk().sendDingTalkMsg(f"苏打接口报错：视觉图片800px资源:{url}\n")
            raise err

    def get_system_template_information(self):
        # 获取系统模板信息
        url = suda_url + "/api/suda/iframe/template/info"
        head = {
            "Content-Type": "application/json",
            "Authorization": "Bearer dSVDzqeIrw9prDjPqMQoqL0JewQfR2diMCd24LQ8",
            "api-key": "61b87025c1e51"
        }
        body = {
            "template_id": 36954,
            "sign": sign
        }
        res = requests.request(method='get', url=url, headers=head, params=body)
        response = res.json()
        try:
            assert response['message'] == expect_get_system_template_information['message']
        except AssertionError as err:
            self.logger.error(f'苏打接口报错：获取系统模板信息:{url}%s' % repr(err))
            SendDingTalk().sendDingTalkMsg(f"苏打接口报错：获取系统模板信息:{url}")
            raise err

    def get_user_design_information(self):
        # 获取用户设计信息（现有设计进入）
        url = suda_url + "/api/suda/iframe/design/info"
        head = {
            "Content-Type": "application/json",
            "Authorization": "Bearer dSVDzqeIrw9prDjPqMQoqL0JewQfR2diMCd24LQ8",
            "api-key": "61b87025c1e51"
        }
        body = {
            "design_id": 16,
            "sign": sign
        }
        res = requests.request(method='get', url=url, headers=head, params=body)
        response = res.json()
        try:
            assert response['message'] == expect_get_system_template_information['message']
        except AssertionError as err:
            self.logger.error(f'苏打接口报错：获取用户设计信息（现有设计进入）:{url}%s' % repr(err))
            SendDingTalk().sendDingTalkMsg(f"苏打接口报错：获取用户设计信息（现有设计进入）:{url}")
            raise err

    def save_design_for_team_users(self):
        # 团队用户保存设计====================================请求数据太长
        url = suda_url + "/api/suda/iframe/design/save"
        head = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Bearer dSVDzqeIrw9prDjPqMQoqL0JewQfR2diMCd24LQ8",
            "api-key": "61b87025c1e51"
        }
        with open(suda_path, mode='rt', encoding='utf-8') as file:
            canvas_info_valuies = file.read()
        body = {
            "action": "save",
            "dir_id": 0,
            "name": "自动化设计名称",
            "cover_url": "//file.isheji.com/isheji/3270/654188/2021122716261361c978a505222414084.png",
            "type": 9,
            "size": "900x500",
            "width": 900,
            "height": 500,
            "template_id": 36954,
            "design_id": 16,
            "canvas_info": str(canvas_info_valuies),
            "sign": sign
        }
        res = requests.request(method='post', url=url, headers=head, data=body)
        response = res.json()
        try:
            assert response['message'] == expect_save_design_for_team_users['message']
        except AssertionError as err:
            self.logger.error(f'苏打接口报错：团队用户保存设计:{url}%s' % repr(err))
            SendDingTalk().sendDingTalkMsg(f"苏打接口报错：团队用户保存设计:{url}")
            raise err

    def team_user_download_design(self):
        # 团队用户下载设计
        url = suda_url + '/api/suda/iframe/design/download'
        head = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Bearer dSVDzqeIrw9prDjPqMQoqL0JewQfR2diMCd24LQ8",
            "api-key": "61b87025c1e51"
        }
        with open(suda_path, mode='rt', encoding='utf-8') as file:
            canvas_info_valuies = file.read()
        body = {
            "design_id": 16,
            "width": 900,
            "height": 500,
            "canvas_info": str(canvas_info_valuies),
            "suffix": "png",
            "enlarge": 1,
            "sign": sign
        }
        res = requests.request(method='post', url=url, headers=head, data=body)
        response = res.json()
        time.sleep(10)
        download_key = response['data']['key']
        try:
            assert response['message'] == expect_team_user_download_design['message']
        except AssertionError as err:
            self.logger.error(f'苏打接口报错：团队用户下载设计:{url}%s' % repr(err))
            SendDingTalk().sendDingTalkMsg(f"苏打接口报错：团队用户下载设计:{url}")
            raise err
        return download_key

    def detect_image_generation(self):
        # 检测图片生成（下载轮循）
        url = suda_url + "/api/suda/iframe/design/download_check"
        head = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Bearer dSVDzqeIrw9prDjPqMQoqL0JewQfR2diMCd24LQ8",
            "api-key": "61b87025c1e51"
        }
        body = {
            "key": self.team_user_download_design(),
            "sign": sign
        }
        res = requests.request(method='get', url=url, headers=head, params=body)
        response = res.json()
        print(response)
        try:
            assert response['status'] == expect_detect_image_generation['status']
        except AssertionError as err:
            self.logger.error(f'苏打接口报错：团队用户保存设计:{url}%s' % repr(err))
            SendDingTalk().sendDingTalkMsg(f"苏打接口报错：团队用户保存设计:{url}")
            raise err


if __name__ == '__main__':
    SudaApi().detect_image_generation()
