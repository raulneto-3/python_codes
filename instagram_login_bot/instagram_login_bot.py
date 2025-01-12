from playwright.sync_api import sync_playwright
import time

def login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto("https://www.instagram.com/", timeout=10000)

        page.wait_for_selector("input[name='username']")
        page.wait_for_selector("input[name='password']")

        page.fill("input[name='username']", "your_username")
        page.fill("input[name='password']", "your_password")

        page.click("button[type='submit']")

        input("Press any key to close the browser...")

def main():
    while True:
        login()
        time.sleep(5)

if __name__ == '__main__':
    main()