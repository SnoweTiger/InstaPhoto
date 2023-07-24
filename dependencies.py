import requests, json, time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

with open("login.json") as f:
    USER = json.loads(f.read())

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("test-type")
chrome_prefs = {}
chrome_options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_options.add_argument("--disable-gpu")


async def get_images_selenium_inst(username: str, max_count: int):
    URL = "http://www.instagram.com/"
    IMAGE_CLASS_NAME = "_ac7v _al3n"

    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(5)
        driver.get(URL)
        images = []
        username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
        password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        username_input.send_keys(USER["username"])
        password_input.send_keys(USER["password"])
        password_input.submit()
        # TODO: check why implicitly doesn't work correctly. Make explicitly way
        time.sleep(5)

        driver.get(URL + "/" + username)
        # TODO: check why implicitly doesn't work correctly. Make explicitly way
        time.sleep(5)

        images = parse_images(driver.page_source, IMAGE_CLASS_NAME, max_count)
    except Exception:
        images = {"error": "Selenium error"}
    finally:
        driver.close()

    return images


async def get_images_selenium_side(username: str, max_count: int | None = None):
    URL = "https://imgsed.com"
    IMAGE_CLASS_NAME = "item"

    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(URL + "/" + username)
        images = parse_images(driver.page_source, IMAGE_CLASS_NAME, max_count)
    except Exception:
        images = {"error": "Selenium error"}
    finally:
        driver.close()

    return images


async def get_images_bs_side(username: str, max_count: int | None = None):
    URL = "https://imgsed.com"
    IMAGE_CLASS_NAME = "items"

    r = requests.get(f"{URL}/{username}/")
    images = parse_images(r.content, IMAGE_CLASS_NAME, max_count)

    return images


def parse_images(content, class_name: str, max_count: int | None = None):
    soup = bs(content, "html.parser")

    try:
        images_div = soup.find("div", {"class": class_name})
        if max_count:
            images_img = images_div.find_all("img", limit=max_count)
        else:
            images_img = images_div.find_all("img")
        images = [
            image["data-src"] if image.get("data-src") else image["src"]
            for image in images_img
        ]
    except Exception:
        images = {"error": "Parsers error"}

    return images
