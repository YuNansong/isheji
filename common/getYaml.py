import os
import yaml

from common.path import data_position
from common.path import config


def read_yaml(file):
    with open(file, encoding='utf-8') as f:
        wenjian = yaml.safe_load(f)
        return wenjian


userinfo = read_yaml(os.path.join(config, 'username.yaml'))
scuserinfo = read_yaml(os.path.join(config, 'scusername.yaml'))
url = read_yaml(os.path.join(config, 'url.yaml'))
button_url = read_yaml(os.path.join(data_position, 'HomeButton.yaml'))
switchInfo = read_yaml(os.path.join(config,'sendDtalk.yaml'))
# print(button_url['url']['公共号首图'])
# print(userinfo)
# print(url)
