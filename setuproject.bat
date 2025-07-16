@echo off
echo Creando estructura de carpetas y archivos...

:: Crear carpetas
mkdir .github
mkdir .github\workflows
mkdir pages
mkdir tests
mkdir utils

:: Crear archivos vacíos
type nul > .github\workflows\ci.yml
type nul > pages\someaction_page.py
type nul > tests\test_someaction.py
type nul > utils\config.py
type nul > playwright.config.py
type nul > conftest.py
type nul > requirements.txt
type nul > README.md
type nul > .gitignore
type nul > run_tests.bat

echo Proyecto generado exitosamente.
pause