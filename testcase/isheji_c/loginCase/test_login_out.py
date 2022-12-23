from pages.isheji_c.loginPage.exit_load import Exit_Load

class TestExit:
    def test_exit(self, driver):
        """验证退出功能"""
        Exit_Load(driver).exit_action()
