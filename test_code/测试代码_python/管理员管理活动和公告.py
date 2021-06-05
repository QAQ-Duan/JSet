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

    # Click text=管理员登录>
    page.click("text=管理员登录>")
    # assert page.url == "http://127.0.0.1:8000/my-admin/"

    # Click [placeholder="账号"]
    page.click("[placeholder=\"账号\"]")

    # Fill [placeholder="账号"]
    page.fill("[placeholder=\"账号\"]", "guanliyuan")

    # Click [placeholder="密码"]
    page.click("[placeholder=\"密码\"]")

    # Fill [placeholder="密码"]
    page.fill("[placeholder=\"密码\"]", "123456")

    # Click button:has-text("登录")
    # with page.expect_navigation(url="http://127.0.0.1:8000/admin-home/"):
    with page.expect_navigation():
        page.click("button:has-text(\"登录\")")

    # Click text=公告管理
    page.click("text=公告管理")
    # assert page.url == "http://127.0.0.1:8000/announcement/"

    # Click input[type="text"]
    page.click("input[type=\"text\"]")

    # Fill input[type="text"]
    page.fill("input[type=\"text\"]", "test")

    # Click textarea
    page.click("textarea")

    # Fill textarea
    page.fill("textarea", "just for test")

    # Click text=发布公告
    page.click("text=发布公告")
    # assert page.url == "http://127.0.0.1:8000/announcement/?"

    # Click text=公告管理
    page.click("text=公告管理")
    # assert page.url == "http://127.0.0.1:8000/announcement/"

    # Click text=查看
    page.click("text=查看")
    # assert page.url == "http://127.0.0.1:8000/single-an-3/"

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)