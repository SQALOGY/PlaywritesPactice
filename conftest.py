import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    """
    Pytest fixture:
    - Launches maximized browser before each test
    - Provides page to test
    - Closes everything after each test
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--start-maximized"]   
        )
        context = browser.new_context(
            no_viewport=True              
        )
        page = context.new_page()

        yield page                        

        context.close()
        browser.close()