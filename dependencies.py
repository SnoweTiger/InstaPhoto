import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("test-type")
chrome_options.add_argument("--disable-gpu")


async def get_images_side_service(
    username: str, max_count: int, service_url: str = "https://imgsed.com"
):
    r = requests.get(f"{service_url}/{username}/")

    images = parse_images(r.content, max_count)

    return images


async def get_images_selenium_side_service(
    username: str, max_count: int, service_url: str = "https://imgsed.com"
):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(service_url + "/" + username)

    images = parse_images(driver.page_source, max_count)

    driver.close()

    return images


def parse_images(content, max_count: int = 0):
    soup = bs(content, "html.parser")
    images_div = soup.find("div", {"class": "items"})

    if max_count:
        images_img = images_div.find_all("img", limit=max_count)
    else:
        images_img = images_div.find_all("img")
    images = [
        image["data-src"] if image.get("data-src") else image["src"]
        for image in images_img
    ]
    return images
