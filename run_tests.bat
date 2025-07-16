
@echo off
echo Instalando dependencias...
pip install -r requirements.txt

echo Instalando navegadores...
playwright install

echo Ejecutando pruebas...
pytest tests/test_registration.py --html=reports/report.html --self-contained-html
pause
