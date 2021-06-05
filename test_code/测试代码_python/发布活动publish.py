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

    # Click text=发布活动
    page.click("text=发布活动")
    # assert page.url == "http://127.0.0.1:8000/publish/"

    # Click input[name="t_title"]
    page.click("input[name=\"t_title\"]")

    # Fill input[name="t_title"]
    page.fill("input[name=\"t_title\"]", "打网球")

    # Click input[name="location"]
    page.click("input[name=\"location\"]")

    # Fill input[name="location"]
    page.fill("input[name=\"location\"]", "胡发光")

    # Click input[name="location"]
    page.click("input[name=\"location\"]")

    # Click input[name="location"]
    page.click("input[name=\"location\"]")

    # Click input[name="location"]
    page.click("input[name=\"location\"]")

    # Click input[name="location"]
    page.click("input[name=\"location\"]")

    # Fill input[name="location"]
    page.fill("input[name=\"location\"]", "胡法光网球场")

    # Click input[name="t_number"]
    page.click("input[name=\"t_number\"]")

    # Fill input[name="t_number"]
    page.fill("input[name=\"t_number\"]", "2")

    # Click input[name="t_time"]
    page.click("input[name=\"t_time\"]")

    # Click td:has-text("31")
    page.click("td:has-text(\"31\")")

    # Click textarea[name="t_content"]
    page.click("textarea[name=\"t_content\"]")

    # Fill textarea[name="t_content"]
    page.fill("textarea[name=\"t_content\"]", "一起打网球")

    # Click textarea[name="t_contact"]
    page.click("textarea[name=\"t_contact\"]")

    # Fill textarea[name="t_contact"]
    page.fill("textarea[name=\"t_contact\"]", "12345678912")

    # Click text=发布活动
    page.click("text=发布活动")
    # assert page.url == "http://127.0.0.1:8000/single/28/"

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)