import os
from datetime import datetime
import pytest
from pytest_html import extras
from playwright.sync_api import sync_playwright

os.makedirs("screenshots", exist_ok=True)


@pytest.fixture(scope="session")
def browser():
   with sync_playwright() as p:
       browser = p.chromium.launch(headless=False, slow_mo=2000)
       yield browser
       browser.close()

@pytest.fixture
def page(browser):
   page = browser.new_page()
   #print("✅ Page fixture is EXECUTING")

   yield page
   page.close()
   #print("❌ Page fixture is CLOSED")

