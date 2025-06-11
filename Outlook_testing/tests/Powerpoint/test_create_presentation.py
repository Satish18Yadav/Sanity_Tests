import os,pytest
from dotenv import load_dotenv

from patchright.sync_api import sync_playwright,expect,Playwright,Page
load_dotenv()

@pytest.fixture(scope='session')
def open_powerpoint():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def create_browser(open_powerpoint : Playwright):
    browser = open_powerpoint.chromium.launch(headless=False)
    context = browser.new_context(viewport={'width':1360, 'height':770})
    page = context.new_page()
    yield page

'''
This method is also not working

def handle_alert(dialog):
    print(f"Dialog message: {dialog.message}")
    dialog.accept()
'''


@pytest.mark.sanity
def test_create_presentation(create_browser : Page):
    page = create_browser
    page.goto("https://www.powerpoint.com")

    sign_in = page.get_by_role("textbox", name="Enter your email, phone, or")
    sign_in.wait_for(state='visible',timeout=3000)
    sign_in.fill(os.getenv("TEST_EMAIL")) #type: ignore

    Next_button = page.get_by_role("button", name="Next")
    Next_button.wait_for(state="visible")
    expect(Next_button).to_be_visible()
    Next_button.click()

    password_section = page.get_by_role("textbox", name="Password")
    password_section.wait_for(state='visible')
    expect(password_section).to_be_visible()
    password_section.fill(os.getenv("TEST_PASSWORD")) # type: ignore

    page.wait_for_timeout(2000)

    page.get_by_test_id("primaryButton").click()

    page.get_by_test_id("secondaryButton").click()

    blank_presentation = page.get_by_role("link", name="Create a new blank")
    blank_presentation.wait_for(state='visible',timeout=30000)
    expect(blank_presentation).to_be_visible()

    # capturing the new tab 
    with page.context.expect_page() as new_page_info:
     blank_presentation.click()
     new_page = new_page_info.value
    #  new_page.close()
     new_page.bring_to_front()
     new_page.wait_for_timeout(5000)
     new_page.bring_to_front()

     accept_button = new_page.locator("xpath=//button[contains(text(), 'Accept') and contains(@style, 'background-color: rgb(74, 74, 74)') and contains(@style, 'color: rgb(243, 243, 243)')]")
     accept_button.wait_for(state="visible", timeout=10000)
     accept_button.click()
        
    # new_page.close()
    # new_page.get_by_role("button", name="Accept").click()
    # accept_button = new_page.wait_for_selector("//button[text()='Accept']")
    # accept_button = new_page.locator("pierce/button:contains('Accept')")

   # if accept_button.count() > 0 and accept_button.is_visible(timeout=30000): # type: ignore
     #   accept_button.wait_for(state="visible", timeout=30000) # type: ignore
       # accept_button.click() # type: ignore
    #     print("Clicked Accept button on warning page.")
    #else:
       # print("Accept button not found or not visible on warning page.")
    
    
    page.pause()
    
    

