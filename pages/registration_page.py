from playwright.sync_api import Page

class RegistrationPage:
    """Page Object para el formulario de registro de Parabank."""

    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.locator("#customer\\.firstName")
        self.last_name = page.locator("#customer\\.lastName")
        self.street = page.locator("#customer\\.address\\.street")
        self.city = page.locator("#customer\\.address\\.city")
        self.state = page.locator("#customer\\.address\\.state")
        self.zipcode = page.locator("#customer\\.address\\.zipCode")
        self.phone = page.locator("#customer\\.phoneNumber")
        self.ssn = page.locator("#customer\\.ssn")
        self.username = page.locator("#customer\\.username")
        self.password = page.locator("#customer\\.password")
        self.repeatpassword = page.locator("#repeatedPassword")
        self.submit_button = page.locator("input[value='Register']")

    def goto(self, base_url: str) -> None:
        """Navega al formulario de registro."""
        self.page.goto(f"{base_url}/register.htm")
        self.page.screenshot(path="screenshots/registration_page_001.png")

    def fill_registration_form(
        self,
        first_name: str, last_name: str, street: str, city: str, state: str,
        zipcode: str, phone: str, ssn: str, username: str, password: str, repeatpassword: str
    ) -> None:
        """Llena y envía el formulario de registro."""
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.street.fill(street)
        self.city.fill(city)
        self.state.fill(state)
        self.zipcode.fill(zipcode)
        self.phone.fill(phone)
        self.ssn.fill(ssn)
        self.username.fill(username)
        self.password.fill(password)
        self.repeatpassword.fill(repeatpassword)
        self.page.screenshot(path="screenshots/registration_filled_002.png")
        self.submit_button.click()
