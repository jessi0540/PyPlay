from pages.home_page import HomePage                    # corregido
from pages.registration_page import RegistrationPage    # corregido

def test_user_registration(page):
    # Navigate to the registration page
    registration_page = RegistrationPage(page)
    registration_page.go_to_registration_form()

    # Prepare test data
    test_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'address': '123 Main St',
        'city': 'Anytown',
        'state': 'CA',
        'zip_code': '12345',
        'phone': '555-1234',
        'ssn': '123-45-6789',
        'username': 'jessi0540',
        'password': 'password123',
        'confirm_password': 'password123'
    }

    # Fill the registration form
    registration_page.fill_registration_form(test_data)

    # Verify successful registration
    home_page = HomePage(page)
    assert home_page.is_registration_successful(), "Registration was not successful."