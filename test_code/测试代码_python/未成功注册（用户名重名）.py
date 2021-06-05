from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://127.0.0.1:8000/
    page.goto("http://127.0.0.1:8000/")

    # Click [placeholder="账号"]
    page.click("[placeholder=\"账号\"]")

    # Fill [placeholder="账号"]
    page.fill("[placeholder=\"账号\"]", "test2")

    # Click [placeholder="密码"]
    page.click("[placeholder=\"密码\"]")

    # Fill [placeholder="密码"]
    page.fill("[placeholder=\"密码\"]", "12345")

    # Click text=注册
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.click("text=注册")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)