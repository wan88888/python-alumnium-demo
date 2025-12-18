import os
from dotenv import load_dotenv

# 必须在 import alumnium 之前加载 .env，因为 alumnium 在导入时就读取环境变量
load_dotenv()

from alumnium import Alumni
from playwright.sync_api import Page
from pytest import fixture

# 从环境变量读取配置
SAUCEDEMO_USERNAME = os.getenv("SAUCEDEMO_USERNAME")
SAUCEDEMO_PASSWORD = os.getenv("SAUCEDEMO_PASSWORD")


@fixture
def al(page: Page):
    al = Alumni(page)
    yield al
    al.quit()


def test_login_success(al: Alumni, page: Page):
    page.goto("https://www.saucedemo.com")
    al.do(f"enter username '{SAUCEDEMO_USERNAME}' in the username field")
    al.do(f"enter password '{SAUCEDEMO_PASSWORD}' in the password field")
    al.do("click the login button")
    al.check("page shows inventory or products page")
    al.check("page contains 'Swag Labs' text")
