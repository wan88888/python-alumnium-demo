import os
from dotenv import load_dotenv

load_dotenv()

from alumnium import Alumni
from selenium.webdriver import Chrome
from pytest import fixture

# 从环境变量读取配置
SAUCEDEMO_USERNAME = os.getenv("SAUCEDEMO_USERNAME")
SAUCEDEMO_PASSWORD = os.getenv("SAUCEDEMO_PASSWORD")

@fixture
def driver():
    driver = Chrome()
    yield driver
    driver.quit()

@fixture
def al(driver: Chrome):
    al = Alumni(driver)
    yield al
    al.quit()

def test_login_success(al: Alumni, driver: Chrome):
    driver.get("https://www.saucedemo.com")
    al.do(f"enter username '{SAUCEDEMO_USERNAME}' in the username field")
    al.do(f"enter password '{SAUCEDEMO_PASSWORD}' in the password field")
    al.do("click the login button")
    al.check("page shows inventory or products page")
    al.check("page contains 'Swag Labs' text")