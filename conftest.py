import os
from datetime import datetime
import pytest
from pytest_html import extras
from playwright.sync_api import sync_playwright

os.makedirs("screenshots", exist_ok=True)


@pytest.fixture(scope="session")
def browser():
   with sync_playwright() as p:
       browser = p.chromium.launch(headless=False)
       yield browser
       browser.close()

@pytest.fixture
def page(browser):
   page = browser.new_page()
   yield page
   page.close()

   # @pytest.hookimpl(hookwrapper=True)
   # def pytest_runtest_makereport(item, call):
   #     outcome = yield
   #     rep = outcome.get_result()
   #
   #     if rep.when == "call":
   #         if "page" in item.funcargs:
   #             page = item.funcargs["page"]
   #             test_name = item.name
   #             status = "PASSED" if rep.passed else "FAILED"
   #             timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
   #             screenshot_path = f"screenshots/{test_name}_{status}_{timestamp}.png"
   #
   #             page.screenshot(path=screenshot_path)
   #
   #             if not hasattr(rep, "extra"):
   #                 rep.extra = []
   #             rep.extra.append(extras.image(screenshot_path))
