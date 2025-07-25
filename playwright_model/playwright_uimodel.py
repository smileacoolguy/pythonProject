## playwright_model execution
import time, re
from playwright.sync_api import sync_playwright,Page, expect
#from pytest_html_reporter import attach


def test_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True to run without UI
        page = browser.new_page()
        page.goto("https://example.com")
        time.sleep(3)
        print(page.title())
        expect(page).to_have_url(re.compile(".*example.com"))
        #attach(data=browser.get_screenshot_as_png())
        browser.close()
