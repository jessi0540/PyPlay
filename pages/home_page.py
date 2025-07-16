class HomePage:
    def __init__(self, page):
        self.page = page

    def is_registration_successful(self):
        # Implement logic to verify if registration was successful
        success_message_selector = "text=Your account was created successfully. You are now logged in."  # Corregido
        return self.page.is_visible(success_message_selector)

    