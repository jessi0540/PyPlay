
from utils.config import BASE_URL
from pages.registration_page import RegistrationPage

def test_successful_registration(page):
    registration = RegistrationPage(page)
    registration.goto(BASE_URL)
    registration.fill_registration_form(
    "Jess", "Esquivel", "Benito Juarez", "CDMX", "CDMX",
    "03100", "5551019999", "6343746", "jessi0540", "testpass", "testpass"
)

    assert "ParaBank" in page.title()
