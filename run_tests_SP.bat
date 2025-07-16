@echo off
REM Install dependencies
pip install -r requirements.txt

REM Install Playwright browsers
playwright install

REM Run the tests
pytest tests/test_registration.py --headed


pause