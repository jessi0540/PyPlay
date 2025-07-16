@echo off
REM Install dependencies
pip install -r requirements_sinPoetry.txt

REM Install Playwright browsers
playwright install

REM Run the tests
pytest tests/test_registration.py --headed


pause