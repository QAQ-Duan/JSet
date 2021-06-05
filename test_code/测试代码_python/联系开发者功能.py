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
    page.fill("[placeholder=\"密码\"]", "123456")

    # Click button:has-text("登录")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.click("button:has-text(\"登录\")")

    # Click [placeholder="密码"]
    page.click("[placeholder=\"密码\"]")

    # Fill [placeholder="密码"]
    page.fill("[placeholder=\"密码\"]", "12345")

    # Click button:has-text("登录")
    # with page.expect_navigation(url="http://127.0.0.1:8000/home/"):
    with page.expect_navigation():
        page.click("button:has-text(\"登录\")")

    # Click text=联系我们
    page.click("text=联系我们")
    # assert page.url == "http://127.0.0.1:8000/contact/"

    # Click input[name="con_name"]
    page.click("input[name=\"con_name\"]")

    # Fill input[name="con_name"]
    page.fill("input[name=\"con_name\"]", "test1")

    # Click input[name="con_phone"]
    page.click("input[name=\"con_phone\"]")

    # Fill input[name="con_phone"]
    page.fill("input[name=\"con_phone\"]", "12345671234")

    # Click input[name="con_subject"]
    page.click("input[name=\"con_subject\"]")

    # Click input[name="con_subject"]
    page.click("input[name=\"con_subject\"]")

    # Fill input[name="con_subject"]
    page.fill("input[name=\"con_subject\"]", "just for test")

    # Click text= 提交
    page.click("text= 提交")
    # assert page.url == "http://127.0.0.1:8000/contact/"

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)