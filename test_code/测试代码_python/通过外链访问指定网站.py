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

    # Click button:has-text("登录")
    # with page.expect_navigation(url="http://127.0.0.1:8000/home/"):
    with page.expect_navigation():
        page.click("button:has-text(\"登录\")")

    # Click text=体育场馆预约
    page.click("text=体育场馆预约")
    # assert page.url == "https://sports.sjtu.edu.cn/pc/#/"

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)