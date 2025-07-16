# README.md

# Parabank Registration Test Automation

This project is an automated testing suite for the user registration flow on the Parabank website using Playwright. It verifies that the registration process works as expected by simulating user interactions and validating outcomes.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd parabank_registration_test
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up Playwright:
   ```
   playwright install
   ```

## Running the Tests

To execute the automated tests, run the following command:
```
pytest tests/test_registration.py
```

Alternatively, you can run the batch script to automate the setup and execution:
```
run_tests.bat
```

## Technologies Used

- Python
- Playwright
- pytest

This project follows best practices for organizing code and maintaining clean, reusable components.
