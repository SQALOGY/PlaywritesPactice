from playwright.sync_api import sync_playwright
import time

def test_two_tabs_google():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--start-maximized"]
        )
        context = browser.new_context(no_viewport=True)

        # Tab 1 - Google
        page1 = context.new_page()
        page1.goto("https://www.google.com")
        time.sleep(2)
        print("Tab 1 title:", page1.title())

        # Tab 2 - Gmail
        page2 = context.new_page()
        page2.goto("https://www.gmail.com")
        time.sleep(2)
        print("Tab 2 title:", page2.title())

        # Switch back to Tab 1
        page1.bring_to_front()
        time.sleep(2)
        print("✅ Switched back to Tab 1:", page1.title())

        context.close()
        browser.close()