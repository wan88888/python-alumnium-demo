import os
from dotenv import load_dotenv

load_dotenv()

from alumnium import Alumni
from appium.options.ios import XCUITestOptions
from appium.webdriver.webdriver import WebDriver
from pytest import fixture

# 从环境变量读取配置
APPIUM_DEVICE_NAME = os.getenv("APPIUM_DEVICE_NAME")
APPIUM_PLATFORM_VERSION = os.getenv("APPIUM_PLATFORM_VERSION")
BUNDLE_ID = "com.apple.Preferences"

@fixture
def driver():
    options = XCUITestOptions()
    options.automation_name = "XCUITest"
    options.bundle_id = BUNDLE_ID
    options.device_name = APPIUM_DEVICE_NAME
    options.no_reset = True
    options.platform_name = "iOS"
    options.platform_version = APPIUM_PLATFORM_VERSION
    driver = WebDriver(options=options)
    yield driver
    
@fixture
def al(driver: WebDriver):
    al = Alumni(driver)
    yield al
    al.quit()

def test_demo(al: Alumni, driver: WebDriver):
    al.do("点击通用")
    al.check("页面包含关于本机")