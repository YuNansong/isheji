import time
from common.path import png
import pyperclip
from pykeyboard import PyKeyboard
from pymouse import PyMouse


def upload_file_mac():
    k = PyKeyboard()
    m = PyMouse()
    time.sleep(2)
    filepathheard = '/'
    time.sleep(2)
    k.press_keys(['Command', 'Shift', 'G'])
    time.sleep(2)
    x_dim, y_dim = m.screen_size()
    time.sleep(2)
    m.click(x_dim // 2, y_dim // 2, 1)
    time.sleep(2)
    # 复制文件路径开头的斜杠/
    pyperclip.copy(filepathheard)
    time.sleep(2)
    # 粘贴斜杠/
    k.press_keys(['Command', 'V'])
    time.sleep(2)
    # 拼接完整路径
    fi = png
    # 输入文件全路径进去
    k.type_string(fi)
    k.press_key('Return')
    time.sleep(2)
    k.press_key('Return')
    time.sleep(2)
