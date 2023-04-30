from selenium.webdriver import Chrome, ChromeOptions, Firefox
from selenium.webdriver.chrome.service import Service as chrome_service
from selenium.webdriver.firefox.service import Service as firefox_service

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

__CHROME = 1
__FIRE_FOX = 2


def driver_factory(driver_id: int):
    if int(driver_id) == __CHROME:
        options = ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--disable-site-isolation-trials")
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--allow-insecure-localhost")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")
        options.add_argument("--window-size=1440, 900")
        return Chrome(chrome_options=options, service=chrome_service(ChromeDriverManager().install()))
    elif int(driver_id) == __FIRE_FOX:
        return Firefox(service=firefox_service(GeckoDriverManager().install()))
    else:
        return Chrome(service=chrome_service(ChromeDriverManager().install()))
