"""import pytest
import pytest_html
from selenium import webdriver
from datetime import datetime
import os
import base64

# Fixture to launch and yield driver
@pytest.fixture
def driver():
    url = "https://www.example.com"
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Optional: run in headless mode
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1280, 800)
    driver.get(url)
    yield driver
    driver.quit()

# Hook to embed screenshot in report
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join("screenshots", file_name)
            driver.save_screenshot(file_path)

            # Encode image to base64
            with open(file_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

            # Embed image in report
            extra_image = pytest_html.extras.image(
                encoded_image, mime_type="image/png"
            )
            report.extra = getattr(report, "extra", [])
            # report.extra.append(extra_image)

            html_link = f'<a href="{file_path}" target="_blank">Screenshot</a>'
            report.extra.append(pytest_html.extras.html(html_link))

    elif report.when == "setup" and report.passed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join("screenshots", file_name)
            driver.save_screenshot(file_path)

            # Encode image to base64
            with open(file_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

            # Embed image in report
            extra_image = pytest_html.extras.image(
                encoded_image, mime_type="image/png"
            )
            report.extra = getattr(report, "extra", [])
            # report.extra.append(extra_image)
            html_link = f'<a href="{file_path}" target="_blank">Screenshot</a>'
            report.extra.append(pytest_html.extras.html(html_link))

    if report.when == "call" and report.passed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join("screenshots", file_name)
            driver.save_screenshot(file_path)

            # Encode image to base64
            with open(file_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

            # Embed image in report
            extra_image = pytest_html.extras.image(
                encoded_image, mime_type="image/png"
            )
            report.extra = getattr(report, "extra", [])
            # report.extra.append(extra_image)

            html_link = f'<a href="{file_path}" target="_blank">Screenshot</a>'
            report.extra.append(pytest_html.extras.html(html_link))"""
#

from selenium import webdriver
import pytest, os
from datetime import datetime

driver = None

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)

            driver = item.funcargs.get("browser")
            if driver:
                os.makedirs("screenshots", exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                file_name = f"{item.name}_{timestamp}.png"
                file_path = os.path.abspath(os.path.join("screenshots", file_name))
                driver.save_screenshot(file_path)
                file_name1 = file_path
                file_name = _capture_screenshot(driver)

            if file_name:
                #html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" onclick="window.open(this.src)" align="right"/></div>' % file_name
                #html = '<div> <a href="javascript:" onclick= "changeImg(data:image/png;base64,%s)" target="_blank" rel="noopener noreferrer"> <img src="data:image/png;base64,%s" alt="screenshot" style="width:304px;height:228px;"  align="right"/></a></div>' % (file_name, file_name)
                #html = """<a href="javascript:" onclick="changeImg('data:image/png;base64,{}')" >Click for screenshot</a>""".format(file_name)
                html = '<div> <img src="data:image/png;base64,%s" alt="screenshot" style="width:304px;height:228px;" onclick="window.open(data:image/png;base64,%s)" align="right"/></div>' % (file_name, file_name1)
                extra.append(pytest_html.extras.html(html))
    report.extra = extra

def _capture_screenshot(name="", *args):
    #driver.get_screenshot_as_file(name)
    try:
        # Capture screenshot as base64 string
        return driver.get_screenshot_as_base64()
    except Exception as e:
        print(f"Failed to capture screenshot: {e}")
        return None


@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Firefox()  # Replace with webdriver.Chrome("path_to_chromedriver") for Chrome
    return driver