# -*- conding:utf-8 -*-
import os
import time

# import pyperclip
# from pykeyboard import PyKeyboard
# from pymouse import PyMouse
import win32gui
import win32con
import win32api

root_directory = os.path.dirname(os.path.dirname(__file__))

config = os.path.join(root_directory, 'config')

logs_path = os.path.join(root_directory, 'logs')

screenshot_path = os.path.join(root_directory, 'screenshot')
pictrue_path = os.path.join(screenshot_path, 'test')
# print(pictrue_path)

drivers_path = os.path.join(root_directory,"drivers")

data_position = os.path.join(root_directory, 'data')

suda_path = os.path.join(data_position, 'suda_file.txt')
# print(suda_path)

vcg = os.path.join(data_position, 'testphoto.jpg')

psd = os.path.join(data_position, 'psdtestphoto.psd')

jepg = os.path.join(data_position, 'jepgphoto.jpeg')

png = os.path.join(data_position, 'testpng.png')

heng = os.path.join(data_position, 'hengban.jpeg')

shu = os.path.join(data_position, 'shuban.jpeg')

zip_file = os.path.join(data_position, 'test.zip')

member_file = os.path.join(data_position, 'member.xlsx')

def getTestReport():
    file_path = ""
    reports_position = os.path.join(root_directory, 'reports')
    dirs = os.listdir(reports_position)
    listReport = []
    for file in dirs:
        listReport.append(file)
    if listReport.__len__() > 0:
        file_name = listReport[-2]
        file_path = os.path.join(reports_position, file_name)
    return file_path


def file_upload(src):
    dialog = win32gui.FindWindow('#32770', u'打开')  # 对话框
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, src)  # 往输入框输入绝对地址
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button


# file_path = getTestReport()
# # print(file_path)
#
# def keybd_event(VK_CODE):
#     #VK_CODE = int(VK_CODE)
#     win32api.keybd_event(VK_CODE, 0, 0, 0)
#     win32api.keybd_event(VK_CODE, 0, win32con.KEYEVENTF_KEYUP, 0)
#
#     '''
#     ESC键VK_ESCAPE (27)
#     回车键：VK_RETURN (13)
#     TAB键：VK_TAB (9)
#     Caps Lock键：VK_CAPITAL (20)
#     Shift键：VK_SHIFT (16)
#     Ctrl键：VK_CONTROL (17)
#     Alt键：VK_MENU (18)
#     空格键：VK_SPACE (32)
#     退格键：VK_BACK (8)
#     左徽标键：VK_LWIN (91)
#     右徽标键：VK_RWIN (92)
#     鼠标右键快捷键：VK_APPS (93)
#     Insert键：VK_INSERT (45)
#     Home键：VK_HOME (36)
#     Page Up：VK_PRIOR (33)
#     PageDown：VK_NEXT (34)
#     End键：VK_END (35)
#     Delete键：VK_DELETE (46)
#     方向键(←)：VK_LEFT (37)
#     方向键(↑)：VK_UP (38)
#     方向键(→)：VK_RIGHT (39)
#     方向键(↓)：VK_DOWN (40)
#     F1键：VK_F1 (112)
#     F2键：VK_F2 (113)
#     F3键：VK_F3 (114)
#     F4键：VK_F4 (115)
#     F5键：VK_F5 (116)
#     F6键：VK_F6 (117)
#     F7键：VK_F7 (118)
#     F8键：VK_F8 (119)
#     F9键：VK_F9 (120)
#     F10键：VK_F10 (121)
#     F11键：VK_F11 (122)
#     F12键：VK_F12 (123)
#     Num Lock键：VK_NUMLOCK (144)
#     小键盘0：VK_NUMPAD0 (96)
#     小键盘1：VK_NUMPAD1 (97)
#     小键盘2：VK_NUMPAD2 (98)
#     小键盘3：VK_NUMPAD3 (99)
#     小键盘4：VK_NUMPAD4 (100)
#     小键盘5：VK_NUMPAD5 (101)
#     小键盘6：VK_NUMPAD6 (102)
#     小键盘7：VK_NUMPAD7 (103)
#     小键盘8：VK_NUMPAD8 (104)
#     小键盘9：VK_NUMPAD9 (105)
#     小键盘。：VK_DECIMAL (110)
#     小键盘*：VK_MULTIPLY (106)
#     小键盘+：VK_ADD (107)
#     小键盘-：VK_SUBTRACT (109)
#     小键盘/：VK_DIVIDE (111)
#     Pause Break键：VK_PAUSE (19)
#     Scroll Lock键：VK_SCROLL (145)
#     '''

# def upload_file_mac():
#     k = PyKeyboard()
#     m = PyMouse()
#     time.sleep(2)
#     # filepathheard = '/'
#     time.sleep(2)
#     k.press_keys(['Command', 'Shift', 'G'])
#     time.sleep(2)
#     x_dim, y_dim = m.screen_size()
#     time.sleep(2)
#     m.click(x_dim // 2, y_dim // 2, 1)
#     time.sleep(2)
#     # 复制文件路径开头的斜杠/
#     # pyperclip.copy(filepathheard)
#     time.sleep(2)
#     # 粘贴斜杠/
#     # k.press_keys(['Command', 'V'])
#     time.sleep(2)
#     # 拼接完整路径
#     fi = vcg
#     # 输入文件全路径进去
#     k.type_string(fi)
#     k.press_key('Return')
#     time.sleep(8)
#     k.press_key('Return')
#     time.sleep(2)