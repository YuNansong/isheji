微梦传媒：爱设计
UI自动化框架（在完善）

common:
action.py文件内存放封装好的 动作方法，如：点击等操作；新的操作页面可直接继承Action，不用实例化对象就可以直接self调用。后续如果需要封装页面动作，封装至侧文件
basepage.oy文件是个demo。

config：
get_yaml.py是封装读取yaml文件的方法。
path.py是事先编写文件路径的。有些文件需要路径，则需要事先编写路径
username.yaml中存放信息，如url,username,password，一个用户对应一条或几条数据，格式为 --> xxx: xxxx(注：冒号后必须有空格,格式要求)

drivers:
放置webdriver驱动的包，只需要Copy Path chromedriver的路径，paste到conftest.py文件中的driver_path变量就可以调用。

pages:
存放登陆动作的包，类变量调取的是yaml文件的数据，login方法是登陆的动作。
下边的go_to方法返回的是类本身，可以在test_login.py文件中直接LoginPafe(driver).go_to().login()运行登陆。

reperts:
每用run.py运行框架，都会在reperts包内生成一个由时间戳命名的html文件，可以查看测试报告。

tests:
存放每个页面的动作，将一个页面作为一个类调用就是po模式的本质(page object)。
每个流程可放在一个py文件中，在test_login文件调取直接运行。

conftest.py:
pytest框架的特性，将调用浏览器的动作封装在driver方法内，yield可理解为unittest框架中的setupclass,teardownclass等前置后置。
run.py：
运行页面，可直接运行，生成的html报告一些信息可以在文件中pytest.main后修改。
test_login.py:
控制页，可以在登陆下方添加想要运行的动作。

需要下载的第三方库：
jinja2
pyyaml
pytest
pytest -testreport
selenium（有些自带）
DingtalkChatbot
openpyxl
lxml
bs4