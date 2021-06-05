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

    # Click text=全部活动
    page.click("text=全部活动")
    # assert page.url == "http://127.0.0.1:8000/all-0-0-0"

    # Click [placeholder="请输入搜索内容"]
    page.click("[placeholder=\"请输入搜索内容\"]")

    # Fill [placeholder="请输入搜索内容"]
    page.fill("[placeholder=\"请输入搜索内容\"]", "棒球")

    # Click text= 搜索
    page.click("text= 搜索")
    # assert page.url == "http://127.0.0.1:8000/all-0-0-0"

    # Click img[alt="Gallery"]
    page.click("img[alt=\"Gallery\"]")
    # assert page.url == "http://127.0.0.1:8000/single/14/"

    # Click text=全部帖子
    page.click("text=全部帖子")
    # assert page.url == "http://127.0.0.1:8000/all-0-0-0"

    # Click [placeholder="请输入搜索内容"]
    page.click("[placeholder=\"请输入搜索内容\"]")

    # Fill [placeholder="请输入搜索内容"]
    page.fill("[placeholder=\"请输入搜索内容\"]", "17")

    # Click text= 搜索
    page.click("text= 搜索")
    # assert page.url == "http://127.0.0.1:8000/all-0-0-0"

    # Click li:nth-child(7) a img
    page.click("li:nth-child(7) a img")
    # assert page.url == "http://127.0.0.1:8000/single/14/"

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)