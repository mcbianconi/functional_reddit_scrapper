
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FF_Options

from robot.config import IMG_HEIGHT, IMG_WIDTH


def driver():
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument(
    #     f"--window-size={IMG_WIDTH}x{IMG_HEIGHT}")  # Full HD 1080p
    # prefs = {'disk-cache-size': 4096}
    # chrome_options.add_experimental_option('prefs', prefs)
    # chrome_driver = os.path.join(
    #     os.getcwd(),
    #     "bin", "chromedriver")
    # web_driver = webdriver.Chrome(
    #     options=chrome_options,
    #     executable_path=chrome_driver)
    return firefox()


def firefox():
    os.environ['MOZ_HEADLESS_WIDTH'] = str(IMG_WIDTH)
    os.environ['MOZ_HEADLESS_HEIGHT'] = str(IMG_HEIGHT)
    options = FF_Options()
    options.add_argument("--headless")
    options.add_argument(
        f"--window-size={IMG_WIDTH},{IMG_HEIGHT}")  # Full HD 1080p
    options.set_preference("dom.webnotifications.enabled", False)
    options.set_preference("dom.push.enabled", False)

    # Download driver from https://github.com/mozilla/geckodriver/releases/tag/v0.25.0
    executable_path = os.path.join(os.getcwd(), "bin", "geckodriver")
    firefox_driver = webdriver.Firefox(
        options=options, executable_path=executable_path)
    return firefox_driver
