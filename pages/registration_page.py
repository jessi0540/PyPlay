class RegistrationPage:
    # Registration page
    def __init__(self, page):
        self.page = page

    def go_to_registration_form(self):
        self.page.goto("https://parabank.parasoft.com/parabank/register.htm")

    def fill_registration_form(self, data):
        self.page.fill("#customer\\.firstName", data['first_name'])
        self.page.fill("#customer\\.lastName", data['last_name'])
        self.page.fill("#customer\\.address\\.street", data['address'])
        # tomar captura de pantalla
        self.page.screenshot(path="screenshots/registration_page_001.png")
        self.page.fill("#customer\\.address\\.city", data['city'])
        self.page.fill("#customer\\.address\\.state", data['state'])
        # espera implicita  
        self.page.fill("#customer\\.address\\.zipCode", data['zip_code']) # corregido locator y nombrado en test registration
        self.page.fill("#customer\\.phoneNumber", data['phone'])
        self.page.fill("#customer\\.ssn", data['ssn']) # corregido
        #-instruccion de captura de pantalla
        self.page.screenshot(path="screenshots/registration_page_00.png")  # aumentado
        self.page.fill("#customer\\.username", data['username'])
        self.page.fill("#customer\\.password", data['password'])
        self.page.fill("#repeatedPassword", data['password'])
        self.page.screenshot(path="screenshots/registration_page_01.png")  # aumentado
        #Instrucción de bajar scroll
        self.page.evaluate("window.scrollBy(0, 1000)")  # aumentado
        self.page.click("input[value='Register']") # corregido locator
        self.page.wait_for_timeout(10000)
        self.page.screenshot(path="screenshots/registration_page_02.png") # aumentado
        #Agregar una aptura de panlla
        self.page.screenshot(path="screenshots/registration_page_03.png")
        self.page.wait_for_timeout(10000)
         #-instruccion de captura de pantalla
         