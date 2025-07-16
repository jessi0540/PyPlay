class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def wait_for_element(self, selector):
        from playwright.sync_api import Page
        page: Page = self.driver
        page.wait_for_selector(selector)