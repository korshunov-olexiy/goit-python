from pyppeteer import launch
import asyncio, requests
from urllib.parse import urlparse
from http import HTTPStatus

def check_site_exist(url: str) -> str:
    try:
        url_parts = urlparse(url)
        domain_name = url_parts.netloc
        request = requests.get(url).status_code
        return domain_name if request in [HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY] else ''
    except:
        return ''

async def take_screenshot(url: str) -> str:
    screenshot_name = check_site_exist(url)
    if screenshot_name:
        screenshot_name = f"{screenshot_name}.png"
        browser = await launch()
        page = await browser.newPage()
        await page.goto(url)
        await page.screenshot({'path': screenshot_name})
        await browser.close()
        return screenshot_name

print(asyncio.run(take_screenshot("https://4pda.ru1")))
