
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page = browser.new_page()
        print(type(page))
        page.goto("https://demoqa.com/text-box")
        # page.fill("#userName","Rahul Sharma")
        page.locator("#userName").press_sequentially("Rahul Sharma")
        page.wait_for_timeout(3000)

        page.fill("#userEmail","Rahul12@gmail.com")
        page.wait_for_timeout(3000)

        page.fill("#currentAddress","Chandinini Chowk Parathe wali gali")
        page.click("#submit")

        page.wait_for_timeout(3000)
        browser.close()
run()
print("This is the last line")
